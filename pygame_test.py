import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('test title')
clock = pygame.time.Clock()

## creates a regular surface in the game.
## below is the code for creating the surface along with the w,h of it.
## test_surface = pygame.Surface((600,100))
## below is the code for creating the fill of said surface along with the color.
## test_surface.fill('Blue')

test_surface = pygame.image.load('graphics/EeBQj8MUYAITUf6.jpg')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)
    

