#import pygame
import pygame

#import CircleShape
from circleshape import CircleShape

#import constants
from constants import *

#create in-game shots
class Shot(CircleShape):
    def __init__(self, position):
        x = position.x
        y = position.y
        super().__init__(x, y, SHOT_RADIUS, *self.containers)

    #draw the shot
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    #move the shot
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)