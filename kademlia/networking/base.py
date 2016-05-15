from abc import ABCMeta, abstractmethod

from kademlia.node import Node

VALID_JOBS_TYPES = ["store", "find_node", "find_value", "ping"]


class Base(metaclass=ABCMeta):
    def __init__(self, node):
        self.kademlia = node

    @abstractmethod
    def start(self, *args, **kwargs):
        pass

class BaseClient(Base):
    def __init__(self, *args, **kwargs):
        super(BaseClient, self).__init__(*args, **kwargs)

        self.start()

    @abstractmethod
    def send(self, node, data):
        pass

    def pong(self, node, loop=None):
        data = {
            "type": "pong",
            "data": "",
            "sender": {
                "id": self.kademlia.node.id,
                "port": self.kademlia.node.id,
                "host": self.kademlia.node.id,
            }

        }
        self.send(node, data, loop)

    def ping(self, node, loop=None):
        data = {
            "type": "ping",
            "data": "",
            "sender": {
                "id": self.kademlia.node.id,
                "port": self.kademlia.node.id,
                "host": self.kademlia.node.id,
            }
        }
        self.send(node, data, loop)


class BaseServer(Base):

    @abstractmethod
    def receive(self):
        pass

    def handle_receive(self, job):
        """
            Handle different types of jobs (messsages comming from other nodes).
        """

        on_job = getattr(self, "on_%s" % job["type"], None)
        if on_job is not None and callable(on_job):
            self.kademlia.received_jobs.append(job)
            return on_job(job)

        raise ValueError("Invalid job type %s. Not in %s" %
                         (job["type"], ",".join(VALID_JOBS_TYPES)))

    @abstractmethod
    def on_store(self, job):
        pass

    @abstractmethod
    def on_find_node(self, job):
        pass

    @abstractmethod
    def on_find_value(self, job):
        pass

    def on_ping(self, job):
        """
            On ping method, the client should respond with a pong message.
        """

        node = Node(job["sender"]["host"], job["sender"]["port"],
                    job["sender"]["id"])
        self.kademlia.pong(node)
