#!/usr/bin/python

#sudo apt-get install python-twisted

#
# Example to perform a speedwire discovery using python
#
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.application.internet import MulticastServer

# Change this address to the address of your local network interface
localInterface = '192.168.2.3'

# Nothing to change below this line
spwMCastAdr='239.12.255.255'
spwPort = 9522

discoveryRequest = '534d4100000402a0ffffffff0000002000000000'
discoveryResponse ='534d4100000402a000000001000200000001'

class MulticastClientUDP(DatagramProtocol):
    def startProtocol (self):
        print "Joining speedwire multicast group."
        self.transport.joinGroup(spwMCastAdr)
        self.transport.setOutgoingInterface(localInterface)

        print "Sending discovery request."
        data = discoveryRequest.decode ('hex')
        self.transport.write(data, (spwMCastAdr, spwPort))

    def datagramReceived (self , datagram, (srcAddress , port)):
        data = datagram.encode('hex')
        if (data.startswith(discoveryResponse)):
            print "Found device: " + srcAddress

def stopReactor():
    print "Discovery finished."
    reactor.stop()

reactor.listenMulticast(spwPort , MulticastClientUDP(), listenMultiple=True)
reactor.callLater(10, stopReactor)
reactor.run()
