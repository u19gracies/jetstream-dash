from movingObjects import MoveBody
from movingObjects import CreateObstacle
from spriteHandler import HandleSprite
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
jetpack0 = HandleSprite(0,spriteSheet,288,288,0.35)
jetpack1 = HandleSprite(1,spriteSheet,288,288,0.35)
jetpackOff = HandleSprite(2, spriteSheet,288,288,0.35)
jetpacks = [jetpack0,jetpack0,jetpack0,jetpack0,jetpack0,jetpack0,
            jetpack1,jetpack1,jetpack1,jetpack1,jetpack1,jetpack1,
            jetpackOff]
fuelCan = HandleSprite(0,fuelImage,32,32,1.5)

player = MoveBody(200,200,5,1,jetpacks)
playerSG = pygame.sprite.Group()
playerSG.add(jetpack0)
playerSG.add(jetpack1)
playerSG.add(jetpackOff)

obstacle1S = HandleSprite(0,obstacleImage,384,96,1.5,0)
obstacle2S = HandleSprite(0,obstacleImage,384,96,1.5,400)
obstacle3S = HandleSprite(0,obstacleImage,384,96,1.5,800)
obstacle4S = HandleSprite(0,obstacleImage,384,96,1.5,1200)
obstacle1 = CreateObstacle(obstacle1S,0, obstacleImage)
obstacle2 = CreateObstacle(obstacle2S,400, obstacleImage)
obstacle3 = CreateObstacle(obstacle3S,800, obstacleImage)
obstacle4 = CreateObstacle(obstacle4S,1200, obstacleImage)

run = True 
while run:
    print(player.x, player.y)
    clock.tick(60)

    player.updatePlayer()
    player.draw(screen, background)
    
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

    pygame.display.update()
    #screen.blit(fuelCan.createSprite(), (100,250)) 

    if pygame.mouse.get_pressed()[0] == 1:
        print(pygame.mouse.get_pos()) 

    if pygame.Rect.colliderect(obstacle1.rect, player.rect):
        print('collision')
        
pygame.quit()