import socket

class Proxy_Server(object):
    def __init__(self,server_address,server_address2):
        self.server_address=server_address
        self.server_address2=server_address2

        self.socket_server1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.socket_server1.bind(server_address)
        except socket.error as err:
            print(str(err))
        self.socket_server1.listen(5)

        self.client_server,self.clent_addr=self.socket_server1.accept()


        self.socket_server2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_server2.connect(server_address2)

        while True:
            try:
                self.handle(self.socket_server2,self.client_server)
            except KeyboardInterrupt:
                print("erroare fam")

    def handle(self,socket_server2,client_server):
        self.MAX_RECV_BUFFER=1024
        self.data=client_server.recv(self.MAX_RECV_BUFFER)

        if not self.data:
            print("client just disconected")
            self.client_server.close()
            self.socket_server2.close()

        socket_server2.send(self.data)
        print("data send {}".format(self.data))

        try:
            self.data2=socket_server2.recv(self.MAX_RECV_BUFFER)

            if not self.data2:

                print("server stopped working")
                client_server.close()
                socket_server2.close()

            client_server.send(self.data2)
            print("data to {}".format(self.data2))

        except socket.error as serr:
            print(str(serr))

if __name__=="__main__":
    Proxy_Server(("127.0.1.1",8081),("127.0.0.1",8089))
