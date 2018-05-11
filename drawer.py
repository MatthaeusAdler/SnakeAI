from settings import tile_size, spriteSnake

head_top = (3, 0)
head_right = (4, 0)
head_left = (3, 1)
head_bottom = (4, 1)

tail_top = (3, 2)
tail_right = (4, 2)
tail_left = (3, 3)
tail_bottom = (4, 3)

body_horizontal = (1, 0)
body_vertical = (2, 1)

def snake_part(part):
    return (part[0] * tile_size, part[1] * tile_size, tile_size, tile_size)

def draw_snake(gameDisplay):
    x = 200
    y = 200

    gameDisplay.blit(spriteSnake, (x , y), snake_part(head_top))