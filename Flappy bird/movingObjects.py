import pygame

class MoveBird:
    def __init__(self, moveSpeed, gravity, player, screen, jumping):
        self.moveSpeed = moveSpeed
        self.gravity = gravity
        self.player = player
        self.screen = screen
        self.jumping = jumping

    def gravityEffect(self):
        self.player.move_ip(0, self.gravity)

    def birdUp(self):
        print('up!!')
        self.player.move_ip(0, -self.moveSpeed)