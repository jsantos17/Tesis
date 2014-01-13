from twisted.internet import reactor, protocol
import random
import string

class Echo(protocol.Protocol):
    
    def dataReceived(self, data):
        """ Reply with ACK to anything """
        print data
        if random.randint(0,10) > 5:
            wt = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20))
            self.transport.write(wt)
        else:
            self.transport.write("ACK\n\0")


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
