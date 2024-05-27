import pygame
pygame.init()

pemain = [pygame.image.load("sprites/S.png"), pygame.image.load("sprites/S1.png"),pygame.image.load("sprites/S.png"), pygame.image.load("sprites/S1.png")]

class Pemain(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = False
        self.right = False
        self.vel = 5
        self.jumlahjalan = 0
    
    def gambar(self,layar):
        if self.jumlahjalan >= 8:
            self.jumlahjalan = 0
        if self.left:
            layar.blit(pemain[self.jumlahjalan // 2], (self.x, self.y))
            self.jumlahjalan += 1
        elif self.right:
            layar.blit(pemain[self.jumlahjalan // 2], (self.x, self.y))
            self.jumlahjalan += 1
   