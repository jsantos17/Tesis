from lib.util.SweepType import SweepType
from lib.util.SourceType import SourceType
from lib.util.SourceMode import SourceMode
from lib.SMUSweep import SMUSweep
from lib.K4200 import K4200
from lib.VnaChannel import VnaChannel
from lib.util.DataTransformers import z_from_s, y_from_s, cga_from_s, cgs_from_s
from gui.VnaMeasure import chunker, write_vector, write_2vectors, write_4vectors
from thread import start_new_thread
import time

gdata = {} 

def con_alt_measure(smu_params, vna_params, delay, conn_keithley, conn_vna):
    points = smu_params["steps"]
    sweep_time = delay*points
    # Prepare K4200 to measure 

    ch = smu_params["index"] + 1
    if smu_params["mode"] == "voltage":
        source_mode = SourceMode.VOLTAGE
        source_type = SourceType.VOLTAGE

    if smu_params["mode"] == "current":
        source_mode = SourceMode.CURRENT
        source_type = SourceType.CURRENT

    start = smu_params["start"]
    stop = smu_params["stop"]
    step = smu_params["step"]
    compliance = smu_params["compliance"]
    sweep_type = SweepType.LINEAR # Always linear.

    smu = SMUSweep(ch, source_mode, source_type, start, stop, step, 
            compliance, sweep_type, 'V%s' % ch, "I%s"%ch)
    
    device = K4200(conn_keithley[0], conn_keithley[1])
    device.attach(smu)
    device.configure()
    device.executor.execute_command("SS DT {time}".format(time=delay))

    # Prepare VNA to measure

    vna = VnaChannel(conn_vna[0], conn_vna[1], 1)
    vna.set_four_channels()
    vna.set_bus_trigger()

    def measure_vna(vna):
        vna.trigger()

    def measure_keithley(keithley):
        keithley.measure()

    for i in range(1,5): # Measure using four channels, once per S parameter
        vna.channel = i
        vna.set_continuous(False)
        vna.set_immediate()
        vna.activate_channel()
        vna.set_traces(1)
        vna.activate_trace(1)
        vna.set_points(points)
        vna.set_format(vna_params["format"])
        vna.set_sparam(1, i) # Assign S11 to ch1, S12 to ch2, S21 to ch3 and S22 to ch4
        vna.set_sweep_time(sweep_time)

        if vna_params["type"] == "center_span":
            vna.set_center_span(vna_params["freq_center"], vna_params["freq_span"])
        elif vna_params["type"] == "start_stop":
            vna.set_center_span(vna_params["freq_start"], vna_params["freq_stop"])

    # Run in different threads to ensure start at the same time
    start_new_thread(measure_vna, (vna,))
    start_new_thread(measure_keithley, (device,))
    start_new_thread(check_vna, (vna,vna_params))
    start_new_thread(check_keithley, (device,smu_params))


def check_vna(vna, vna_params):
    while not vna.is_ready():
        time.sleep(1)
        print "Waiting for VNA"
    print "VNA is ready"
    retrieve_vna_data(vna)
    vna.executor.close()

def check_keithley(device, smu_params):
    while not device.is_ready():
        time.sleep(1)
        print "Waiting for K4200"
    print "K4200 is ready"
    retrieve_keithley_data(device)
    device.executor.close()

def retrieve_keithley_data(device, smu_params):
    ch = smu_params["index"] + 1
    cmd = "DO 'CH{ch}T'".format(ch=ch)
    data = device.executor.ask(cmd)
    data = data.split(",")
    data = [float(datum) for datum in data]
    gdata["pol"] = data
    write_vector(data, smu_params["file"] + "_pol.csv")
    
    retrieve_both()

def retrieve_vna_data(vna, vna_params):
    sdata = []
    freq_data = []
    template = ":CALC{ch}:DATA:FDAT?"
    template_freq = ":SENS{ch}:FREQ:DATA?"
    for channel in [1,2,3,4]:
        data = vna.executor.ask(template.format(ch=str(channel)))
        fdata = vna.executor.ask(template_freq.format(ch=str(channel)))
        fdata = fdata.split(',')
        data = data.split(',')
        data = [complex(float(pair[0]), float(pair[1])) for pair in chunker(data, 2)]
        
        sdata.append(data)
        freq_data.append(fdata)

    ydata = y_from_s(sdata)
    zdata = z_from_s(sdata)
    cga_data = cga_from_s(sdata)
    cgs_data = cgs_from_s(sdata)
    capacitance = [cga, cgs]
    gdata["cap"] = capacitance
    write_4vectors(freq_data, vna_params["file"] + "_freqs.csv")
    write_4vectors(sdata, vna_params["file"] + "_s.csv")
    write_4vectors(zdata, vna_params["file"] + "_z.csv")
    write_4vectors(ydata, vna_params["file"] + "_y.csv")
    write_2vectors(capacitance, vna_params["file"] + "_cap.csv")
    
    retrieve_both()

def retrieve_both():
    try:
        cap = gdata["cap"]
        pol = gdata["pol"]
    except KeyError as e: # The other routine has not finished yet, return and wait for next call
        return
    
    v_cga = [pol, cap[0]]
    v_cgs = [pol, cap[1]]

    write_2vectors(v_cga, "v_vs_cga.csv")
    write_2vectors(v_cgs, "v_vs_cgs.csv")
