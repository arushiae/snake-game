import pygame
from pygame import Vector2

from init import *
from mouse import Mouse
import random

# initialize values
x, y = 250, 250
new_x, new_y = 25, 0
mouse_x, mouse_y = 0, 0

head_direction = "head_left.png"

snake_body = [(x, y)]

# snake movement
def snake(image, mouse):

    global x, y
    x = (x + new_x)%500
    y = (y + new_y)%500

    global mouse_x, mouse_y
    mouse_x, mouse_y = mouse.get_mouse_location()

    global snake_body
    snake_body.append((x, y))

    check_mouse_collision()

    head_image = pygame.image.load(image).convert_alpha()
    #tail_image = pygame.image.load("tail.png").convert_alpha()

    screen.blit(background, (0, 0))

    # display snake body
    for (i,j) in snake_body:
        if (snake_body[len(snake_body)-1]== (i, j)):
            screen.blit(head_image, (i, j))
        else:
            if (image == 'head_right.png' or image == 'head_left.png'):
                body_image = pygame.image.load("body_hor.png").convert_alpha()
                screen.blit(body_image, (i, j))
            else:
                body_image = pygame.image.load("body_vert.png").convert_alpha()
                screen.blit(body_image, (i, j))

# find snake direction from key event
def find_snake_direction(event):
    global new_x, new_y
    global head_direction

    if (event.type == pygame.KEYDOWN):
        if (event.key == pygame.K_LEFT):
            if (new_x != 25):
                new_x = -25
                head_direction = "head_left.png"
            new_y = 0
        elif (event.key == pygame.K_RIGHT):
            if (new_x != -25):
                new_x = 25
                head_direction = "head_right.png"
            new_y = 0
        elif (event.key == pygame.K_UP):
            if (new_y != 25):
                new_y = -25
                head_direction = "head_up.png"
            new_x = 0
        elif (event.key == pygame.K_DOWN):
            if (new_y != -25):
                new_y = 25
                head_direction = "head_down.png"
            new_x = 0

    return head_direction

# checks for snake and mouse collision
def check_mouse_collision():
    global mouse_x, mouse_y
    global snake_body
    global x, y

    if (mouse_x == int(x/cell_size) and mouse_y == int(y/cell_size)):
        while ((mouse_x, mouse_y) in snake_body):
            mouse_x, mouse_y = random.randrange(0, 500) // 10 * 10, random.randrange(0, 500) // 10 * 10
    else:
        del snake_body[0]

