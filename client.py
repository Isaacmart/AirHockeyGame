import pygame
from network import Network

width = 800
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Player:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.center = [self.x, self.y]
        self.radius = radius
        self.color = color
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        self.x, self.y = pygame.mouse.get_pos()

def redrawWindow(window, player, player2):
    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def read_pos(txt):
    txt = str(txt).split(",")
    return int(txt[0]), int(txt[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def main():
    n = Network()
    pPos = read_pos(n.getPos())
    p = [Player(pPos[0],pPos[1], 10, (255,0,0)),Player(100,100, 10, (0,0,255))]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p2Pos = read_pos(n.send(make_pos((p[0].x,p[0].y))))
        p[1].x = p2Pos[0]
        p[1].y = p2Pos[1]
        
        p[0].move()
        redrawWindow(win, p[0], p[1])
        

main()