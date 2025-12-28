# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

#import Player class
from player import Player

#import Asteroid class
from asteroid import Asteroid

#import AsteroidField class
from asteroidfield import AsteroidField

#import Shot class
from shot import Shot

# import from constants file
from constants import *

# import logger module
from logger import log_state
from logger import log_event

#import sys
import sys

def main():
    #initialize pygame
    pygame.init()

    #set screen width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #set clock object
    clock = pygame.time.Clock()

    #display starting messages
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initialize delta time variable
    dt = 0

    #create asteroid group
    asteroids = pygame.sprite.Group()

    #create shots group
    shots = pygame.sprite.Group()

    #create player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable, )

    #instantiate Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #instantiate AsteroidField
    asteroidfield = AsteroidField()

    #set loop to draw screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill((0, 0, 0))
 #       player.draw(screen)
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
