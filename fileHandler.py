import pygame
class Leaderboard:
    def __init__(self, file):
        self.file = file
    
    def displayLB(self,screen,lb):
        lbFont = pygame.font.SysFont("Arial", 44)
        for i in range(len(lb)):
            lbText = lbFont.render(lb[i], True, (255,255,255))
            screen.blit(lbText, (30,180+i*44))