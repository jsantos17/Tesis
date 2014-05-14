from lib.util.SweepType import SweepType
from lib.util.SourceType import SourceType
from lib.util.SourceMode import SourceMode
from lib.SMUSweep import SMUSweep
from lib.K4200 import K4200
from lib.VnaChannel import VnaChannel
from lib.util.DataTransformers import z_from_s, y_from_s, cga_from_s, cgs_from_s
from gui.VnaMeasure import chunker, write_vector, write_2vectors, write_4vectors
import lib.util.plotter as plotter
from thread import start_new_thread
from threading import RLock
import time
import pprint

vlock = RLock()
klock = RLock()

gdata = {} 
params = []
def con_alt_measure(smu_params, vna_params, delay, conn_keithley, conn_vna):
    points = smu_params["steps"]
    sweep_time = delay*points
    # Prepare K4200 to measure 
    params.append(smu_params)
    params.append(vna_params)
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
    # device.executor.execute_command("SS HT {time}".format(time=2.2))

    # Prepare VNA to measure

    vna = VnaChannel(conn_vna[0], conn_vna[1], 1)
    vna.set_four_channels()
    vna.set_bus_trigger()

    def measure_vna(vna):
        vlock.acquire()    
        vna.trigger()
        vlock.release()

    def measure_keithley(keithley):
        klock.acquire()
        keithley.measure()
        klock.release()

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
    while True:
        vlock.acquire()
        is_ready = vna.is_ready()
        vlock.release()
        if is_ready:
            break
        time.sleep(1)
        print "Waiting for VNA"
    print "VNA is ready"
    vna.beep()
    retrieve_vna_data(vna, vna_params)
    reset_config(vna)
    vna.executor.close()

def check_keithley(device, smu_params):
    while True:
        klock.acquire()
        is_ready = device.is_ready()
        klock.release()
        if is_ready:
            break
        time.sleep(1)
        print "Waiting for K4200"
    print "K4200 is ready"
    retrieve_keithley_data(device, smu_params)
    device.executor.close()

def retrieve_keithley_data(device, smu_params):
    ch = smu_params["index"] + 1
    cmd = "DO 'CH{ch}T'".format(ch=ch)
    data = device.executor.ask(cmd)
    print "Keithley Data:"
    pprint.pprint(data)
    data = data.split(",")
    data = [float(datum) for datum in data]
    gdata["pol"] = data
    write_vector(data, smu_params["file"] + "_pol.csv")
    
    retrieve_both()

def retrieve_vna_data(vna, vna_params):
    sdata = []
    freq_data = []
    template = ":CALC{ch}:DATA:FDAT?"
    for channel in [1,2,3,4]:
        data = vna.executor.ask(template.format(ch=str(channel)))
        data = data.split(',')
        data = [complex(float(pair[0]), float(pair[1])) for pair in chunker(data, 2)]
        sdata.append(data)
    
    template_freq = ":SENS{ch}:FREQ:DATA?"
    freq_data = vna.executor.ask(template_freq.format(ch=1))
    freq_data = freq_data.split(',')
    freq_data = [float(fdatum) for fdatum in freq_data]


    ydata = y_from_s(sdata)
    zdata = z_from_s(sdata)
    cga_data = cga_from_s(freq_data, sdata)
    cgs_data = cgs_from_s(freq_data, sdata)
    capacitance = [cga_data, cgs_data]
    gdata["cap"] = capacitance
    write_vector(freq_data, vna_params["file"] + "_freqs")
    write_4vectors(sdata, vna_params["file"] + "_s")
    write_4vectors(zdata, vna_params["file"] + "_z")
    write_4vectors(ydata, vna_params["file"] + "_y")
    write_2vectors(capacitance, vna_params["file"] + "_cap")
    
    retrieve_both()

def reset_config(vna):
    vna.set_internal_trigger()
    vna.set_one_channel()
    for ch in [1,2,3,4]:
        vna.channel = ch
        vna.set_immediate()

def retrieve_both():
    try:
        cap = gdata["cap"]
        pol = gdata["pol"]
    except KeyError as e: # The other routine has not finished yet, return and wait for next call
        return
    
    v_cga = [pol, cap[0]]
    v_cgs = [pol, cap[1]]
    print "V_cga len"
    print str(len(v_cga[0])) + "," + str(len(v_cga[1]))
    print "V_cgs len"
    print str(len(v_cgs[0])) + "," + str(len(v_cgs[1]))
    write_2vectors(v_cga, params[0]["file"] + "_v_vs_cga")
    write_2vectors(v_cgs, params[0]["file"] + "_v_vs_cgs")

    plotter.plot(pol, cga, params[0]["file"]+ "cga_plot")
    plotter.plot(pol, cgs, params[0]["file"]+ "cgs_plot")
