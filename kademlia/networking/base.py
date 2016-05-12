from abc import ABCMeta, abstractmethod


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

    def handle_receive(self, data):
        if data["type"] == "store":
            self.store(data["job_description"])
        elif data["type"] == "":
            pass

    @abstractmethod
    def store(self, job):
        raise NotImplemented("store method needs to be implemented on BaseServer")

