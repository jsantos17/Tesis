from SocketExecutor import SocketExecutor

class Vna:
    def __init__(self, ip, port):
        self.executor = SocketExecutor(ip, port)

    def activate_channel(self,channel):
        template = ":DISP:WIND{ch}:ACT"
        cmd = template.format(ch=channel)
        self.executor.execute_command(cmd)

    def activate_trace(self, channel, trace):
        template = ":CALC{ch}:PAR{tr}:SEL"
        cmd = template.format(ch=channel, tr=trace)
        self.executor.execute_command(cmd)
       
    def set_traces(self, trace):
        template = ":CALC{trace}:PAR:COUNT"
        cmd = template.format(trace=trace)
        self.executor.execute_command(cmd)

    def add_marker(self, channel, trace, marker):
        cmd = ":CALC{channel}:TRAC{trace}:MARK{marker}:ACT".format(
                channel=channel, trace=trace, marker=marker)
        self.executor.execute_command(cmd)

    def set_sparam_for_trace(self, sparam, trace)
        cmd = ":CALC{sparam}:PAR{trace}:DEF".format(sparam=sparam
                                                    trace=trace)
        self.executor.execute_command(cmd)

