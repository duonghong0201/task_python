class mess:

    def __init__(self):
        self.echo = None
        self.password = None
        self.username = None
        self.type = None

    def set_type_msg(self, type):
        self.type = type

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_echo(self, echo):
        self.echo = echo

    def create_msg(self, type, username, password):
        return self.set_type_msg(type), self.set_username(username), self.set_password(password)

    # return self.type, self.username, self.password

    def create_echo_msg(self, type, echo):
        return self.set_type_msg(type), self.set_echo(echo)

    def create_type_msg(self, type):
        return self.set_type_msg(type)

    def convert_dict(self):
        return self.__dict__


if __name__ == "__main__":
    Mess = mess()
    Mess.set_type_msg('2')
    print(Mess.convert_dict())
    Mess.set_username('hong')
    print(Mess.convert_dict())
    Mess.set_password('hong123')
    print(Mess.convert_dict())
    print(Mess.create_msg('1', 'hong', 'hong123'))
