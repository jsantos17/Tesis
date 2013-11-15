from SMU import SMU
from visa import instrument


class K4200:
    
    def __init__(self, ip, port):
        self.ip = ip
        self.k4200 = instrument("TCPIP::{ip}::{port}::SOCKET".
                            format(ip=self.ip, port=self.port))
        self.smus = list()
    
    def attach(self, smu):
        self.smus.append(smu)

    def measure(self):
        for commands in smus:
            for command in smus.get_commands():
                k4200.write(command)

    def __str__(self):
        pass
        

