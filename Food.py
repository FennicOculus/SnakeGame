import random
import pygame

class Food:
    def __init__(self, color, width, HEIGHT, GRID_SIZE):
        self.color = None
        self.position = (0, 0)
        self.colors = color
        self.width = width
        self.HEIGHT = HEIGHT
        self.GRID_SIZE = GRID_SIZE
        self.randomize_position()

    def randomize_position(self):
        random_number = random.randint(0, 100000)%len(self.colors)
        self.color = self.colors[random_number]
        self.position = (random.randint(0, (self.width//self.GRID_SIZE)-1) * self.GRID_SIZE,
                         random.randint(0, (self.HEIGHT//self.GRID_SIZE)-1) * self.GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], self.GRID_SIZE, self.GRID_SIZE))

