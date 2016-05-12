from .base import BaseClient


class KademliaUDPServer(BaseClient):
    def start(self):
        print("Staring sever")

    def __call__(self):
        return lambda x,y: print(x,y)
