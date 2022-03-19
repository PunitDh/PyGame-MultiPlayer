import socket as s
from _thread import *
import os
import sys

from helper import make_pos, read_pos

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

pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)
            # end
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
        # end
    print("Lost connection")
    conn.close()
    # end
# end


current_player = 0

while True:
    conn, addr = socket.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
# end
