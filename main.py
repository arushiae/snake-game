import pygame
import snake


pygame.init()

# creating game window and setting caption
width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python")

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

running = True
start_game = False

x = 250
y = 250
new_x = 1
new_y = 0

clock = pygame.time.Clock()

# display snake
def snake(image):
    global x, y

    x = x + new_x
    y = y + new_y

    head_image = pygame.image.load(image).convert_alpha()

    screen.blit(background, (0, 0))
    screen.blit(head_image, (x%width, y%height))

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

        # change snake head direction
        if (event.type == pygame.KEYDOWN):
            head_direction = "head_right.png"
            if (event.key == pygame.K_LEFT):
                if (new_x != 1):
                    new_x = -1
                    head_direction = "head_left.png"
                new_y = 0
            elif (event.key == pygame.K_RIGHT):
                if (new_x != -1):
                    new_x = 1
                    head_direction = "head_right.png"
                new_y = 0
            elif (event.key == pygame.K_UP):
                if (new_y != 1):
                    new_y = -1
                    head_direction = "head_up.png"
                new_x = 0
            elif (event.key == pygame.K_DOWN):
                if (new_y != -1):
                    new_y = 1
                    head_direction = "head_down.png"
                new_x = 0
            else:
                continue
            snake(head_direction)

        # continue moving when there is no key down event
        if (not pygame.event.get()):
            snake(head_direction)

    # set game speed
    clock.tick(100)

    pygame.display.flip()

pygame.quit()
