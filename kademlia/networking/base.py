from abc import ABCMeta, abstractmethod

VALID_JOBS_TYPES = ["store", "find_node", "find_value", "ping"]


class Base(metaclass=ABCMeta):
    def __init__(self, node):
        self.node = node

    @abstractmethod
    def start(self, *args, **kwargs):
        pass


class BaseClient(Base):

    @abstractmethod
    def send(self, node, data):
        pass

    def pong(self, node):
        data = {
            "job_type": "pong",
            "data": "",
            "sender": self.node.id
        }
        self.send(node, data)

    def ping(self, node):
        data = {
            "job_type": "ping",
            "data": "",
            "sender": self.node.id
        }
        self.send(node, data)


class BaseServer(Base):

    @abstractmethod
    def receive(self):
        pass

    def handle_receive(self, job):
        """
            Handle different types of jobs (messsages comming from other nodes).
        """

        if job["type"] in self.__dict__ and callable(self.__dict__[job["type"]]):
            self.node.receive_jobs.append(job)
            return self.__dict__[job["job_type"]](job["data"])

        raise ValueError("Invalid job type %s. Not in %s" %
                         (job["type"], ",".join(VALID_JOBS_TYPES)))

    @abstractmethod
    def store(self, job):
        pass

    @abstractmethod
    def find_node(self, job):
        pass

    @abstractmethod
    def find_value(self, job):
        pass

    def ping(self, job):
        """
            On ping method, the client should respond with a pong message.
        """

        node = Node(job["host"], job["port"], job["node_id"])
        self.node.client.pong(node)
