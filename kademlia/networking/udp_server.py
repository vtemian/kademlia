import json
import time
import asyncio
import threading

import uvloop

from .base import BaseServer


class KademliaUDPServer(BaseServer):
    def start(self):
        loop = uvloop.new_event_loop()

        def starting_new_thread():
            asyncio.set_event_loop(loop)

            try:
                address = ("0.0.0.0", self.kademlia.node.port)
                task = asyncio.Task(loop.create_datagram_endpoint(
                                    self.get_self_instance(),
                                    local_addr=address))
                loop.run_until_complete(task)
                loop.run_forever()
            finally:
                loop.close()

        threading.Thread(target=starting_new_thread).start()
        time.sleep(1)

    def get_self_instance(self):
        class DatagramWrapper(object):
            def __new__(me, *args, **kwargs):
                return self
        return DatagramWrapper

    def receive(self):
        print("receive something")

    def on_store(self, job):
        print("store")

    def on_find_node(self, job):
        print("find_node")

    def on_find_value(self, job):
        print("store")

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        job = json.loads(data.decode())
        job["sender_address"] = addr
        self.handle_receive(job)

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print('stop', exc)
