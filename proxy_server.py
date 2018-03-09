import socket
import time

class ProxyServer(object):
    def __init__(self, server_address, server_address2):
        self.server_address = server_address
        self.server_address2 = server_address2

        self.socket_server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("[*] Binding server...")
        self.socket_server1.bind(self.server_address)
        print("[*] Server binded successfully.")

        print("[*] Server is now listening...")
        self.socket_server1.listen(5)

        self.client_socket, self.client_addr = self.socket_server1.accept()

        self.socket_server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server2.connect(server_address2)
        print("[*] Client has just connected.")

        while True:
            self.handle(self.socket_server2, self.client_socket)

    def handle(self, socket_server2, client_socket):
        self.MAX_RECV_BUFF = 1024
        self.socket_server2 = socket_server2
        self.client_socket = client_socket

        try:
            self.data = self.client_socket.recvall(self.client_socket)
            print("[*] Received data from client: {}".format(self.data))

            if not self.data:
                print("[*] Client just disconnected.")
                self.socket_server2.close()
                self.client_socket.close()

            print("[*] Sending data to the server...")
            self.socket_server2.send(self.data)
            print("[*] Data has been sent.")
        except socket.error as serr:
            print(serr)

        try:
            self.data2 = self.socket_server2.recv(self.MAX_RECV_BUFF)
            print("[*] Received data back from the server.")

            if not self.data2:
                print("[*] Server stopped working")
                self.client_socket.close()
                self.socket_server2.close()

            print("[*] Sending data to client...")
            self.client_socket.send(self.data2)
            print("[*] Data has been sent.")
        except socket.error as serr:
            print(serr)


    # def recvall(self, client_socket, MAX_RECV_BUFF=1024):
    #     self.client_socket = client_socket
    #
    #     self.MAX_RECV_BUFF = MAX_RECV_BUFF
    #
    #     self.total_data = []
    #     self.data = ""
    #
    #     while 1:
    #         self.data = client_socket.recv(self.MAX_RECV_BUFF)
    #         self.total_data.append(self.data)
    #         if len(self.data) < self.MAX_RECV_BUFF:
    #             break
    #     return self.total_data


if __name__ == "__main__":
    ProxyServer(("127.0.0.1", 8081),("127.0.0.1",8089))
