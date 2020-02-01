import pygame
from pygame.sprite import Sprite

class Brick(Sprite):
    '''Класс кирпича'''
    def __init__(self, screen, sett):
        '''Загрузка изображения, создание спрайта'''
        super(Brick, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = sett
        self.image = pygame.image.load('Arkanoid_Im/block01.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def blit_me(self):
        '''Отрисовка кирича'''
        self.screen.blit(self.image, self.rect)