from math import sqrt
from objects import *

class Game:

    width = 800
    height = 500
    players = [Player(width/4, height/2, 15, (0,0,255), "Left"), Player(width*3/4, height/2, 15, (255,0,0), "Right")]
    goals = [Goal(0, height*3/8, 10, height/4, (0,0,0)), Goal(width-10, height*3/8, 10, height/4, (0,0,0))]

    def __init__(self):
        self.players = [None, None]
        self.goals = Game.goals
        self.puck = Puck(Game.width/2, Game.height/2, 10, (0,0,0))
        self.num = 0
    
    def borderCollision(self):
        if((self.puck.pos[0] < self.puck.radius)):
            self.puck.vel[0] *= -1
            self.puck.pos[0] = self.puck.radius
        if(self.puck.pos[1] < self.puck.radius):
            self.puck.vel[1] *= -1
            self.puck.pos[1] = self.puck.radius
        if((self.height-self.puck.pos[1]) < self.puck.radius):
            self.puck.vel[1] *= -1
            self.puck.pos[1] = self.height - self.puck.radius
        if((self.width-self.puck.pos[0]) < self.puck.radius):
            self.puck.vel[0] *= -1
            self.puck.pos[0] = self.width - self.puck.radius        
    
    def goalCollision(self):
        if ((self.puck.pos[0]-self.goals[0].width < self.puck.radius or self.goals[1].pos[0]-self.puck.pos[0] < self.puck.radius) and (self.puck.pos[1] > self.goals[0].pos[1] and self.puck.pos[1] < (self.goals[0].pos[1]+self.goals[0].height))):
            if(self.puck.pos[0] <= 0 or self.puck.pos[0] >= self.width):
                self.puck.reset(self.puck)
        else:
            self.borderCollision()
    
    def playerCollision(self, num):
        dist = sqrt(((self.puck.pos[0]-self.players[num].pos[0])**2)+((self.puck.pos[1]-self.players[num].pos[1])**2))
        xdir = (self.puck.pos[0]-self.players[num].pos[0])/dist
        ydir = (self.puck.pos[1]-self.players[num].pos[1])/dist
        if(dist < (self.puck.radius + self.players[num].radius)):
            vel = sqrt(self.puck.vel[0]**2 + self.puck.vel[1]**2)
            self.puck.pos[0] += xdir
            self.puck.pos[1] += ydir
            if(self.players[num].relX != 0 and self.players[num].relY != 0):
                self.puck.vel[0] += self.players[num].relX/5
                self.puck.vel[1] += self.players[num].relY/5
            else:
                if(vel < 0.01): vel = 0.01
                self.puck.vel[0] = vel*((self.puck.pos[0]-self.players[num].pos[0])/dist)
                self.puck.vel[1] = vel*((self.puck.pos[1]-self.players[num].pos[1])/dist)