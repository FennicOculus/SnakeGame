import random
import pygame
import os

class Food:
    def __init__(self, width, height, grid_size, color=None, image_path=None):
        self.color = None
        self.image = None
        self.image_path = image_path
        self.position = (0, 0)
        self.colors = color
        self.width = width
        self.HEIGHT = height
        self.GRID_SIZE = grid_size
        self.randomize_position()

    def randomize_position(self):
        if self.colors:
            random_number = random.randint(0, 100000) % len(self.colors)
            self.color = self.colors[random_number]
        if self.image_path:
            image_files = [file for file in os.listdir(self.image_path) if file.endswith(".png")]
            random_number = random.randint(0, 100000) % len(image_files)
            self.image = pygame.image.load(self.image_path+'/'+image_files[random_number])
            # Resize image to match grid size
            self.image = pygame.transform.scale(self.image, (self.GRID_SIZE, self.GRID_SIZE))
        self.position = (random.randint(0, (self.width//self.GRID_SIZE)-1) * self.GRID_SIZE,
                         random.randint(0, (self.HEIGHT//self.GRID_SIZE)-1) * self.GRID_SIZE)

    def rendercolor(self, surface):
        cell_center_x = self.position[0] + self.GRID_SIZE // 2
        cell_center_y = self.position[1] + self.GRID_SIZE // 2

        # Draw a circle in the center of the grid cell
        pygame.draw.circle(surface, self.color, (cell_center_x, cell_center_y), self.GRID_SIZE // 2)

    def render(self, surface):
        surface.blit(self.image, self.position)

