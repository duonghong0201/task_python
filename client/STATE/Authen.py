from abc import ABC

from client.action_state import Action_State

class Authen(Action_State, ABC):

    def register(self):
        print("Into Idle")
        return True

    def logout(self):
        print(" Into Idle")
        return True

    def echo(self):
        print("In authen")
        return True

    def broadcast(self):
        print("In authen")
        return True

    def sleep(self):
        print("Into Sleep")
        return True

    def wake(self):
        print("no access")
        return False

    def login(self):
        print("no access")
        return False



