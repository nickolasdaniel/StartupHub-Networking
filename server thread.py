import threading
import socket
import configparser

class Thread(threading.Thread):

    MAX_RECV_BUFFER = 1024

    def __init__(self, client_socket, client_address):
        super(Thread, self).__init__()

        self.client_socket = client_socket
        self.client_address = client_address



    def run(self):
        data = ''

        while 1:
            message = self.client_socket.recv(Thread.MAX_RECV_BUFFER)
            if not message:
                print("There`s no message.")
            data += message.decode('utf-8')
            print("{}:{} => {}".format(self.client_address[0], self.client_address[1], data))
            response = input("Send back to the client: ")
            self.client_socket.sendall(response.encode("utf-8"))
            data = ''


class Server(object):

    BACKLOG = 2

    def __init__(self):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read("config.ini")

        self.server_addr = self.config_parser.get("resources", "host"), int(self.config_parser.get("resources", "port"))

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server_socket.bind(self.server_addr)
            print("Server has binded to address: {}:{}".format(self.server_addr[0], self.server_addr[1]))
        except IOError as e:
            print("Couldn`t bind to address, error: {}".format(e))

        self.server_socket.listen(Server.BACKLOG)
        self.server_active = True



    def start_server(self):
        while self.server_active:
            try:
                self.handle()
            except KeyboardInterrupt:
                self.shutdown_server()



    def handle(self):
        server_addresses=[]
        self.client_socket, self.client_address = self.server_socket.accept()
        print("Client just connected with address: {}:{}".format(self.client_address[0], self.client_address[1]))
        server_addresses.append((self.client_socket, self.client_address))
        for address in server_addresses:
            client_handler = Thread(address[0], address[1])
            client_handler.start()

    def shutdown_server(self):
        print("Server is closing...")
        self.server_active = False
        self.server_socket.close()
        self.client_socket.close()


if __name__ == '__main__':
    server = Server()
    server.start_server()