import socket
import os
import struct

class FTPClient(object):

    BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
    DEST_FOLDER = BASE_FOLDER + "/" + "testfolder"
    MAX_SEND_SIZE = 1024
    MAX_RECV_SIZE = 1024
    FILENAME = "test"

    def __init__(self, server_address):
        self.server_address = server_address
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_client(self):
        try:
            self.client_socket.connect(self.server_address)
            print("[*] Just connected at {}:{}".format(self.server_address[0], self.server_address[1]))
        except OSError:
            print("[*] Couldn`t connect.")
            self.send_file_request()
            self.download_file("test")

    def send_file_request(self):
        try:
            self.client_socket.sendall(FTPClient.DEST_FOLDER + FTPClient.FILENAME)
            print("[*] Request has been sent.")
        except OSError:
            print("[*] Couldn`t send request")


    def recv_all(self):

        self.total_data=""
        self.data=""

        self.recv_size=1

        while self.recv_size:
            self.data = self.client_socket.recv(FTPClient.MAX_RECV_SIZE)
            if not len(self.data):
                break
            else:
                self.total_data += self.data
            self.recv_size=len(self.data)
            self.data=""
        return self.total_data

    def download_file(self, filename):


if __name__ == "__main__":
    ftp = FTPClient(("127.0.0.1", 8080))
    ftp.start_client()
