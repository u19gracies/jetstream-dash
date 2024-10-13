import time
import pygame

class MoveBody:
    def __init__(self, x, y, moveSpeed, gravity, player):
        self.x = x
        self.y = y
        self.moveSpeed = moveSpeed
        self.gravity = gravity
        self.player = player
        self.speed = 0
        self.cFrame = 0
        self.clock = pygame.time.Clock()
        self.prop = False

    def draw(self, screen, jetpacks, background):
        if self.prop:
            if self.cFrame >= 12:
                self.cFrame=0
            self.cFrame += 1
        else:
            self.cFrame = 12
        

        screen.blit(background, (0,0))
        screen.blit((jetpacks[self.cFrame].createSprite()).convert_alpha(), (self.x,self.y))
        screen.set_colorkey((0,0,0))

    def updatePlayer(self):
        
        self.speed += 0.2
        if self.speed > 6:
            self.speed = 6

        if self.y < 590 and self.y > 52:
            self.y += int(self.speed)
        else:
            print("Game over.")

        if pygame.key.get_pressed()[pygame.K_SPACE] == True:
            self.speed -= 0.4
            self.prop=True
        else:
            self.prop=False