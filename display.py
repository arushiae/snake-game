import pygame

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
background = pygame.image.load('background.png').convert()

x = 250
y = 250
new_x = 25
new_y = 0

head_direction = "head_left.png"

snake_body = [(x, y)]

def snake(image):
    global x, y
    x = x + new_x
    y = y + new_y

    head_image = pygame.image.load(image).convert_alpha()

    screen.blit(background, (0, 0))
    screen.blit(head_image, (x % width, y % height))

def findSnakeDirection(event):
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




