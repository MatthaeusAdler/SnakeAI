import pygame
import settings
import color
import drawer

def runGame():
    snake = [(4,4), (4,5), (4,6)]
    apples = [(2, 2)]
    direction = "UP"
    
    pygame.init()
    pygame.display.set_caption(settings.game_title)

    gameDisplay = pygame.display.set_mode((settings.display_width, settings.display_height))

    clock = pygame.time.Clock()

    started = False
    exited = False

    while not exited:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exited = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exited = True
                    break
                elif not started:
                    started = True
                elif event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                    direction = changeDirection(event.key, direction)
                    break
        
        if started:
            if checkCollision(snake):
                print("GAME OVER")
                exited = True
            else:
                moveSnake(snake, apples, direction)    
        
        drawer.draw_background(gameDisplay)
        drawer.draw_snake(gameDisplay, snake)
        drawer.draw_apple(gameDisplay, apples)

        pygame.display.update()
        clock.tick(settings.fps)

    pygame.quit()
    quit()

def changeDirection(key, cur_direction):
    if key == pygame.K_UP and cur_direction != "DOWN": return "UP"
    elif key == pygame.K_DOWN and cur_direction != "UP": return "DOWN"
    elif key == pygame.K_LEFT and cur_direction != "RIGHT": return "LEFT"
    elif key == pygame.K_RIGHT and cur_direction != "LEFT": return "RIGHT"
    else: return cur_direction

def checkCollision(snake):
    return False

def moveSnake(snake, apples, direction):
    head = snake[0]

    if direction == "UP": new_head = (head[0], head[1] - 1)
    elif direction == "DOWN": new_head = (head[0], head[1] + 1)
    elif direction == "RIGHT": new_head = (head[0] + 1, head[1])
    elif direction == "LEFT": new_head = (head[0] - 1, head[1])

    if new_head == apples[0]:
        snake.insert(0, new_head)
        #create new apple
    else:
        snake.insert(0, new_head)
        snake.pop()
        
runGame()