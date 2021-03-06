from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from atmo_soa.skywalker import Skywalker

from skywalker.handler import Handler

if __name__ == "__main__":
    port = 8000

    handler = Handler()

    processor = Skywalker.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "Starting python server..."
    server.serve()
    print "done!"
