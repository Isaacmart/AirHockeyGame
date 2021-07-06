from math import sqrt
import pygame

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

class Player(Circle):
    def __init__(self, x, y, radius, color, side):
        Circle.__init__(self, x, y, radius, color)
        self.side = side

    def move(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.relX, self.relY = pygame.mouse.get_rel()
        if(self.side == "Left" and self.x >= 400):
            self.x = 400
        elif(self.side == "Right" and self.x <= 400):
            self.x = 400

class Puck(Circle):
    def __init__(self):
        Circle.__init__(self, 400, 250, 10, (0,0,0))
        self.velX = 0
        self.velY = 0

    def playerCollision(self, player):
        dist = sqrt(((self.x-player.x)**2)+((self.y-player.y)**2))
        if(dist < (self.radius + player.radius)):
            self.velX += player.relX/4
            self.velY += player.relY/4
            
    def borderCollision(self):
        if(self.x < self.radius):
            self.velX *= -1
            self.x = self.radius
        if(self.y < self.radius):
            self.velY *= -1
            self.y = self.radius
        if((500-self.y) < self.radius):
            self.velY *= -1
            self.y = 500 - self.radius
        if((800-self.x) < self.radius):
            self.velX *= -1
            self.x = 800 - self.radius
    
    def move(self, player):
        self.playerCollision(player)
        self.borderCollision()

        if(self.velX > 0.75): self.velX = 0.75
        if(self.velY > 0.75): self.velY = 0.75

        self.x += self.velX
        self.y += self.velY

        self.velX *= 0.9997
        self.velY *= 0.9997
    def reset(self, puck):
        del puck
        self.__init__()