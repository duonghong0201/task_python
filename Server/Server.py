from Database.database import check_login, check_register, insert_new_account
import pickle
import threading
import socket
class Server:
    def connect_socket(self):
        HOST = '127.0.0.1'
        PORT = 5678
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)

    def receive_msg(self):
        self.connect_socket()
        while True:
            client, addr = s.accept()
            try:
                print("Connected by ",addr)
                while True:
                    data = client.recv(1024)
                    str_data = data.decode("utf8")
            finally:
                client.close()

    @staticmethod
    def register(client,username, password):
        if check_register(username):
            return client.send(bytes("Register Fail", 'utf-8'))
        else:
            insert_new_account(username, password)
            return client.send(bytes("Register successful", 'utf-8'))

    @staticmethod
    def login(client, username, password):
        if check_login(username, password):
            return client.send(bytes("Login successful", 'utf-8'))
        else:
            return client.send(bytes("Login fail", 'utf-8'))

    @staticmethod
    def echo(client, message):
        string = ''.join(char for char in message if char.isalnum())
        client.send(bytes(string, 'utf-8'))
if __name__ == "__main__":
    server = Server()
    server.receive_msg()
