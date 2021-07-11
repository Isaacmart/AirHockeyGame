import socket
from _thread import *
import pickle
from objects import *
from game import Game

server = "192.168.1.129"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Server is running. Waiting for connection...")

num = 0
games = []
gameID = 0

def threaded_client(conn, num, game):
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

                #print("Received: ", data)
                #print("Sending : ", reply)

            game.goalCollision()
            game.playerCollision(num)
            game.puck.move()
            conn.sendall(pickle.dumps((reply, game.puck)))
        except:
            break

    print("Lost connection")
    conn.close()
    game.players[num] = None
    for i in range(len(games)-1): 
        if(games[i].players == [None, None]): 
            del games[i]
            print(True)

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    if(num == 0): games.append(Game())
    if None in games[-1].players: num = games[-1].players.index(None)
    else:
        num = 0
        games.append(Game())
        
    games[-1].players[num] = Game.players[num]

    start_new_thread(threaded_client, (conn, num, games[-1]))
    num += 1