from CommandExecutor import CommandExecutor

class MockExecutor(CommandExecutor):
    def __init__(self, ip, port=2049, expect_reply=False):
        pass

    def execute_command(self, command):
        print command
