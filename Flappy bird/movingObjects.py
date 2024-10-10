import pygame

class MoveBird:
    def __init__(self, moveSpeed, gravity, player, screen):
        self.moveSpeed = moveSpeed
        self.gravity = gravity
        self.player = player
        self.screen = screen

    def gravityEffect(self):
        self.player.move_ip(0, self.gravity)

    def birdUp(self):
        print('up!!')
        self.player.move_ip(0, -self.moveSpeed)