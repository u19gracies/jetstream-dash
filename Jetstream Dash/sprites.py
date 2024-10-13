import pygame


class HandleSprite:

  def __init__(self, frame, spritesheet, height, width, scale):
    self.frame = frame
    self.spritesheet = spritesheet
    self.height = height
    self.width = width
    self.scale = scale

  def createSprite(self):
    sprite = pygame.Surface((self.width, self.height)).convert_alpha()
    sprite.blit(self.spritesheet, (0, 0), (0, self.frame*self.height, self.width, self.height))
    sprite = pygame.transform.scale(sprite, (self.width * self.scale, self.height * self.scale))
    return sprite
