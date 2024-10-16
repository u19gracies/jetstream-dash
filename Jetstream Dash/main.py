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
timer=0

screen = pygame.display.set_mode((screenWidth, screenHeight)) 
pygame.display.set_caption("Jetstream Dash")

fuelImage = pygame.image.load("fuelCan.png").convert()
obstacleImage = pygame.image.load("obstacle.png").convert()
background = pygame.image.load("bg.png").convert()

fuelCan = HandleSprite(0,fuelImage,32,32,1.5)

player = MoveBody(200,200,5,1)
playerSG = pygame.sprite.Group()
playerSG.add(player)
print(playerSG)

obstacleSprite = HandleSprite(0,obstacleImage,384,96,1.5)
playerGroup = pygame.sprite.Group()
obstacleGroup = pygame.sprite.Group()
playerGroup.add(player)
spriteList = []

run = True 
while run:
    current=[]
    clock.tick(60)
    timer+=1

    player.updatePlayer()
    player.draw(screen, background)
 
    for i in spriteList:
        i[0].moveU(screen, spriteList)
        i[1].moveD(screen, spriteList)
 
    if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
        run=False 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    #screen.blit(fuelCan.createSprite(), (100,250)) 

    if timer > 150:
        spriteList.append([CreateObstacle(obstacleSprite),CreateObstacle(obstacleSprite)])
        timer=0
        current = spriteList

        for i, j in current:
            print(i, j) 
        

    if pygame.mouse.get_pressed()[0] == 1:
        print(pygame.mouse.get_pos()) 


    pygame.display.update()
        
        
pygame.quit()