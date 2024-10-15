import pygame
import random


class HandleSprite(pygame.sprite.Sprite):

  def __init__(self, frame, img, height, width, scale, add=None):
    pygame.sprite.Sprite.__init__(self)
    self.frame = frame
    self.img = img
    self.height = height
    self.width = width
    self.scale = scale
    self.rect = self.img.get_rect()

  def createObstacleSprite(self):
    sprite = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
    sprite.blit(self.img, (0, 0), (0, self.frame*self.height, self.width, self.height))
    sprite = pygame.transform.scale(sprite, (self.width, self.height * self.scale))
    return sprite

  def createSprite(self):
    sprite = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
    sprite.blit(self.img, (0, 0), (0, self.frame*self.height, self.width, self.height))
    sprite = pygame.transform.scale(sprite, (self.width * self.scale, self.height * self.scale))
    return sprite