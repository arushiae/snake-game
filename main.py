import pygame, sys
import random
from pygame.math import Vector2
from display import *

pygame.init()

# creating game window, setting caption & clock
cell_size = 25
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Python")
clock = pygame.time.Clock()

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

# setting the snake icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen.fill((50,168,52))

background = pygame.image.load('background.png').convert()

# loading and getting rectangle for the snake image
snake_image = pygame.image.load('snake.png').convert_alpha()
snake_rect = snake_image.get_rect()
snake_rect.center = (250, 250)

# function to create font
def render_text(font, text, color, pos):
    rendered_text = font.render(text, False, color)
    text_rect = rendered_text.get_rect()
    text_rect.center = pos
    return rendered_text, text_rect

# start screen constants
font = 'DisposableDroidBB.ttf'
white = (255, 255, 255)
dark_green = (21, 71, 52)

# adding start screen font
title_font = pygame.font.Font(font, 80)
title_text, title_rect = render_text(title_font, "PYTHON", white, (255, 140))
title_text_bg, title_bg_rect = render_text(title_font, "PYTHON", dark_green, (258, 143))
start_font = pygame.font.Font(font, 24)
start_text, start_rect = render_text(start_font, "Press any key to start", dark_green, (255, 410))

mouse = Mouse()

running = True
start_game = False

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            start_game = True

    screen.blit(background, (0, 0))
    screen.blit(snake_image, snake_rect)
    screen.blit(title_text_bg, title_bg_rect)
    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)

    if start_game:
        # start the game here
        screen.blit(background, (0,0))

        # change snake head direction and move snake
        head_direction = findSnakeDirection(event)
        snake(head_direction)

        # insert mouse
        mouse.draw_mouse()

    # set game speed
    clock.tick(8)

    pygame.display.flip()

pygame.quit()
sys.exit()
