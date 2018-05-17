import pygame
import color

game_title = "Snake AI"

fps = 10
disableUI = True #unused
background_color = color.brown

tile_size = 64
tiles_x, tiles_y = 10, 10
playground_size = (tile_size * tiles_x, tile_size * tiles_y)

font_color = color.blue
font_family = "Bauhaus 93"
font_size_big = 45
font_size_medium = int(font_size_big / 2)
font_size_small = int(font_size_big / 4)


spriteCollection = pygame.image.load('snake-graphics.png')