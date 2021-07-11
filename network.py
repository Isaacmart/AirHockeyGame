import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = "192.168.1.129"
        self.port = 5555
        self.server = (self.addr, self.port)
    
    def connect(self):
        try:
            self.client.connect(self.server)
            return pickle.loads(self.client.recv(2048))
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except:
            pass

        