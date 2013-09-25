from CommandExecutor import CommandExecutor
import socket
import time

class SocketExecutor(CommandExecutor):
    def __init__(self, ip, port=1225):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip,port))

    def execute_command(self, command):
        self.s.send(command)
        time.sleep(1) # Wait before sending more commands. Should actually wait for ACK TODO


