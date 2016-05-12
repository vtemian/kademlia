import hashlib
from random import randint


class Node(object):
    MAX_ID_BITS = 128

    @staticmethod
    def hash_it(value):
        return hashlib.sha1(value.encode()).hexdigest()

    @staticmethod
    def generate_id():
        return randint(0, 2 ** Node.MAX_ID_BITS)

    def __init__(self, host, port, bucket, node_id=None):
        self.host = host
        self.port = port
        self.node_id = node_id or Node.generate_id()
        self.bucket = bucket

    def __xor__(self, node):
        return self.node_id ^ node.node_id

    def address(self):
        return (self.host, self.port)
