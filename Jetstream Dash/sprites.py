import pygame


class HandleSprite(pygame.sprite.Sprite):

  def __init__(self, frame, spritesheet, height, width, scale):
    pygame.sprite.Sprite.__init__(self)
    self.frame = frame
    self.spritesheet = spritesheet
    self.height = height
    self.width = width
    self.scale = scale
    self.rect = self.spritesheet.get_rect()

  def createObstacleSprite(self):
    sprite = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
    sprite.blit(self.spritesheet, (0, 0), (0, self.frame*self.height, self.width, self.height))
    sprite = pygame.transform.scale(sprite, (self.width, self.height * self.scale))
    return sprite

  def createSprite(self):
    sprite = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
    sprite.blit(self.spritesheet, (0, 0), (0, self.frame*self.height, self.width, self.height))
    sprite = pygame.transform.scale(sprite, (self.width * self.scale, self.height * self.scale))
    return sprite