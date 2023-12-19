import pygame
import random


class Snake:
    def __init__(self, WIDTH, HEIGHT, UP, DOWN, LEFT, RIGHT, GRID_SIZE, color):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = color
        self.GRID_SIZE = GRID_SIZE
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.UP = UP
        self.DOWN = DOWN
        self.LEFT = LEFT
        self.RIGHT = RIGHT

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * self.GRID_SIZE)) % self.WIDTH), (cur[1] + (y * self.GRID_SIZE)) % self.HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((self.WIDTH // 2), (self.HEIGHT // 2))]
        self.direction = random.choice([self.UP, self.DOWN, self.LEFT, self.RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], self.GRID_SIZE, self.GRID_SIZE))
