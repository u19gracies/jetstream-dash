import time
import pygame

class MoveBird:
    def __init__(self, x, y, moveSpeed, gravity, player):
        self.x = x
        self.y = y
        self.moveSpeed = moveSpeed
        self.gravity = gravity
        self.player = player
        self.clicked = False
        self.speed = 0

    def draw(self, screen):
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 50, 50))

    def updateBird(self):
        self.speed += 0.3
        if self.speed > 10:
            self.speed = 10
        elif self.speed < -10:
            self.speed = -10

        if self.y < 620 and self.y > 20:
            self.y += int(self.speed)
        else:
            print("Game over.")

        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked=True
            self.speed -=15
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked=False 