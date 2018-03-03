import socket

class ProxyServer(object):

    def __init__(self,server_address,MSG):
        self.MSG=MSG
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_address=server_address

        self.binder(socket_server,server_address)

        self.connecter(socket_server,server_address)
    def binder(self,socket_server,server_address):
        try:
            socket_server.bind(server_address)
        except socket_server.error as errr:
            print(str(errr))

        self.setsock(socket_server)

        socket_server.listen(5)

        print("Now is listening {}:{}".format(server_address[0],server_address[1]))

        try:
            self.handle_server(socket_server)
        except KeyboardInterrupt as kerr:
            print("server is closing...")
            socket_server.close()

    def setsock(self,socket_server):
        socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
        if hasattr(socket,"SO_REUSEPORT"):
            socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)

    def handle_server(self,socket_server):
        self.MAX_RECV_BUFFER=1024
        while True:
            self.client_server, self.client_address = socket_server.accept()

            self.recv_size=1
            while self.recv_size:
                self.data=self.client_server.recv(self.MAX_RECV_BUFFER)
                self.msg=self.data

                if not self.data:
                    print("client just disconected")
                    break
                self.recv_size=len(self.data)

                self.client_server.send(self.MSG)

                self.data=""
                return self.msg

    def connecter(self,server_address,socket_server):

        socket_server.connect(server_address)

        try:
            while True:
                self.handle_client(socket_server)
        except KeyboardInterrupt:
            print("you left this server...MUIE")
            socket_server.close()
    def handle_client(self,socket_server):
        self.MAX_BUFFER=1024

        self.data=socket_server.recv(self.MAX_BUFFER)



















if __name__=="__main__":
