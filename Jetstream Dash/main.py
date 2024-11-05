import pygame
import random
from movingObjects import MoveBody
from movingObjects import CreateUpper, CreateLower 
from spriteHandler import HandleSprite

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Jetstream Dash")

screenWidth = 1280
screenHeight = 720

def gameLoop():
    screen = pygame.display.set_mode((screenWidth, screenHeight)) 
    clock = pygame.time.Clock()
    canFly = True
    timer = 0
    count = 0


    fuelImage = pygame.image.load("fuelCan.png").convert()
    obstacleImage = pygame.image.load("obstacle.png").convert_alpha()
    background = pygame.image.load("bg.png").convert()

    #fuelCan = HandleSprite(0,fuelImage,32,32,1.5)

    player = MoveBody(200,200,5,1)

    obstacleSprite = HandleSprite(0,obstacleImage,384,96,1.5)
    spriteList = []

    score = pygame.font.SysFont("Arial", 50)
    gameFont = pygame.font.SysFont("Arial", 100)

    setup = True
    run=False
    endgame = False

    while setup:
        clock.tick(120) 
        timer+=1

        begin = gameFont.render("Press space to begin", True, (0,0,0))
        screen.blit(background, (0,0))

        if pygame.key.get_pressed()[pygame.K_SPACE] == True:
            run=True
            setup=False
            spriteList = []

        for i in spriteList:
            i[0].move(screen, spriteList)
            i[1].move(screen)

        screen.blit(begin, (250,250))

        if timer > 150:
            rand1 = random.randint(50,450)
            rand2 = rand1+random.randint(124,650-rand1)
            spriteList.append([CreateUpper(obstacleSprite, obstacleImage, rand1),CreateLower(obstacleSprite, obstacleImage,rand2)])
            timer=0 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 

        pygame.display.update()

        
    while run:
        clock.tick(60) 
        timer+=1
        
        player.updatePlayer(spriteList, canFly)
        player.draw(screen, background, canFly)

        for i in spriteList:
            i[0].move(screen, spriteList)
            i[1].move(screen)
            if player.x+72 == i[0].x + 50:
                count+=1

            if player.x > i[0].x-72 and player.x < i[0].x + 72:
                if player.rect.topleft[1]+10 < i[0].rect.bottomleft[1]:
                    canFly = False

                if player.rect.bottomleft[1]-10 > i[1].rect.topleft[1]:
                    canFly = False

        scoreDisplay = score.render(str(count), True, (255,255,255))
        screen.blit(scoreDisplay, (10,50))
            
        if timer > 150:
            rand1 = random.randint(50,450)
            rand2 = rand1+random.randint(124,650-rand1)
            spriteList.append([CreateUpper(obstacleSprite, obstacleImage, rand1),CreateLower(obstacleSprite, obstacleImage,rand2)])
            timer=0 

        if player.y > 590 or player.y < 52:
            run=False
            endgame=True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
    
        

        pygame.display.update()

    while endgame:
        clock.tick(120) 
        timer+=1
        screen.blit(background, (0,0))
        
        end = gameFont.render("Press space to retry", True, (0,0,0))
        finalScore = gameFont.render(f"You scored: {count}", True, (0,0,0))


        if pygame.key.get_pressed()[pygame.K_SPACE] == True:
            gameLoop()

        for i in spriteList:
            i[0].move(screen, spriteList)
            i[1].move(screen)

        if timer > 150:
            rand1 = random.randint(50,450)
            rand2 = rand1+random.randint(124,650-rand1)
            spriteList.append([CreateUpper(obstacleSprite, obstacleImage, rand1),CreateLower(obstacleSprite, obstacleImage,rand2)])
            timer=0 
        
        screen.blit(end, (250,265))
        screen.blit(finalScore, (275,150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                
        pygame.display.update()
            

gameLoop()