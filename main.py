import asyncio
import uvloop

from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR


class MyServerUdpEchoProtocol:

    def connection_made(self, transport):
        print('start', transport)
        self.transport = transport

    def datagram_received(self, data, addr):
        print('Data received:', data, addr)
        self.transport.sendto(data, addr)

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print('stop', exc)


class MyClientUdpEchoProtocol:

    message = 'This is the message. It will be echoed.'

    def connection_made(self, transport):
        self.transport = transport
        print('sending "{}"'.format(self.message))
        self.transport.sendto(self.message.encode())
        print('waiting to receive')

    def datagram_received(self, data, addr):
        print('received "{}"'.format(data.decode()))
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print('closing transport', exc)
        loop = asyncio.get_event_loop()
        loop.stop()


def start_server(loop, addr):
    t = asyncio.Task(loop.create_datagram_endpoint(
                     MyServerUdpEchoProtocol, local_addr=addr))
    transport, server = loop.run_until_complete(t)
    return transport


def start_client(loop, addr):
    t = asyncio.Task(loop.create_datagram_endpoint(
                     MyClientUdpEchoProtocol, remote_addr=addr))
    loop.run_until_complete(t)


if __name__ == "__main__":
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        server = start_server(loop, ("0.0.0.0", 9999))
        start_client(loop, ("127.0.0.1", 9999))
        loop.run_forever()
    finally:
        if hasattr(loop, 'print_debug_info'):
            gc.collect()
            print(chr(27) + "[2J")
            loop.print_debug_info()

        loop.close()
