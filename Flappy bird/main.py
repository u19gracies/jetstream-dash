from movingObjects import MoveBird
import pygame
import time

pygame.init()

screenWidth = 1280
screenHeight = 720
speed = 0.25

screen = pygame.display.set_mode(size=(screenWidth, screenHeight))
pBody = pygame.Rect(50,50,50,50)
p1 = MoveBird(5, 1, pBody, screen)

run = True
while run:
    time.sleep(0.001)

    screen.fill((0,0,0))
    
    p1.gravityEffect()
    pygame.draw.rect(screen, (255,0,0), pBody)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        p1.birdUp()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()