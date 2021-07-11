import pygame
from network import Network
from objects import *
from game import Game

win = pygame.display.set_mode((Game.width, Game.height))
pygame.display.set_caption("Client")

def redrawWindow(win, *args):
    win.fill((255,255,255))
    for arg in args:
        if arg == None: continue
        else: arg.draw(win)
    pygame.display.update()

def main():
    n = Network()
    p1, puck = n.connect()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        p2, puck = n.send(p1)
        p1.move()
        redrawWindow(win, p1, p2, puck, Game.goals[0], Game.goals[1])


main()