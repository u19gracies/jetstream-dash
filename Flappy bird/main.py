from movingObjects import MoveBird
import pygame
import time

pygame.init()

screenWidth = 1280
screenHeight = 720
speed = 0.25

run = True
jumping = False

screen = pygame.display.set_mode(size=(screenWidth, screenHeight))
pBody = pygame.Rect(50,50,50,50)
p1 = MoveBird(5, 1, pBody, screen, jumping)


while run:
    print(jumping)
    time.sleep(0.001)

    screen.fill((0,0,0))
    
    p1.gravityEffect()
    pygame.draw.rect(screen, (255,0,0), pBody)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        if not jumping:
            p1.birdUp()
            jumping = True

    if not key[pygame.K_SPACE]:
        jumping = False
        
    pygame.display.update()

pygame.quit()