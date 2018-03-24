import threading
import socket

# print(os.getpid())
def port_scanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)
    s.settimeout(0.8)
    try:
        s.connect(address)
    except socket.error as error:
        # print("{} este inchis".format(address[1]))
        pass
    else:
        print("{} este deschis".format(address[1]))
        # OPEN_PORTS.append(port)
        s.close()
if __name__ == "__main__":
    for port in range(1, 500):
        mythread = threading.Thread(target=port_scanner, args=("87.106.83.127", port))
        mythread.start()
        # mythread.join()
    # print(OPEN_PORTS)