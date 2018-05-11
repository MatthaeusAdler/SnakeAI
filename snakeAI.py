import pygame
import settings
import color
import drawer

pygame.init()
pygame.display.set_caption(settings.game_title)

gameDisplay = pygame.display.set_mode((settings.display_width, settings.display_height))

clock = pygame.time.Clock()

exited = False

while not exited:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exited = True
        
        print(event)
    
    gameDisplay.fill(color.brown)
    drawer.draw_snake(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()



