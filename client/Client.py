from message import mess
import re
import pickle
import time
import socket

global socket_client


class client:
    @staticmethod
    def check_password(password):
        pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=]).*$"
        if re.findall(pattern, password):
            return True
        else:
            return False

    @staticmethod
    def connect_socket():
        global socket_client
        host_ip = socket.gethostname()
        port = 5678
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect((host_ip, port))

    def send_msg(self, mess_dict):
        while True:
            try:
                self.connect_socket()
                msg = pickle.dumps(mess_dict)
                msg = bytes(f"{len(msg):<{10}}", 'utf-8') + msg
                socket_client.send(msg)
            except Exception as err:
                print(err)

    def user_choice(self):
        print("""
                 1: Register
                 2: Login
                 3: Echo
                 4: Exit""")
        choice = input("Your select is: ")
        time.sleep(1)
        if choice == '1':
            print("____Register____")
            try:
                username = input("Enter username: ")
                while True:
                    password = input("Enter password: ")
                    if self.check_password(password):
                        break
                    else:
                        print("wrong password")
                        continue
                mess.create_msg(choice, username, password)
                mess_dict = mess.convert_dict()
                mess.send_msg(mess_dict)
            except Exception as err:
                print(err)
        elif choice == '2':
            while True:
                print("____Login____")
                username = input("Enter username: ")
                password = input("\n Enter password: ")
                mess.create_msg(choice, username, password)
                mess_dict = mess.convert_dict()
                self.send_msg(mess_dict)
        elif choice == '3':
            while True:
                print("____Echo____")
                echo = input("Echo: ")
                self.create_echo_msg(choice, echo)
                msg_dict = mess.convert_dict()
                self.send_msg(msg_dict)
        else:
            print("Exit")
            exit()

    def create_echo_msg(self, choice, echo):
        pass


if __name__ == "__main__":
    Client = client()
    # Client.send_msg('hong')
    Client.user_choice()
