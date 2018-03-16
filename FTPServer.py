import socket
import struct
import os

class FTPServer(object):

    BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FILENAME = "mata"
    MAX_RECV_SIZE = 1024

    def __init__(self, server_addr=None, backLog=10, setBlocking=False, reuseAddr=True, port = 8080):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if server_addr is None:
            self.server_address = ("127.0.0.1",port)
        else:
            self.server_address = socket.gethostbyname(socket.gethostname())

        try:
            self.server_socket.bind(self.server_address)
            print("[*] Server has bined to address {}:{}.".format(self.server_address[0], self.server_address[1]))
        except socket.error:
            print("[*] Couldn`t bind the server.")

        if setBlocking:
            self.server_socket.setblocking(0)

        if reuseAddr:
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket.listen(backLog)
        self.active_server = True
        print("[*] Server is now listening...")

    def start_server(self):

        try:
            while self.active_server:
                self.client_socket, self.client_address = self.server_socket.accept()
                print("[*] Client just connected.")
                self.handle(self.client_socket)

        except KeyboardInterrupt:
            self.shutdown_server()

    def handle(self, client_socket):
        self.file_location = FTPServer.BASE_FOLDER + "/" + FTPServer.FILENAME
        self.client_socket = client_socket
        try:
            self.data = self.client_socket.recv(FTPServer.MAX_RECV_SIZE)

            if not self.data:
                print("[*] Client is closing...")
                self.client_socket.close()
                self.shutdown_server()
            else:

                print("[*] Received data.")
                self.send_file(self.file_location ,self.client_socket)
                print("[*] Data has been sent.")

        except IOError:
            print("[*] Error")

    def shutdown_server(self):
        print("[*] Server is closing...")
        self.active_server = False
        self.server_socket.close()

    def send_file(self, file_location, client_socket):

        self.file_location = file_location
        self.client_socket = client_socket

        with open(self.file_location, 'rb') as self.f:
            self.data1=self.f.read(1024)

            self.file_size = os.path.getsize(self.data1)
            self.packer = struct.Struct('I')
            self.packet_data = self.packer.pack(self.file_size)

            while self.packet_data:

                try:
                    client_socket.send(str(self.packet_data))
                except IOError:

                    print("cant send...")
                self.packet_data=self.f.read(1024)
            self.f.close()





if __name__ == "__main__":
    ftp = FTPServer()
    ftp.start_server()
