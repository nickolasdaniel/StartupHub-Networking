import socket

class Proxy_Server(object):
    def __init__(self,server_address,server_address2):
        self.server_address=server_address
        self.server_address2=server_address2

        self.socket_server1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            print("[*] Server is trying to bind...")
            self.socket_server1.bind(server_address)
            print("[*] Server has successfuly binded.")
        except socket.error as err:
            print(str(err))
        self.socket_server1.listen(5)
        print("[*] Servere is now listening...")

        self.client_server,self.clent_addr=self.socket_server1.accept()


        self.socket_server2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("[*] Server is trying to connect...")
        self.socket_server2.connect(server_address2)
        print("[*] Server has connected to {}".format(server_address2))

        while True:
            try:
                self.handle(self.socket_server2,self.client_server)
            except KeyboardInterrupt:
                print("Server is disconnecting.")

    def handle(self,socket_server2,client_server):
        self.MAX_RECV_BUFFER=1024
        self.data=client_server.recv(self.MAX_RECV_BUFFER)

        if not self.data:
            print("Client just disconected.")
            self.client_server.close()
            self.socket_server2.close()

        socket_server2.send(self.data)
        print("Data {} is sending...".format(self.data))

        try:
            self.data2=socket_server2.recv(self.MAX_RECV_BUFFER)

            if not self.data2:

                print("Server stopped working")
                client_server.close()
                socket_server2.close()

            client_server.send(self.data2)
            print("Data to {}".format(self.data2))

        except socket.error as serr:
            print(str(serr))

if __name__=="__main__":
    Proxy_Server(("127.0.1.1",8081),("127.0.0.10",8090))
