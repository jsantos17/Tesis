from lib.util.SweepType import SweepType
from lib.util.SourceType import SourceType
from lib.util.SourceMode import SourceMode
from lib.SMUSweep import SMUSweep
from lib.K4200 import K4200
from lib.VnaChannel import VnaChannel
from thread import start_new_thread

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
    device.executor.execute_command("SS DT {time}".format(time=delay))

    # Prepare VNA to measure

    vna = VnaChannel(conn_vna[0], conn_vna[1], 1)
    vna.set_four_channels()

    def measure_vna(vna):
        vna.trigger()

    def measure_keithley(keithley)
        keithley.measure()

    for i in range(1,5): # Measure using four channels, once per S parameter
        vna.channel = i
        vna.set_continuous(False)
        vna.set_immediate()
        vna.set_bus_trigger()
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

