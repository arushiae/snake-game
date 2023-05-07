import random
from init import *
from pygame.math import Vector2

class Mouse():
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y) #storing x and y position in a 2D vector
        self.image = pygame.image.load('mouse.png').convert_alpha()
        self.image_resized = pygame.transform.scale(self.image, (cell_size, cell_size))

    def draw_mouse(self):
        mouse_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(self.image_resized, mouse_rect)

    def get_mouse_location(self):
        return (self.x, self.y)