import socket
import select
import sys
import logging
from configparser import ConfigParser
from queue import Queue

class Server(object):
    def __init__(self,setBlocking=False,port=8080,resueAddr=True,server_addr=None,backLog=10):
        self.port=port
        self.socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        if server_addr is None:
            self.server_address=("127.0.0.1",port)
        else:
            self.server_address=socket.gethostbyname(socket.gethostname())

        try:
            self.socket_server.bind(self.server_address)
            print("server successfully binded at {}:{}".format(self.server_address[0],self.server_address[1]))
        except socket.error:
            print("couldn't bind this server...")

        if setBlocking:
            self.socket_server.setblocking(0)

        if resueAddr:
            self.socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        self.socket_server.listen(10)

        self.inputs=[self.socket_server]
        self.outputs=[]

    def start_server(self):

        self.server_status=True

        while self.server_status:

            readable,writeable,exceptional=select.select(self.inputs,self.outputs,self.inputs)

            for sock in readable:
                if sock==self.socket_server:

                    self.socket_client,self.socket_addr=self.socket_server.accept()
                    self.inputs.append(self.socket_client)
                    print("client just connected {}:{}".format(self.socket_client[0],self.socket_client[1]))
                    self.handle(self.socket_client)
                else:


    def handle(self,socket_client):
        MAX_RECV_BUFFER=1024
        try:
            self.data=socket_client.recv(MAX_RECV_BUFFER)
        except socket.error:

            if socket_client in self.inputs:

                self.inputs.remove(socket_client)
                self.shut_down()

            elif not self.data:
                self.shut_down()

    def shut_down(self):
        self.socket_server.close()



'''
        for socket in self.inputs:
            if socket!=socket_server and socket!=sock:
                try:
                    socket.send(message)
                except:
                    socket.close()

                    if socket in self.inputs:
                        self.inputs.remove(message)
'''
