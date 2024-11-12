import pygame
import random
import sys
from movingObjects import MoveBody, CreateUpper, CreateLower 
from spriteHandler import HandleSprite
from fileHandler import Leaderboard

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
    lbUpdated=False
    user = ''


    try:
        f=open("leaderboard.txt", "x")
        f.close()
    except FileExistsError:
        ''
    f = open("leaderboard.txt", "r+")
    lb = Leaderboard(f)


    fuelImage = pygame.image.load("fuelCan.png").convert()
    obstacleImage = pygame.image.load("obstacle.png").convert_alpha()
    background = pygame.image.load("bg.png").convert()

    #fuelCan = HandleSprite(0,fuelImage,32,32,1.5)

    player = MoveBody(200,200,5,1)

    obstacleSprite = HandleSprite(0,obstacleImage,384,96,1.5)
    spriteList = []

    score = pygame.font.SysFont("Arial", 50)
    gameFont = pygame.font.SysFont("Arial", 70)
    endgameFont = pygame.font.SysFont("Arial", 50)

    setup = True
    run=False
    endgame = False


    while setup:
        clock.tick(120) 
        timer+=1

        begin = gameFont.render("Enter name:", True, (0,0,0))
        name = gameFont.render(user, True, (0,0,0))
        namebg = pygame.Rect(415,325,350,75)
        screen.blit(background, (0,0))

        for i in spriteList:
            i[0].move(screen, spriteList)
            i[1].move(screen)

        pygame.draw.rect(screen, (100,100,100), namebg)
        screen.blit(begin, (400,250))
        screen.blit(name, (420,325))

        if timer > 150:
            rand1 = random.randint(50,450)
            rand2 = rand1+random.randint(124,650-rand1)
            spriteList.append([CreateUpper(obstacleSprite, obstacleImage, rand1),CreateLower(obstacleSprite, obstacleImage,rand2)])
            timer=0 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user = user[:-1]
                if event.key == pygame.K_RETURN and user != '':
                    setup = False
                    run = True
                    spriteList = []
                elif event.key != pygame.K_SPACE and event.key != pygame.K_RETURN:
                    user += event.unicode

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
                f.close()
                pygame.quit()
                sys.exit()
    
        pygame.display.update()


    while endgame:
        clock.tick(120) 
        timer+=1
        screen.blit(background, (0,0))
        
        end = endgameFont.render("Press enter to retry", True, (0,0,0))
        finalScore = endgameFont.render(f"You scored: {count}", True, (0,0,0))
        lbBackground = pygame.Rect(20,180,300,450)


        if pygame.key.get_pressed()[pygame.K_RETURN] == True:
            f.close()
            gameLoop()

        for i in spriteList:
            i[0].move(screen, spriteList)
            i[1].move(screen)

        if timer > 150:
            rand1 = random.randint(50,450)
            rand2 = rand1+random.randint(124,650-rand1)
            spriteList.append([CreateUpper(obstacleSprite, obstacleImage, rand1),CreateLower(obstacleSprite, obstacleImage,rand2)])
            timer=0 
        
        screen.blit(finalScore, (0,50)) 
        screen.blit(end, (0,100)) 
        pygame.draw.rect(screen, (0,0,0), lbBackground)

        if not lbUpdated:
            lboard = f.read().split('\n')
            lboardLength= len(lboard)
            print(lboardLength)
            if lboardLength < 10:
                if lboardLength != 1:
                    for i in range(len(lboard)):
                        x=0
                        n=""
                        for j in range(len(lboard[i])):
                            if lboard[i][j-x] == ":":
                                if lboard[i][j]!=":":
                                    n+=lboard[i][j]
                                x+=1
                        if count > int(n):
                            lboard.insert(i, f'{user}:{count}')
                            break
                        if i+1 == len(lboard):
                            lboard.append(f'{user}:{count}')
                else:
                    lboard.append(f'{user}:{count}')

            else:
                for i in lboard[-1]:
                    if i.isdigit():
                        if count > int(i):
                            lboard = lboard[:-1]
                            for j in range(len(lboard)):
                                x=0
                                n=""
                                for k in range(len(lboard[j])):
                                    if lboard[j][k-x] == ":":
                                        if lboard[j][k]!=":":
                                            n+=lboard[j][k]
                                        x+=1
                                if count > int(n):
                                    lboard.insert(j, f'{user}:{count}')
                                    break
                                if j+1 == len(lboard):
                                    lboard.append(f'{user}:{count}')

            f.close()
            f = open("leaderboard.txt", "w")
            f.write('\n'.join(lboard))
            f.close()

            f = open("leaderboard.txt", "r+")
            new = f.read().split('\n')
            lbUpdated=True
            f.close()
        lb.displayLB(screen, new)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f.close()
                pygame.quit()
                sys.exit()
                
                
        pygame.display.update()
gameLoop()
