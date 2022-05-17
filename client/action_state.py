from abc import ABC, abstractmethod


class Action_State(ABC):

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def echo(self):
        pass

    @abstractmethod
    def broadcast(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def wake(self):
        pass

    @abstractmethod
    def logout(self):
        pass
