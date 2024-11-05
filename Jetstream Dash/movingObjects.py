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
        for i in range(1,5):
            img = HandleSprite(0,pygame.image.load(f"jetpack{i}.png"),288,288,0.35)
            self.images.append(img)

        self.counter=0

        self.image = self.images[self.index]

        self.rect = self.image.rect
        self.rect.topleft=[self.x,self.y]
        self.rect.scale_by_ip(0.35)


    def draw(self, screen, background, canFly):
        if self.prop and canFly:
            if self.counter < 5:
                self.counter+=1
                self.index=0
            elif self.counter < 10:
                self.counter+=1
                self.index=1
            else:
                self.counter=0
        elif not canFly:
            self.index = 3
        else:
            self.index=2

        self.rect.topleft=[self.x,self.y]

        screen.blit(background, (0,0))
        screen.blit((self.images[self.index].createSprite()).convert_alpha(), (self.x,self.y))
        screen.set_colorkey((0,0,0))

        #pygame.draw.rect(screen, (255,255,255), self.rect)


    def updatePlayer(self, spriteList, canFly):
        
        self.speed += 0.2
        if self.speed > 6:
            self.speed = 6
        if self.speed < -5:
            self.speed = -5

        self.y += int(self.speed)

        if pygame.key.get_pressed()[pygame.K_SPACE] == True and canFly:
            self.speed -= 0.4
            self.prop=True
        else:
            self.prop=False

        # for i in spriteList:
        #     print(pygame.Rect.colliderect(self.rect, i[1].rect))

class CreateUpper(pygame.sprite.Sprite):
    def __init__(self, obstacle, img,rand):
        pygame.sprite.Sprite.__init__(self)
        self.rand = rand
        self.obstacle = obstacle
        self.img = img
        self.x = 1280
        self.y = 70
        self.rect = img.get_rect()
        

    
    def move(self, screen, spriteList):
        self.rect.bottomleft = self.x,self.rand
        self.x -= 2
        screen.blit(self.img, self.rect)
        if self.x < -500:
            self.kill()
            spriteList.pop(0)
        

class CreateLower(pygame.sprite.Sprite):
    def __init__(self, obstacle, img,rand):
        pygame.sprite.Sprite.__init__(self)
        self.rand = rand
        self.obstacle = obstacle
        self.img = img
        self.x = 1280
        self.y = 650
        self.rect = img.get_rect()

    def move(self, screen):
        self.rect.topleft = self.x,self.rand
        self.x -= 2
        screen.blit(self.img, self.rect)
        if self.x < -500:
            self.kill()
