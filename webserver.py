import socket

class WebServer(object):
    def __init__(self, reuseAddr = True, reusePort = True, backlog = 5):

        self.address = '', 8889
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if reuseAddr:
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if reusePort:
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.server_socket.bind((self.address))
        self.server_socket.listen(backlog)
        print('Serving HTTP on port {} ...'.format(self.address[1]))


    def start_server(self):
        server_active = True
        while server_active:
            client_connection, client_address = self.server_socket.accept()
            request = client_connection.recv(1024).decode("utf-8")
            print(request)

            http_response = """\
HTTP/1.1 200 OK

Hello, World!
Benzi sugi pula am facut web server !
"""
            client_connection.sendall(http_response.encode("utf-8"))
            client_connection.close()

if __name__ == "__main__":
    ws = WebServer()
    ws.start_server()
