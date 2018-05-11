from settings import tile_size, spriteSnake, background_color

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

apple = (0, 3)

def snake_part(part):
    return (part[0] * tile_size, part[1] * tile_size, tile_size, tile_size)

def draw_background(gameDisplay):
    gameDisplay.fill(background_color)

def draw_apple(gameDisplay, apples):
    gameDisplay.blit(spriteSnake, (apples[0][0] * tile_size, apples[0][1] * tile_size), snake_part(apple))

def draw_snake(gameDisplay, snake):
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
        
        gameDisplay.blit(spriteSnake, (snake[i][0] * tile_size , snake[i][1] * tile_size), snake_part(part))
        i = i + 1

    
        