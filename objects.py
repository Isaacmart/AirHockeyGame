import pygame

class Circle:
    def __init__(self, x, y, radius, color):
        self.pos = [x, y]
        self.radius = radius
        self.color = color
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos, self.radius)

class Player(Circle):
    def __init__(self, x, y, radius, color, side):
        Circle.__init__(self, x, y, radius, color)
        self.side = side

    def move(self):
        self.pos[0], self.pos[1] = pygame.mouse.get_pos()
        self.relX, self.relY = pygame.mouse.get_rel()
        if(self.side == "Left" and self.pos[0] >= 400):
            self.pos[0] = 400
        elif(self.side == "Right" and self.pos[0] <= 400):
            self.pos[0] = 400

class Puck(Circle):
    def __init__(self):
        Circle.__init__(self, 400, 250, 10, (0,0,0))
        self.vel = [0,0]
    
    def move(self):
        if(self.vel[0] > 0.75): self.vel[0] = 0.75
        if(self.vel[1] > 0.75): self.vel[1] = 0.75

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.vel[0] *= 0.9997
        self.vel[1] *= 0.9997
    
    def reset(self, puck):
        del puck
        self.__init__()

class Goal():
    def __init__(self, x, y, width, height, color):
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)