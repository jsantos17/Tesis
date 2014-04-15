from twisted.internet import reactor, protocol
import random
from time import sleep
import string

class Echo(protocol.Protocol):
    
    def dataReceived(self, data):
        """ Echo everything """
        sleep(1) # emulate slow server
        print data


def main():
    """This runs the protocol on port 1225"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(5025,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
