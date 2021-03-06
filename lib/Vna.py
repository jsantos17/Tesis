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
        template = ":SENS{ch}:CORR:COLL:TRLT {port_x}, {port_y}"
        self.executor.execute_command(template.format(port_x = port_x, port_y = port_y, ch = channel))

    def trl_reflect(self, channel, port):
        template = ":SENS{ch}:CORR:COLL:TRLR {port}"
        self.executor.execute_command(template.format(ch=channel, port=port))

    def trl_line_match(self, channel, port_x, port_y):
        template = ":SENS{ch}:CORR:COLL:TRLL {port_x},{port_y}"
        self.executor.execute_command(template.format(ch=channel, port_x=port_x, port_y=port_y))

    def save_cal(self, channel):
        template = ":SENS{ch}:CORR:COLL:SAVE"
        template.format(ch=channel)
        self.executor.execute_command(template.format(ch=channel))

    def set_continuous(self, channel, cont):
        if cont:
            template = ":INIT{ch}:CONT ON"
        else:
            template = ":INIT{ch}:CONT OFF"

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
        self.executor.execute_command("*TRG")

    def set_cs5(self, channel):
        sel_cal_kit = ":SENS{ch}:CORR:COLL:CKIT 30" # Last kit
        sel_cal_kit_name = ":SENS{ch}:CORR:COLL:CKIT:LABEL CS5" # Last kit

        set_velocity = ":SENS{ch}:CORR:RVEL:COAX 0.442"

        set_std1_label = ":SENS{ch}:CORR:COLL:CKIT:STAN1:LABEL CS5_OPEN"
        set_std1_type_open = ":SENS{ch}:CORR:COLL:CKIT:STAN1:TYPE OPEN"
        set_std1_c0 = ":SENS{ch}:CORR:COLL:CKIT:STAN1:C0 6.5e-15"
        set_std1_cls_port1 = ":SENS{ch}:CORR:COLL:CKIT:ORD:OPEN 1,1" # Assign standard 1 to port 1
        set_std1_cls_port2 = ":SENS{ch}:CORR:COLL:CKIT:ORD:OPEN 2,1" # Assign standard 1 to port 2


        set_std2_label = ":SENS{ch}:CORR:COLL:CKIT:STAN2:LABEL CS5_SHORT"
        set_std2_type_short = ":SENS{ch}:CORR:COLL:CKIT:STAN2:TYPE SHORT"
        set_std2_l0 = ":SENS{ch}:CORR:COLL:CKIT:STAN2:L0 5e-12"
        set_std2_cls_port1 = ":SENS{ch}:CORR:COLL:CKIT:ORD:SHORT 1,2" # Assign standard 2 to port 1
        set_std2_cls_port2 = ":SENS{ch}:CORR:COLL:CKIT:ORD:SHORT 2,2" # Assign standard 2 to port 2

        set_std3_label = ":SENS{ch}:CORR:COLL:CKIT:STAN3:LABEL CS5_LOAD"
        set_std3_type_load = ":SENS{ch}:CORR:COLL:CKIT:STAN3:TYPE LOAD"
        set_std3_delay = ":SENS{ch}:CORR:COLL:CKIT:STAN3:DELAY 0.0156e-12"
        set_std3_z0 = ":SENS{ch}:CORR:COLL:CKIT:STAN3:Z0 5"
        set_std3_cls_port1 = ":SENS{ch}:CORR:COLL:CKIT:ORD:LOAD 1,3" # Assign standard 3 to port 1
        set_std3_cls_port2 = ":SENS{ch}:CORR:COLL:CKIT:ORD:LOAD 2,3" # Assign standard 3 to port 2

        set_std4_label = ":SENS{ch}:CORR:COLL:CKIT:STAN4:LABEL CS5_THRU"
        set_std4_type_thru = ":SENS{ch}:CORR:COLL:CKIT:STAN4:TYPE THRU"
        set_std4_delay = ":SENS{ch}:CORR:COLL:CKIT:STAN4:DELAY 1.132e-12"
        set_std4_cls_port12 = ":SENS{ch}:CORR:COLL:CKIT:ORD:THRU 1,2,4" # Assign standard 4 to port 1 and 2
 

        commands = [sel_cal_kit, sel_cal_kit_name, set_velocity,
                    set_std1_label, set_std1_type_open, set_std1_c0, set_std1_cls_port1, set_std1_cls_port2, 
                    set_std2_label, set_std2_type_short, set_std2_l0, set_std2_cls_port1, set_std2_cls_port2,
                    set_std3_label, set_std3_type_load, set_std3_delay, set_std3_z0, set_std3_cls_port1, set_std3_cls_port2,
                    set_std4_label, set_std4_type_thru, set_std4_delay, set_std4_cls_port12]

        for command in commands[:]:
            command = command.format(ch=channel)
            self.executor.execute_command(command)

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

    def set_bus_trigger(self):
        self.executor.execute_command(":TRIG:SOUR BUS")

    def set_internal_trigger(self):
        self.executor.execute_command(":TRIG:SOUR INT")

    def set_immediate(self, channel):
        cmd = ":INIT{ch}:IMM"
        cmd = cmd.format(ch=channel)
        self.executor.execute_command(cmd)

    def set_four_channels(self):
        self.executor.execute_command(":DISP:SPL D12_34")

    def beep(self):
        self.executor.execute_command(":SYST:BEEP:COMP:IMM")

    def set_sweep_time(self, channel, time):
        no_auto = ":SENS{ch}:SWE:TIME:AUTO 0"
        cmd = ":SENS{ch}:SWE:TIME {time}"
        cmd = cmd.format(ch=channel, time=time)
        no_auto = no_auto.format(ch=channel)
        self.executor.execute_command(no_auto)
        self.executor.execute_command(cmd)

class VnaConfigError(Exception):
    pass
