import pygame
import color

fps = 5
game_title = "Snake AI"

tile_size = 64
tiles_x = 10
tiles_y = 10

display_width = tiles_x * tile_size
display_height = tiles_y * tile_size

background_color = color.brown

spriteSnake = pygame.image.load('snake-graphics.png')