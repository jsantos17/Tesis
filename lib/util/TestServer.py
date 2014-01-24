from twisted.internet import reactor, protocol
import random
import string

class Echo(protocol.Protocol):
    
    def dataReceived(self, data):
        """ Echo everything """
        if data.replace("\0", "")  == ":CALC1:DATA:FDAT?":
            print "Sending data"
            self.transport.write(", ".join([str(1000*random.random()) for i in xrange(10000)]))
        elif data.replace("\0", "") == "SENS1:FREQ:DATA?":
            print "Sending data"
            self.transport.write(", ".join([str(1000*random.random()) for i in xrange(10000)]))
        else:
            print data


def main():
    """This runs the protocol on port 1225"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
