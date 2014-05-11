from Vna import Vna
from SocketExecutor import SocketExecutor
from lib.util.VnaEnums import SweepType
from lib.util.VnaEnums import SParameters 

class VnaChannel(Vna):
    """ Wrapper for Vna class that specifies a fixed channel """
    def __init__(self, ip, port, channel):
        super(VnaChannel, self).__init__(ip, port)
        self.channel = channel

    def set_continuous(self, cont):
        super(VnaChannel, self).set_continuous(self.channel, cont)

    def is_ready(self):
        return super(VnaChannel, self).is_ready()

    def set_sweep_type(self, sweep_type):
        super(VnaChannel, self).set_sweep_type(self.channel, sweep_type)

    def set_center_span(self, center, span):
        super(VnaChannel, self).set_center_span(self.channel, center, span)

    def set_start_stop(self, start, stop):
        super(VnaChannel, self).set_start_stop(self.channel, start, stop)

    def activate_channel(self):
        super(VnaChannel, self).activate_channel(self.channel)

    def activate_trace(self, trace):
        super(VnaChannel, self).activate_trace(self.channel, trace)
       
    def set_traces(self, trace):
        super(VnaChannel, self).set_traces(self.channel, trace)

    def add_marker(self, marker, trace=1):
        super(VnaChannel, self).add_marker(self.channel, trace, marker)

    def set_x(self, new_x, mark=1):
        super(VnaChannel, self).set_x(self.channel, new_x, mark)

    def get_start_x(self):
        return super(VnaChannel, self).get_start_x(self.channel)

    def get_stop_x(self):
        return super(VnaChannel, self).get_stop_x(self.channel)

    def get_x(self, mark=1):
        return super(VnaChannel, self).get_x(self.channel, mark)

    def get_y(self, mark=1):
        return super(VnaChannel, self).get_y(self.channel, mark)

    def set_sparam(self, trace, sparam):
        super(VnaChannel, self).set_sparam(self.channel, trace, sparam)

    def set_points(self, points):
        super(VnaChannel, self).set_points(self.channel, points)

    def auto_scale(self):
        super(VnaChannel, self).auto_scale(self.channel)

    def set_format(self, fmt):
        super(VnaChannel, self).set_format(self.channel, fmt)

    def set_cal_kit(self, kit):
        super(VnaChannel, self).set_cal_kit(self.channel, kit)

    def set_cal_type(self, cal_type, port=None):
        super(VnaChannel, self).set_cal_type(self.channel, cal_type, port)

    def cal_measure_open(self, port):
        super(VnaChannel, self).cal_measure_open(self.channel, port)

    def cal_measure_short(self, port):
        super(VnaChannel, self).cal_measure_short(self.channel, port)

    def cal_measure_load(self, port):
        super(VnaChannel, self).cal_measure_load(self.channel, port)

    def cal_measure_thru(self, port_x, port_y):
        super(VnaChannel, self).cal_measure_thru(self.channel, port_x, port_y)

    def cal_measure_isol(self, port_x, port_y):
        super(VnaChannel, self).cal_measure_isol(self.channel, port_x, port_y)

    def trl_thru_line(self, port_x, port_y):
        super(VnaChannel, self).trl_thru_line(self.channel, port_x, port_y)

    def trl_reflect(self, port):
        super(VnaChannel, self).trl_reflect(self.channel, port)

    def trl_line_match(self, port_x, port_y):
        super(VnaChannel, self).trl_line_match(self.channel, port_x, port_y)
    
    def save_cal(self):
        super(VnaChannel, self).save_cal(self.channel)

    def set_cs5(self):
        super(VnaChannel, self).set_cs5(self.channel)

    def set_immediate(self):
        super(VnaChannel, self).set_immediate(self.channel)
    
    def set_sweep_time(self, time)
        super(VnaChannel, self).set_sweep_time(self.channel, time)

