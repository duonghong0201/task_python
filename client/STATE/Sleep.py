from abc import ABC

from client.action_state import Action_State


class Sleep(Action_State, ABC):

    def wake(self):
        print("Into authen")
        return True

    def register(self):
        print("no access")
        return False

    def login(self):
        print("no access")
        return False

    def logout(self):
        print("no access")
        return False

    def echo(self):
        print("no access")
        return False

    def broadcast(self):
        print("no access")
        return False

    def sleep(self):
        print("In Sleep")
        return True
