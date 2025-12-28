#import pygame
import pygame

#import random library
import random

#import CircleShape
from circleshape import CircleShape

#import constants
from constants import *

# import logger module
from logger import log_state
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, *self.containers)

    #draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    #move the asteroid
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    #split the asteroid
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50) # degrees
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(random_angle)*1.2
        new_asteroid2.velocity = self.velocity.rotate(-random_angle)*1.2

