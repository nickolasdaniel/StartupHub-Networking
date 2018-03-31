import socket
import configparser

class Client(object):

    MAX_RECV_BUFFER = 1024

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read("client_config.ini")

    def connect(self):
        self.server_address = self.config_parser.get("resources", "host"), int(self.config_parser.get("resources", "port"))
        self.client_socket.connect(self.server_address)
        print("Client just connected at: {}:{}".format(self.server_address[0], self.server_address[1]))

    def send_message(self):
        while 1:
            message = input('Send a message to the server: ')
            try:
                self.client_socket.sendall(message.encode('utf-8'))
                response = self.client_socket.recv(Client.MAX_RECV_BUFFER)
                print("Received message from server: {}".format(response.decode('utf-8')))
            except:
                print("Server is closed.")
                self.client_socket.close()
                break




if __name__ == "__main__":
    client = Client()
    client.connect()
    client.send_message()