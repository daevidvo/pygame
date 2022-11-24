import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('test title')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)

# creates a regular surface in the game.
# below is the code for creating the surface along with the w,h of it.
# test_surface = pygame.Surface((600,100))
# below is the code for creating the fill of said surface along with the color.
# test_surface.fill('Blue')

#sky_surface = pygame.image.load('graphics/EeBQj8MUYAITUf6.jpg')
#ground_surface = pygame.image.load('graphics/tumblr_oi0zvwAFAe1sfbymbo1_400.jpg')
text_surface = test_font.render('HELLO',True,'black')
sky_surface = pygame.Surface((1600,600))
sky_surface.fill('light blue')
ground_surface = pygame.Surface((1600,300))
ground_surface.fill('dark green')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # pygame draws in the order that you write the code. sky_surface will always be below the ground_surface
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,600))
    # the rendering of the text will always go over the top of the other layers since it's rendering as a display surface instead of a regular surface
    screen.blit(text_surface,(700,0))
    pygame.display.update()
    clock.tick(120)
    

