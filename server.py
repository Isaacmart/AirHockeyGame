
import socket
from _thread import *
import pickle
from objects import *
from game import Game

server = "192.168.1.128"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server is running. Waiting for connection...")

game = Game()

def threaded_client(conn, num):
    conn.send(pickle.dumps((game.players[num], game.puck)))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            game.players[num] = data

            if not data:
                print("Disconnected")
                break
            else:
                if num == 1:
                    reply = game.players[0]
                else:
                    reply = game.players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            game.goalCollision()
            game.playerCollision(num)
            game.puck.move()
            conn.sendall(pickle.dumps((reply, game.puck)))
        except:
            break

    print("Lost connection")
    conn.close()

num = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, num))
    num += 1