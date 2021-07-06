import pygame
from network import Network
from objects import *

width = 800
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(window, player, player2, puck):
    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    puck.draw(window)
    pygame.display.update()

def main():
    n = Network()
    p1, puck = n.connect()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        p2, puck= n.send((p1))
        p1.move()
        redrawWindow(win, p1, p2, puck)
        

main()