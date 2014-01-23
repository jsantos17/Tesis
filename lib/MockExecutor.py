from CommandExecutor import CommandExecutor

class MockExecutor(CommandExecutor):
    def __init__(self, ip, port=2049):
        pass

    def execute_command(self, command):
        print command
