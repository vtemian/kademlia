import asyncio

from .base import BaseServer


class KademliaUDPServer(BaseServer):
    def start(self, loop):
        address = ("0.0.0.0", self.node.node.port)
        task = asyncio.Task(loop.create_datagram_endpoint(
                            self.get_self_instance(), local_addr=address))
        transport, server = loop.run_until_complete(task)
        print("Staring sever")

    def get_self_instance(self):

        class DatagramWrapper(object):
            def __init__(me, *args, **kwargs):
                me = self
                print("mind blowing")

        return DatagramWrapper


    def receive(self):
        print("receive something")

    def store(self, job):
        print("store")

    def find_node(self, job):
        print("find_node")

    def find_value(self, job):
        print("store")
