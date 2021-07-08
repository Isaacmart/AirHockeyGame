import pygame
from network import Network
from objects import *
from game import Game

width = 800
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

game = Game()
def redrawWindow(win, *args):
    win.fill((255,255,255))
    for arg in args:
        arg.draw(win)
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
        redrawWindow(win, p1, p2, puck, game.goals[0], game.goals[1])
        

main()