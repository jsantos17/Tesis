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
        print command
        self.s.send(command + self.endline)
        time.sleep(1)
        if self.expect_reply:
            data = self.s.recv(8192)
            self.data = ''
            self.data = data

    def ask(self, command):
        print command
        self.s.send(command + self.endline)
        time.sleep(1)
        self.data = ""
        data = ""
        pdata = ""
        while True:
            pdata = self.s.recv(8192)
            if pdata[len(pdata)-1] == "\n": # Check if pdata includes LF at the end. Indicates end of transmission
                data += pdata
                break
            print "Receive length: {leng}".format(leng=len(pdata))
            data += pdata
        data = data[:-1] # For some reason there's a comma at the end of the transmission. Delete it
        self.data = data
        print data
        return self.data


    # Should be called after command execution
    def get_data(self):
        return self.data

    def close(self):
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()

