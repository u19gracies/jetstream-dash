import time
import pygame
import random
from spriteHandler import HandleSprite

class MoveBody(pygame.sprite.Sprite):
    def __init__(self, x, y, moveSpeed, gravity):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.moveSpeed = moveSpeed
        self.gravity = gravity
        self.speed = 0
        self.clock = pygame.time.Clock()
        self.prop = False
        self.index=0
        self.images=[]
        for i in range(1,4):
            img = HandleSprite(0,pygame.image.load(f"jetpack{i}.png"),288,288,0.35)
            self.images.append(img)

        self.counter=0

        self.image = self.images[self.index]

        self.rect = self.image.rect
        self.rect.center=[x,y]


    def draw(self, screen, background):
        if self.prop:
            if self.counter < 5:
                self.counter+=1
                self.index=0
            elif self.counter < 10:
                self.counter+=1
                self.index=1
            else:
                self.counter=0
        else:
            self.index=2

        screen.blit(background, (0,0))
        screen.blit((self.images[self.index].createSprite()).convert_alpha(), (self.x,self.y))
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

class CreateObstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle):
        pygame.sprite.Sprite.__init__(self)
        self.randu = random.randint(1,315)
        self.randd = random.randint(1,316-self.randu)
        self.obstacle = obstacle
        self.x = 1500
        self.yD = 600
        self.yU = -450
        self.rect = obstacle.rect

    
    def moveU(self, screen, spriteList):
        screen.blit(self.obstacle.createObstacleSprite(), (self.x,self.yD-self.randu))
        self.x -= 2
        if self.x < -500:
            spriteList.pop(1)
            

    def moveD(self, screen, spriteList):
        screen.blit(self.obstacle.createObstacleSprite(), (self.x,self.yU+self.randd))
        self.x -= 2
        if self.x < -500:
            spriteList.pop(1)
