from abc import ABCMeta, abstractmethod


class BaseClient(metaclass=ABCMeta):
    def __init__(self, node):
        self.node = node

    @abstractmethod
    def start(self):
        raise NotImplemented("start method needs to be implemented on BaseClient")

    @abstractmethod
    def __call__(self):
        raise NotImplemented("__call__ method needs to be implemented on BaseClient")
