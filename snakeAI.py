import pygame
import settings
import drawer
import random

def main():
    pygame.init()
    pygame.display.set_caption(settings.game_title)
    
    screen = pygame.display.set_mode(settings.playground_size)    

    clock = pygame.time.Clock()

    running = True
    gameover = True

    points = 0
    last_direction = None
    
    while running:
        drawer.draw_background(screen)

        if gameover:
            drawer.write_centered_text(screen, "Press 'Return' to start the Game", settings.font_size_big)
        else:
            drawer.draw_background(screen)
            drawer.draw_snake(screen, snake)
            drawer.draw_apple(screen, apples)
            drawer.write_top_right_text(screen, "Apples: " + str(points), settings.font_size_medium)

        pygame.display.update()

        clock.tick(settings.fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) :
                    last_direction = changeDirection(event.key, last_direction)
                elif event.key == pygame.K_RETURN and gameover:
                    snake = [(4,4), (4,5), (4,6)]
                    apples = [(2, 2)]
                    last_direction = "UP"
                    points = 0
                    gameover = False

        if running and not gameover:
            if moveSnake(snake, apples, last_direction):
                points = points + 1
            
            if checkCollision(snake):
                gameover = True

    pygame.quit()
    quit()

def changeDirection(key, cur_direction):
    if key == pygame.K_UP and cur_direction != "DOWN": return "UP"
    elif key == pygame.K_DOWN and cur_direction != "UP": return "DOWN"
    elif key == pygame.K_LEFT and cur_direction != "RIGHT": return "LEFT"
    elif key == pygame.K_RIGHT and cur_direction != "LEFT": return "RIGHT"
    else: return cur_direction        

def checkCollision(snake):
    head = snake[0]

    if head[0] < 0 or head[0] > settings.tiles_x - 1 or head[1] < 0 or head[1] > settings.tiles_y - 1:
        return True

    for i in range(1, len(snake) - 1):
        if head == snake[i]:
            return True

def createApple(snake, apples):
    possible_apples = []

    for x in range(0, settings.tiles_x):
        for y in range(0, settings.tiles_y):
            possible_apples.append((x,y))

    for part in snake:
        possible_apples.remove(part)
    
    apple = random.randint(0, len(possible_apples) - 1)
    
    apples.insert(0, possible_apples[apple])
    apples.pop()

def moveSnake(snake, apples, direction):
    head = snake[0]

    if direction == "UP": new_head = (head[0], head[1] - 1)
    elif direction == "DOWN": new_head = (head[0], head[1] + 1)
    elif direction == "RIGHT": new_head = (head[0] + 1, head[1])
    elif direction == "LEFT": new_head = (head[0] - 1, head[1])

    if new_head == apples[0]:
        snake.insert(0, new_head)
        createApple(snake, apples)
        return True
    else:
        snake.insert(0, new_head)
        snake.pop()
        return False

if __name__ == "__main__":
    main()

