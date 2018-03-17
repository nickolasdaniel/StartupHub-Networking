import socket
import os
import struct
import sys 

class FTPClient(object):

    DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FILENAME = 'mata3'
    MAX_RECV_SIZE = 1024

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
        self.unpacker = struct.Struct("I")
        self.file_size = unpacker.unpack(self.client_socket.recv(self.unpacker.size))[0]
        if os.path.exists(FTPClient.DOWNLOAD_FOLDER):
            self.file_location = FTPClient.DOWNLOAD_FOLDER + filename
            with open(filename,'wb') as self.f:
                print("[*] File has been created...")
                self.recv_len = 0
                try:
                    while self.recv_len <= self.file_size:
                        self.data = self.client_server.recv(FTPClient.MAX_RECV_SIZE)
                        self.f.write(self.data)
                        self.recv_len += len(self.file_data)
                except IOError as ierr:
                    sys.exit(1)
                 print("File: {} Bytes: {} was succesfuly downloaded".format(filename, self.file_size))
         else:
            self.client_socket.send("Download location doesn`t exist!")
                    
            
        self.f.close()
        self.client_socket.close()

if __name__ == "__main__":
    ftp = FTPClient(("127.0.0.1", 8080))
    ftp.start_client()
