from MockExecutor import MockExecutor


class K4200:
    
    def __init__(self, ip, port=2099):
        self.ip = ip
        self.executor = MockExecutor(ip, port)
        self.configured = False
        self.smus = list()
    
    def attach(self, smu):
        self.smus.append(smu)

    def configure(self):
        for smu in self.smus:
            for command in smu.get_commands():
                self.executor.execute_command(command)
        self.configured = True

    def measure(self):
#       TODO implement measure commands
        pass


