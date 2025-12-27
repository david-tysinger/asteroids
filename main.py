# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

#import Player class
from player import Player

# import from constants file
from constants import *

# import logger module
from logger import log_state

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

    #instantiate Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #set loop to draw screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
