from CommandExecutor import CommandExecutor
import socket
import time

class SocketExecutor(CommandExecutor):
    def __init__(self, ip, port=1225, expect_reply=True):
        self.port = port
        self.ip = ip
        print "Port: %s" % self.port
        print "IP: %s" % self.ip
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip,port))
        self.data = None
        self.expect_reply = expect_reply

    def execute_command(self, command):
        self.s.send(command + "\0")
        time.sleep(0.5)
        if self.expect_reply:
            data = self.s.recv(8192)
            self.data = ''
            self.data = data

    def ask(self, command):
        self.s.send(command + "\0")
        time.sleep(0.5)
        data = self.s.recv(8192)
        self.data = ''
        self.data = data


    # Should be called after command execution
    def get_data(self):
        return self.data

    def close(self):
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()

