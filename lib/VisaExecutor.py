from CommandExecutor import CommandExecutor
import visa

class VisaExecutor(CommandExecutor):
    def __init__(self, ip, port=1225):
        self.ip = ip
        self.device = visa.instrument("TCPIP::{ip}::{port}::SOCKET".format(ip=ip, port=port))

    def execute_command(self, command):
        self.device.write(command)
