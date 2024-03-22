import pygame
fromfrom pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width