import pygame
import random


class Snake:
    def __init__(self, width, height, up, down, left, right, grid_size, color):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = color
        self.GRID_SIZE = grid_size
        self.WIDTH = width
        self.HEIGHT = height
        self.UP = up
        self.DOWN = down
        self.LEFT = left
        self.RIGHT = right

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
            # Calculate the center of the grid cell
            cell_center_x = p[0] + self.GRID_SIZE // 2
            cell_center_y = p[1] + self.GRID_SIZE // 2

            # Draw a circle in the center of the grid cell
            pygame.draw.circle(surface, self.color, (cell_center_x, cell_center_y), self.GRID_SIZE // 2)

