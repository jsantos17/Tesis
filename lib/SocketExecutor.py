from CommandExecutor import CommandExecutor
import socket
import time

class SocketExecutor(CommandExecutor):
    def __init__(self, ip, port=1225, expect_reply=True, endline="\0"):
        self.port = port
        self.ip = ip
        self.endline = endline
        print "Port: %s" % self.port
        print "IP: %s" % self.ip
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip,port))
        self.data = None
        self.expect_reply = expect_reply

    def execute_command(self, command):
        self.s.send(command + self.endline)
        if self.expect_reply:
            data = self.s.recv(8192)
            self.data = ''
            self.data = data

    def ask(self, command):
        self.s.send(command + self.endline)
        self.data = ""
        data = ""
        pdata = ""
        while True:
            pdata = self.s.recv(8192)
            if pdata[len(pdata)-1] == "\n" or pdata[len(pdata)-1] == "\0": # Check if pdata includes LF at the end. Indicates end of transmission
                data += pdata
                break
            data += pdata
        data = data[:-1] # For some reason there's a comma at the end of the transmission. Delete it
        self.data = data
        return self.data


    # Should be called after command execution
    def get_data(self):
        return self.data

    def close(self):
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()

