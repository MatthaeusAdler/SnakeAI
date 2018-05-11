import pygame
import settings
import color
import drawer

#GAME LOGIC
apple = (2, 2)
#                               HEAD - TAIL
#snake = [(4,4), (4,5), (4,6)]  #top to bottom
#snake = [(4,6), (4,5), (4,4)]  #bottom to top
#snake = [(3,4), (4,4), (6,4)]  #left to right
#snake = [(6,4), (4,4), (3,4)]  #right to left
snake = [(4,4), (4,5), (3,5)]   # TOP - BOTTOM - LEFT

#GAME LOOP
pygame.init()
pygame.display.set_caption(settings.game_title)

gameDisplay = pygame.display.set_mode((settings.display_width, settings.display_height))

clock = pygame.time.Clock()

exited = False

while not exited:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exited = True
        
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_LEFT:

        print(event)
    
    drawer.draw_background(gameDisplay)
    drawer.draw_snake(gameDisplay, snake)
    drawer.draw_apple(gameDisplay, apple)

    pygame.display.update()
    clock.tick(settings.fps)

pygame.quit()
quit()



