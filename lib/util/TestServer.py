from twisted.internet import reactor, protocol
import random
import string

class Echo(protocol.Protocol):
    
    def dataReceived(self, data):
        """ Echo everything """
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
