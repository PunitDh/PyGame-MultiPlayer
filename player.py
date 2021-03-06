import pygame
from constants import WINDOW


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 3
        self.rect = (x, y, width, height)

    def draw(self):
        pygame.draw.rect(WINDOW, self.color, self.rect)
    # end

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.update()
    # end

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
    # end
# end