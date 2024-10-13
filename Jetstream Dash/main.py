from movingObjects import MoveBody
from sprites import HandleSprite
import pygame
import time

pygame.init()

screenWidth = 1500
screenHeight = 720
speed = 0.25
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screenWidth, screenHeight)) 
pygame.display.set_caption("Jetstream Dash")
pBody = pygame.Rect(50,50,50,50)
player = MoveBody(200,200,5, 1, pBody)
spriteSheet = pygame.image.load("sSheet.png").convert_alpha()
fuelImage = pygame.image.load("fuelCan.png").convert_alpha() 
background = pygame.image.load("bg.png").convert()
jetpack0 = HandleSprite(0,spriteSheet, 288,288, 0.25)
jetpack1 = HandleSprite(1,spriteSheet, 288,288, 0.25)
jetpackOff = HandleSprite(2, spriteSheet, 288,288, 0.25)
jetpacks = [jetpack0,jetpack0,jetpack0,jetpack0,jetpack0,jetpack0,
            jetpack1,jetpack1,jetpack1,jetpack1,jetpack1,jetpack1,
            jetpackOff]
fuelCan = HandleSprite(0,fuelImage, 32,32, 1.5)

while True:
    clock.tick(60)

    player.updatePlayer()
    player.draw(screen, jetpacks, background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(fuelCan.createSprite().convert_alpha(), (250,250))
        
    pygame.display.update()