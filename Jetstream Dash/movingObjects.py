import time
import pygame
import random

class MoveBody:
    def __init__(self, x, y, moveSpeed, gravity, imgs):
        self.x = x
        self.y = y
        self.moveSpeed = moveSpeed
        self.gravity = gravity
        self.speed = 0
        self.cFrame = 0
        self.clock = pygame.time.Clock()
        self.prop = False
        self.imgs = imgs
        self.rect = imgs[0].rect

    def draw(self, screen, background):
        if self.prop:
            if self.cFrame >= 12:
                self.cFrame=0
            self.cFrame += 1
        else:
            self.cFrame = 12
        

        screen.blit(background, (0,0))
        screen.blit((self.imgs[self.cFrame].createSprite()).convert_alpha(), (self.x,self.y))
        screen.set_colorkey((0,0,0))

    def updatePlayer(self):
        
        self.speed += 0.2
        if self.speed > 6:
            self.speed = 6
        if self.speed < -5:
            self.speed = -5

        if self.y < 590 and self.y > 52:
            self.y += int(self.speed)
        else:
            print("Game over.")

        if pygame.key.get_pressed()[pygame.K_SPACE] == True:
            self.speed -= 0.4
            self.prop=True
        else:
            self.prop=False

class CreateObstacle:
    def __init__(self, obstacle, add, img):
        self.randu = random.randint(1,315)
        self.randd = random.randint(1,315-self.randu)
        self.obstacle = obstacle
        self.x = 1000 + add
        self.yD = 600
        self.yU = -450
        self.rect = img.get_rect()

    
    def moveU(self, screen):
        screen.blit(self.obstacle.createObstacleSprite(), (self.x,self.yD-self.randu))
        self.x -= 2
        if self.x < -300:
            self.x = 1300
            self.randu = random.randint(1,315)
            self.randd = random.randint(1,315-self.randu)
            

    def moveD(self, screen):
        screen.blit(self.obstacle.createObstacleSprite(), (self.x,self.yU+self.randd))
        self.x -= 2
        if self.x < -300:
            self.x = 1300
            self.randu = random.randint(1,315)
            self.randd = random.randint(1,315-self.randu)
