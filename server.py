
import socket
from _thread import *
import sys
import pickle
from objects import *

server = "192.168.1.111"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server is running. Waiting for connection...")


p = [Player(200,250, 10, (255,0,0), "Left"),Player(600,250, 10, (0,0,255), "Right"), Puck()]

def threaded_client(conn, pNum):
    conn.send(pickle.dumps((p[pNum], p[2])))
    while True:
        try:    
            data = conn.recv(2048)
            p[pNum] = pickle.loads(data)
            if not data:
                print("Disconnected")
                break
            else:
                if pNum == 1:
                    reply = p[0]
                else:
                    reply = p[1]
            
            p[2].move(p[pNum])
            conn.sendall(pickle.dumps((reply, p[2])))
        except:
            break
    print("Lost connection")
    conn.close()

pNum = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, pNum))
    pNum+=1