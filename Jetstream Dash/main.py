from movingObjects import MoveBody
from movingObjects import CreateObstacle
from sprites import HandleSprite
import pygame
import time

pygame.init()
pygame.mouse.set_visible(False)

screenWidth = 1280
screenHeight = 720
speed = 0.25
clock = pygame.time.Clock()
newOb = True

screen = pygame.display.set_mode((screenWidth, screenHeight)) 
pygame.display.set_caption("Jetstream Dash")

spriteSheet = pygame.image.load("sSheet.png").convert_alpha()
fuelImage = pygame.image.load("fuelCan.png").convert()
obstacleImage = pygame.image.load("obstacle.png").convert()
background = pygame.image.load("bg.png").convert()
jetpack0 = HandleSprite(0,spriteSheet, 288,288, 0.35)
jetpack1 = HandleSprite(1,spriteSheet, 288,288, 0.35)
jetpackOff = HandleSprite(2, spriteSheet, 288,288, 0.35)
jetpacks = [jetpack0,jetpack0,jetpack0,jetpack0,jetpack0,jetpack0,
            jetpack1,jetpack1,jetpack1,jetpack1,jetpack1,jetpack1,
            jetpackOff]
fuelCan = HandleSprite(0,fuelImage, 32,32, 1.5)
ob = HandleSprite(0,obstacleImage, 384, 96, 1.5)

player = MoveBody(200,200,5, 1)
playerSG = pygame.sprite.Group()
playerSG.add(jetpack0)
obstacle1 = CreateObstacle(ob, obstacleImage, 0 )
obstacle2 = CreateObstacle(ob, obstacleImage, 400)
obstacle3 = CreateObstacle(ob, obstacleImage, 800)
obstacle4 = CreateObstacle(ob, obstacleImage, 1200)
obstacleSG = pygame.sprite.Group()
obstacleSG.add(obstacle1)
print(obstacleSG)


run = True
while run:
    clock.tick(60)

    player.updatePlayer()
    player.draw(screen, jetpacks, background)
    
    obstacle1.moveD(screen)
    obstacle1.moveU(screen)
    obstacle2.moveD(screen)
    obstacle2.moveU(screen)
    obstacle3.moveD(screen)
    obstacle3.moveU(screen)
    obstacle4.moveD(screen)
    obstacle4.moveU(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    #screen.blit(fuelCan.createSprite(), (100,250))
        
    pygame.display.update()

    if pygame.mouse.get_pressed()[0] == 1:
        print(pygame.mouse.get_pos())

pygame.quit()