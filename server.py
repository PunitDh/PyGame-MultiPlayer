import pickle
import socket as s
from _thread import *
import os
import sys

from constants import COLOR
from game import Game
from player import Player

server = "192.168.0.91"
port = 5555
socket = s.socket(s.AF_INET, s.SOCK_STREAM)

try:
    socket.bind((server, port))
except s.error as e:
    str(e)
# end

socket.listen(2)
print("Waiting for a connection, server started")

connected = set()
games = {}
id_count = 0


def threaded_client(connection, current_player, game_id_thread):
    global id_count
    connection.send(str.encode(str(current_player)))
    while True:
        try:
            data = connection.recv(4096).decode()
            if game_id_thread in games:
                game = games[game_id_thread]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset_went()
                    elif data != "get":
                        game.play(current_player, data)
                    # end
                    connection.sendall(pickle.dumps(game))
            else:
                break
            # end
        except:
            break
        # end
    print("Lost connection...")
    try:
        del games[game_id_thread]
        print("Closing game", game_id_thread)
    except:
        pass
    id_count -= 1
    connection.close()
    # end
# end


while True:
    conn, addr = socket.accept()
    print("Connected to:", addr)
    id_count += 1
    player = 0
    game_id = (id_count - 1)//2
    if id_count % 2 == 1:
        games[game_id] = Game(game_id)
        print("Creating a new game...")
    else:
        games[game_id].ready = True
        player = 1
    # end
    start_new_thread(threaded_client, (conn, player, game_id))
# end
