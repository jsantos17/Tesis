from Vna import Vna
from SocketExecutor import SocketExecutor
from lib.util.VnaEnums import SweepType
from lib.util.VnaEnums import SParameters 

class VnaChannel(Vna):
    """ Wrapper for Vna class that specifies a fixed channel """
    def __init__(self, ip, port, channel):
        super(VnaChannel, self).__init__(ip, port)
        self.channel = channel

    def set_continuous(self):
        super(VnaChannel, self).set_continuous(self.channel)

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

    def add_marker(self, channel, trace, marker):
        super(VnaChannel, self).add_marker(self.channel, trace, marker)

    def set_sparam(self, trace, sparam):
        super(VnaChannel, self).set_sparam(self.channel, trace, sparam)

    def set_points(self, points):
        super(VnaChannel, self).set_points(self.channel, points)
