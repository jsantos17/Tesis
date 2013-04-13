from SMU import SMU
from visa import instrument


class K4200:
    
    def __init__(self, ip)
        self.ip = ip
        self.k4200 = instrument("TCPIP::{ip}::INSTR".
                            format(ip=ip))
        self.smus = list()
    
    def attach(smu):
        self.smus.append(smu)

    def __str__(self):
        pass
        

