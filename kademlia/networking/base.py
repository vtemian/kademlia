from abc import ABCMeta, abstractmethod

VALID_JOBS_TYPES = ["store", "find_node", "find_value", "ping"]


class Base(metaclass=ABCMeta):
    def __init__(self, node):
        self.node = node

    @abstractmethod
    def start(self):
        raise NotImplemented("start method needs to be implemented on BaseClient")


class BaseClient(Base):
    @abstractmethod
    def send(self):
        raise NotImplemented("send method needs to be implemented on BaseClient")


class BaseServer(Base):

    @abstractmethod
    def receive(self):
        raise NotImplemented("receive method needs to be implemented on BaseClient")

    def handle_receive(self, job):
        """
            Handle different types of jobs (messsages comming from other nodes).
        """

        if job["type"] in self.__dict__ and callable(self.__dict__[job["type"]]):
            return self.__dict__[job["job_type"]](job["data"])

        raise ValueError("Invalid job type %s. Not in %s" %
                         (job["type"], ",".join(VALID_JOBS_TYPES)))

    @abstractmethod
    def store(self, job):
        raise NotImplemented("store method needs to be implemented on BaseServer")

    @abstractmethod
    def find_node(self, job):
        raise NotImplemented("find_node method needs to be implemented on BaseServer")

    @abstractmethod
    def find_value(self, job):
        raise NotImplemented("find_value method needs to be implemented on BaseServer")

    @abstractmethod
    def ping(self, job):
        raise NotImplemented("ping method needs to be implemented on BaseServer")
