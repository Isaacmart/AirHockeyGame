
import socket
from _thread import *
import sys

server = "192.168.1.111"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server is running. Waiting for connection...")

def read_pos(txt: str):
    txt = txt.split(",")
    return int(txt[0]), int(txt[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(10,10),(50,50)]
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    while True:
        data = read_pos((conn.recv(2048)).decode())
        pos[player] = data
        if not data:
            break
        else:
            if player == 1:
                reply = pos[0]
            else:
                reply = pos[1]

        conn.sendall(str.encode(make_pos(reply)))

player = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, player))
    player+=1