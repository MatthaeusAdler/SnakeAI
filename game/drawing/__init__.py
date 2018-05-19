import pygame

from settings import *
from .color import Color

FONT_FAMILY = "Bauhaus 93"
FONT_SIZE = 45

spriteCollection = pygame.image.load('snake-graphics.png')

head_top = (3, 0)
head_right = (4, 0)
head_bottom = (4, 1)
head_left = (3, 1)

tail_top = (3, 2)
tail_right = (4, 2)
tail_bottom = (4, 3)
tail_left = (3, 3)

body_vertical = (2, 1)
body_horizontal = (1, 0)

body_top_right = (0, 1)
body_top_left = (2, 2)

body_bottom_right = (0, 0)
body_bottom_left = (2, 0)

apple_pos = (0, 3)

def getSpriteCoordinate(part):
    return (part[0] * TILE_SIZE, part[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)

def draw_background(screen):
     screen.fill(Color.BROWN)

def write_text(screen, text):
    font = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
    label = font.render(text,  1, Color.BLUE)

    screen_width, screen_height = screen.get_size()

    x = screen_width / 2 - label.get_rect().width / 2
    y = screen_height / 2 - label.get_rect().height / 2

    screen.blit(label, (x, y))

def draw_apple(screen, apple):
    screen.blit(spriteCollection, (apple[0] * TILE_SIZE, apple[1] * TILE_SIZE), getSpriteCoordinate(apple_pos))

def draw_snake(screen, snake):
    i = 0

    while i < len(snake):
        if i == 0:
            vX = snake[i][0] - snake[i + 1][0]
            vY = snake[i][1] - snake[i + 1][1]

            if vX < 0: part = head_left
            elif vX > 0: part = head_right
            elif vY < 0: part = head_top
            elif vY > 0: part = head_bottom
            
        elif i == len(snake) - 1:
            vX = snake[i - 1][0] - snake[i][0]
            vY = snake[i - 1][1] - snake[i][1]

            if vX < 0: part = tail_left
            elif vX > 0: part = tail_right            
            elif vY < 0: part = tail_top
            elif vY > 0: part = tail_bottom
                    
        else:
            #VECTOR 1
            v1X = snake[i - 1][0] - snake[i][0]
            v1Y = snake[i - 1][1] - snake[i][1]

            #VECTOR 2
            v2X = snake[i][0] - snake[i + 1][0]
            v2Y = snake[i][1] - snake[i + 1][1]

            if v1Y < 0:
                if v2Y != 0:
                    part = body_vertical
                elif v2X < 0:
                    part = body_top_right
                elif v2X > 0:
                    part = body_top_left
            elif v1Y > 0:
                if v2Y != 0:
                    part = body_vertical
                elif v2X < 0:
                    part = body_bottom_right
                elif v2X > 0:
                    part = body_bottom_left
            elif v1X < 0:
                if v2X != 0:
                    part = body_horizontal
                elif v2Y > 0:
                    part = body_top_left
                elif v2Y < 0:
                    part = body_bottom_left
            elif v1X > 0:
                if v2X != 0:
                    part = body_horizontal
                elif v2Y < 0:
                    part = body_bottom_right
                elif v2Y > 0:
                    part = body_top_right
        
        screen.blit(spriteCollection, (snake[i][0] * TILE_SIZE , snake[i][1] * TILE_SIZE), getSpriteCoordinate(part))
        i = i + 1