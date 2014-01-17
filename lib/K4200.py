from MockExecutor import MockExecutor
from VisaExecutor import VisaExecutor
from SocketExecutor import SocketExecutor
import time

class K4200:
    
    def __init__(self, ip, port=2099):
        self.ip = ip
        self.executor = SocketExecutor(ip, port)
        self.configured = False
        self.has_measured = False
        self.smus = list()
    
    def attach(self, smu):
        self.smus.append(smu)

    def configure(self):
        for smu in self.smus:
            for command in smu.get_commands():
                self.executor.execute_command(command)
        self.configured = True

    def measure(self):
        self.executor.execute_command("MD ME1")
        self.has_measured = True

    def get_data(self, ch=1):
        if has_measured:
            template = "DO CH{ch}T"
            cmd = template.format(ch=ch)
            self.executor.execute_command(cmd)
            return executor.get_data()
        else:
            raise NoDataError("No data to retrieve")

class NotMeasuredYetError(Exception):
    pass
