from movingObjects import MoveBird
import pygame
import time

pygame.init()

screenWidth = 1280
screenHeight = 720
speed = 0.25
clock = pygame.time.Clock()


jump = False

screen = pygame.display.set_mode(size=(screenWidth, screenHeight)) 
pBody = pygame.Rect(50,50,50,50)
p1 = MoveBird(200,200,5, 1, pBody)


while True:
    clock.tick(60)

    p1.updateBird()
    p1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()