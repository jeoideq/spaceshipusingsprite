import pygame

WIDTH=600
HEIGHT=600 
TITLE="SPACESHIP-USING-SPRITE"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

background=pygame.image.load("space.png")

run = True 
while run:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()






