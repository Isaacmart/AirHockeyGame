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
    player = Player(100,100,15,(0,0,255), "Left")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        game.goalCollision()
        game.playerCollision(player)
        player.move()
        game.puck.move()
        redrawWindow(win, player, game.puck, game.goals[0], game.goals[1])
        

main()