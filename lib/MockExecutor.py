from CommandExecutor import CommandExecutor
import visa

class MockExecutor(CommandExecutor):
    def __init__(self, ip, port=2049):
        pass

    def execute_command(self, command):
        print command
