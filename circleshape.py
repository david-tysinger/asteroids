import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, *groups):
        # we will be using this later
        super().__init__(*groups)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        collision = self.position.distance_to(other.position)
        return collision <= (self.radius + other.radius)
