from SocketExecutor import SocketExecutor
from MockExecutor import MockExecutor
from lib.util.VnaEnums import SweepType
from lib.util.VnaEnums import SParameters 

class Vna(object):
    def __init__(self, ip, port):
        self.executor = MockExecutor(ip, port)

    def reset(self):
        self.executor.execute_command(":SYST:PRES")

    def set_one_channel(self):
        self.executor.execute_command(":DISP:SPL D1")

    def set_continuous(self, channel):
        template = ":INIT{ch}:CONT ON"
        cmd = template.format(ch=channel)
        self.executor.execute_command(cmd)

    def set_sweep_type(self, channel, sweep_type):
        if sweep_type == SweepType.LINEAR:
            stype = "LIN"
        elif sweep_type == SweepType.LOG:
            stype = "LOG"
        elif sweep_type == SweepType.SEGM:
            stype = "SEGM"
        elif sweep_type == SweepType.POW:
            stype = "POW"
        template = ":SENS{ch}:SWE:TYPE {stype}"
        cmd = template.format(ch=channel, stype=stype)
        self.executor.execute_command(cmd)

    def set_center_span(self, channel, center, span):
        template_center = ":SENS{ch}:FREQ:CENT {center}"
        template_span = ":SENS{ch}:FREQ:SPAN {span}"
        cmd_center = template_center.format(ch=channel, center=center)
        cmd_span = template_span.format(ch=channel, span=span)
        self.executor.execute_command(cmd_center)
        self.executor.execute_command(cmd_span)

    def set_start_stop(self, channel, start, stop):
        template_start = ":SENS{ch}:FREQ:STAR {start}"
        template_stop = ":SENS{ch}:FREQ:STOP {stop}"
        cmd_start = template_start.format(ch=channel, start=start)
        cmd_stop = template_stop.format(ch=channel, stop=stop)
        self.executor.execute_command(cmd_start)
        self.executor.execute_command(cmd_stop)

    def activate_channel(self, channel):
        template = ":DISP:WIND{ch}:ACT"
        cmd = template.format(ch=channel)
        self.executor.execute_command(cmd)

    def activate_trace(self, channel, trace):
        template = ":CALC{ch}:PAR{tr}:SEL"
        cmd = template.format(ch=channel, tr=trace)
        self.executor.execute_command(cmd)
       
    def set_traces(self, channel, trace):
        template = ":CALC{ch}:PAR:COUNT {trace}"
        cmd = template.format(ch=channel, trace=trace)
        self.executor.execute_command(cmd)

    def add_marker(self, channel, trace, marker):
        cmd = ":CALC{channel}:TRAC{trace}:MARK{marker}:ACT".format(
                channel=channel, trace=trace, marker=marker)
        self.executor.execute_command(cmd)

    def set_sparam_for_chan(self, channel, sparam):
        template = ":CALC{ch}:PAR:DEF '{sparam}_ch{ch}',{sparam}"
        if sparam == SParameters.S11:
            sparam = "S11"
        elif sparam == SParameters.S12:
            sparam = "S12"
        elif sparam == SParameters.S21:
            sparam = "S21"
        elif sparam == SParameters.S22:
            sparam = "S22"

        cmd = template.format(ch=channel, sparam=sparam)
        self.executor.execute_command(cmd)

    def set_points(self, channel, points):
        template = ":SENS{ch}:SWE:POIN {points}"
        template.format(ch=channel, points=points)

