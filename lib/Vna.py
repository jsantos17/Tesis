from SocketExecutor import SocketExecutor
from MockExecutor import MockExecutor
from lib.util.VnaEnums import SweepType
from lib.util.VnaEnums import SParameters 
from lib.util.VnaEnums import CalType 
from lib.util.VnaEnums import DataFormat 

class Vna(object):
    def __init__(self, ip, port):
        self.executor = SocketExecutor(ip, port, expect_reply=False, endline="\n")

    def reset(self):
        self.executor.execute_command(":SYST:PRES")

    def is_ready(self):
        return "+1" in self.executor.ask("*OPC?")

    def set_one_channel(self):
        self.executor.execute_command(":DISP:SPL D1")

    def set_cal_kit(self, channel, kit):
        template = ":SENS{ch}:CORR:COLL:CKIT {kit}"
        cmd = template.format(ch=channel,kit=kit)
        self.executor.execute_command(cmd)

    def set_cal_type(self, channel, cal_type, port=None):
        if cal_type == CalType.OPEN:
            template = ":SENS{ch}:CORR:COLL:METH:OPEN {port}"
        elif cal_type == CalType.SHORT:
            template = ":SENS{ch}:CORR:COLL:METH:SHORT {port}"
        elif cal_type == CalType.THRU:
            template = ":SENS{ch}:CORR:COLL:METH:THRU {port}"
        elif cal_type == CalType.FULL_2PORT:
            template = ":SENS{ch}:CORR:COLL:METH:SOLT2 1, 2"
        elif cal_type == CalType.FULL_1PORT:
            template = ":SENS{ch}:CORR:COLL:METH:SOLT1 {port}"
        elif cal_type == CalType.TRL_2PORT:
            template = ":SENS{ch}:CORR:COLL:METH:TRL2 1, 2"

        cmd = template.format(ch=channel, port=port)
        self.executor.execute_command(cmd)

    def cal_measure_open(self, channel, port):
        template = ":SENS{ch}:CORR:COLL:OPEN {port}"
        self.executor.execute_command(template.format(ch=channel, port=port))

    def cal_measure_short(self, channel, port):
        template = ":SENS{ch}:CORR:COLL:SHOR {port}"
        self.executor.execute_command(template.format(ch=channel, port=port))

    def cal_measure_load(self, channel, port):
        template = ":SENS{ch}:CORR:COLL:LOAD {port}"
        self.executor.execute_command(template.format(ch=channel, port=port))

    def cal_measure_thru(self, channel, port_x, port_y):
        template = ":SENS{ch}:CORR:COLL:THRU {port_x},{port_y}"
        self.executor.execute_command(template.format(port_x = port_x, port_y = port_y, ch = channel))

    def cal_measure_isol(self, channel, port_x, port_y):
        template = ":SENS{ch}:CORR:COLL:ISOL {port_x},{port_y}"
        self.executor.execute_command(template.format(port_x = port_x, port_y = port_y, ch = channel))

    def trl_thru_line(self, channel, port_x, port_y):
        template = ":SENS{ch}:CORR:COLL:METH:TRLT {port_x}, {port_y}"
        self.executor.execute_command(template.format(port_x = port_x, port_y = port_y, ch = channel))

    def trl_reflect(self, channel, port):
        template = ":SENS{ch}:CORR:COLL:ACQ:TRLR {port}"
        self.executor.execute_command(template.format(ch=channel, port=port))

    def trl_line_match(self, channel, port_x, port_y):
        template = ":SENS{ch}:CORR:COLL:ACQ:TRLL {port_x},{port_y}"
        self.executor.execute_command(template.format(ch=channel, port_x=port_x, port_y=port_y))

    def save_cal(self, channel):
        template = ":SENS{ch}:CORR:COLL:SAVE"
        template.format(ch=channel)
        self.executor.execute_command(template.format(ch=channel))

    def set_continuous(self, channel):
        template = ":INIT{ch}:CONT ON"
        cmd = template.format(ch=channel)
        self.executor.execute_command(cmd)

    def auto_scale(self, channel):
        template = ":DISP:WIND{ch}:TRAC1:Y:AUTO"
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
        template = ":CALC{ch}:PAR:COUN {trace}"
        cmd = template.format(ch=channel, trace=trace)
        self.executor.execute_command(cmd)

    def add_marker(self, channel, trace, marker):
        cmd = ":CALC{channel}:TRAC{trace}:MARK{marker}:ACT".format(
                channel=channel, trace=trace, marker=marker)
        self.executor.execute_command(cmd)

    def set_x(self, channel, new_x, mark):
        cmd = ":CALC{ch}:MARK{mark}:X {new_x}".format(ch=channel, mark=mark, new_x = new_x)
        self.executor.execute_command(cmd)

    def get_x(self, channel, mark):
        cmd = ":CALC{ch}:MARK{mark}:X?".format(ch=channel, mark=mark)
        return float(self.executor.ask(cmd))

    def get_y(self, channel, mark):
        cmd = ":CALC{ch}:MARK{mark}:Y?".format(ch=channel, mark=mark)
        result = str(self.executor.ask(cmd))
        result = result.split(",")
        y_re = float(result[0])
        y_im = float(result[1])

        return (y_re, y_im) # We return a tuple with a real part and and an imaginary part 

    def get_start_x(self, channel):
        x = ":SENS{ch}:FREQ:STAR?".format(ch=channel)
        return float(self.executor.ask(x))

    def get_stop_x(self, channel):
        x = ":SENS{ch}:FREQ:STOP?".format(ch=channel)
        return float(self.executor.ask(x))

    def set_sparam(self, channel, trace, sparam):
        template = ":CALC{ch}:PAR{tr}:DEF {sparam}"
        if sparam == SParameters.S11:
            sparam = "S11"
        elif sparam == SParameters.S12:
            sparam = "S12"
        elif sparam == SParameters.S21:
            sparam = "S21"
        elif sparam == SParameters.S22:
            sparam = "S22"

        cmd = template.format(ch=channel, sparam=sparam, tr=trace)
        self.executor.execute_command(cmd)

    def set_points(self, channel, points):
        template = ":SENS{ch}:SWE:POIN {points}"
        cmd = template.format(ch=channel, points=points)
        self.executor.execute_command(cmd)

    def turn_on(self):
        self.executor.execute_command(":OUTP")

    def trigger(self):
        self.executor.execute_command(":TRIG:IMM")

    def set_format(self, channel, fmat):
        if fmat not in [DataFormat.LOG, DataFormat.LIN, DataFormat.LIN_PHASE, DataFormat.PHASE,
                    DataFormat.GDELAY, DataFormat.SMITH_LIN_PHASE, DataFormat.SMITH_LOG_PHASE,
                    DataFormat.SMITH_RE_IM, DataFormat.SMITH_R_JX, DataFormat.SMITH_G_JB]:
            raise VnaConfigError("Data format should be defined from DataFormat enum")

        template = ":CALC{ch}:SEL:FORM {fmat}"

        if fmat == DataFormat.LOG:
            cmd_fmat = "MLOG"
        elif fmat == DataFormat.LIN:
            cmd_fmat = "MLIN"
        elif fmat == DataFormat.LIN_PHASE:
            cmd_fmat = "PLIN"
        elif fmat == DataFormat.GDELAY:
            cmd_fmat = "GDEL"
        elif fmat == DataFormat.SMITH_LIN_PHASE:
            cmd_fmat = "SLIN"
        elif fmat == DataFormat.SMITH_LOG_PHASE:
            cmd_fmat = "SLOG"
        elif fmat == DataFormat.SMITH_RE_IM:
            cmd_fmat = "SCOM"
        elif fmat == DataFormat.SMITH_R_JX:
            cmd_fmat = "SMIT"
        elif fmat == DataFormat.SMITH_G_JB:
            cmd_fmat = "SADM"

        self.executor.execute_command(template.format(ch=channel, fmat=cmd_fmat))

class VnaConfigError(Exception):
    pass
