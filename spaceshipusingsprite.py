import pygame
pygame.init()

WIDTH=600
HEIGHT=600 
TITLE="SPACESHIP-USING-SPRITE"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

background=pygame.image.load("space.png")
spaceship=pygame.image.load("spaceship.png")

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


rocket=Spaceship(300,300,spaceship)
sprites=pygame.sprite.Group()
sprites.add(rocket)


        



        

run = True 
while run:
    screen.blit(background, (0,0))
    sprites.draw(screen)
    keys=pygame.key.get_pressed()
    if keys [pygame.K_w]:
        rocket.rect.y +=5
    if keys [pygame.K_s]:
        rocket.rect.y -=5
    if keys [pygame.K_a]:
         rocket.rect.x +=5
    if keys [pygame.K_d]:
        rocket.rect.x -=5
    if rocket.rect.left<0:
        rocket.rect.left=0
    if rocket.rect.right>600:
        rocket.rect.right=600
    if rocket.rect.top<0:
        rocket.rect.top=0
    if rocket.rect.bottom>600:
        rocket.rect.bottom=600
        
    

    




    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()






