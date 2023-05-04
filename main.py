import pygame

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

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            start_game = True

    if start_game:
        # start the game here
        pass

    screen.blit(background, (0, 0))
    screen.blit(snake_image, snake_rect)
    screen.blit(title_text_bg, title_bg_rect)
    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)
    pygame.display.flip()

pygame.quit()