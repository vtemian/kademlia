from .base import BaseClient


class KademliaUDPClient(BaseClient):
    def start(self):
        print("Staring sever")

    def __call__(self):
        return lambda x,y: print(x,y)
