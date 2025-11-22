from Other_functions import *
from random import randint
import NetworkingUI as UI
from time import sleep
from os import path
import threading
import socket
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
s = socket.socket()
players = []

UI.NetworkUI()
information = UI.network
if len(information) == 0:
    sys.exit()

Type = ""
if len(information) == 1:
    Type = "Server"
    username = information[0]

    try:
        host = socket.gethostname()
        port = randint(6001, 15000)
        s.bind((host, port))
        s.listen(10)
    except:
        s.close()
        error()
        sys.exit()
    
elif len(information) == 3:
    Type = "Client"

    try:
        host = information[1]
        port = int(information[0])
        username = information[2]
        s.connect((host,port))
        players.append([])
        
        #s.send("Hello this is the Client!".encode())
        #print(s.recv(100).decode())
    except:
        s.close()
        error()
        sys.exit()

global x, y
x = 250 - (145 / 6)
y = 250 - (182 / 6)
running = True  
room = pygame.image.load(path.realpath("room.png"))
player_image = pygame.transform.scale(pygame.image.load(path.realpath("player.png")), [145 / 3, 182 / 3])

window = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Networking Demo")
icon = pygame.image.load(path.realpath("player image.png"))
pygame.display.set_icon(icon)

port_label = label(0, 0, (255, 255, 255), port, 25)
host_label = label(0, 0, (255, 255, 255), host.upper(), 25)
host_label.x = 500 - host_label.get_size()[0]
user_label = label(0, 0, (255, 255, 255), username, 20)

global x2, y2
x2 = None
y2 = None

def player_username(x, y, label):
    label.x = (x + (145 / 6)) - (label.get_size()[0] / 2)
    label.y = y - 40
    label.draw(window)

def move():
    global x, y
    Key = pygame.key.get_pressed()
    
    if Key[pygame.K_a]: x -= 2
    elif Key[pygame.K_d]: x += 2
    elif Key[pygame.K_w]: y -= 2
    elif Key[pygame.K_s]: y += 2

def server_recv():
    global x, y, players
    c, addr = s.accept()
    players.append([])
    while running:
        content = c.recv(100).decode()
        info = content.split(",")
        players[0] = [float(info[0]), float(info[1]), None]
        c.send((str(x) + "," + str(y)).encode())
        sleep(0.01)
        
if Type == "Server":
    thread = threading.Thread(target = server_recv)
    thread.start()
  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))#(0, 10, 117)
    window.blit(room, (0, 0))
    
    port_label.draw(window)
    host_label.draw(window)
    player_username(x, y, user_label)

    move()
    window.blit(player_image, [x, y])
    
    if Type == "Client":
        s.send((str(x) + "," + str(y)).encode())
        num = s.recv(100).decode()
        info = num.split(",")
        players[0] = [float(info[0]), float(info[1]), None]
    
    for p in players:
        if len(p) > 0:
            window.blit(player_image, [p[0], p[1]])

    clock.tick(60)
    pygame.display.flip()    

pygame.quit()
sys.exit()
s.close()
