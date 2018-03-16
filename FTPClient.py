import socket
import os
import struct

class FTPClient(object):

    BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FILENAME = 'mata3'

    def __init__(self, server_address):
        self.server_address = server_address
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_client(self):
        try:
            self.client_socket.connect(self.server_address)
            print("[*] Just connected at {}:{}".format(self.server_address[0], self.server_address[1]))
            self.download_file(FTPClient.FILENAME)
        except OSError:
            print("[*] Couldn`t connect.")

    def download_file(self, filename):
        with open(filename,'wb') as self.f:
            print("file opened...")
            while True:
                print("reciving data...")
                self.data = self.client_socket.recv(1024)
                self.file_size= os.path.getsize(self.data)
                self.unpacker=struct.Struct('I')
                self.unpacker_data=self.unpacker.unpack(self.file_size)[0]
                if not self.unpacker_data:
                    break
                self.f.write(self.unpacker_data)
        self.f.close()
        self.client_socket.close()

if __name__ == "__main__":
    ftp = FTPClient(("127.0.0.1", 8080))
    ftp.start_client()
