#import pygame
import pygame

#import CircleShape
from circleshape import CircleShape

#import constants
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    #draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    
    #move the asteroid
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

