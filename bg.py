import pygame
from pygame.sprite import Sprite

class BG(Sprite):
    '''Класс для отоброжения фоновой фотографии'''
    def __init__(self, screen):
        '''Инициализация и загрузка картинки'''
        self.image = pygame.image.load('Arkanoid_Im/bg.jpg')
        self.screen = screen
        self.rect = self.image.get_rect(topleft=(0, 0))

    def blit_me(self):
        '''Отрисовка доски'''
        self.screen.blit(self.image, self.rect)