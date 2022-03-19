import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.91"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
    # end

    def get_player(self):
        return self.p
    # end

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
        # end
    # end

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096*4))
        except socket.error as e:
            print(e)
        # end
    # end
# end
