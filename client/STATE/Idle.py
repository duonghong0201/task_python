from client.action_state import Action_State


class Idle(Action_State):

    def register(self):
        print("In state Idle")
        return True

    def login(self):
        print("Into state Authen")
        return True

    def logout(self):
        print("no access")
        return False

    def echo(self):
        print("no access")
        return False

    def broadcast(self):
        print("no access")
        return False

    def wake(self):
        print("no access")
        return False

    def sleep(self):
        print("no access")
        return False