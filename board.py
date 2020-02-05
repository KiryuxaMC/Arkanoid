import pygame
from pygame.sprite import Sprite

class Board(Sprite):
    '''Класс доски'''
    def __init__(self, screen, sett):
        '''Инициализация координат, размеров'''
        self.screen = screen
        self.image = pygame.image.load('Arkanoid_Im/paddle.png')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect(bottomright=(self.screen_rect.centerx,
                                                    self.screen_rect.height))
        self.moving_right = False
        self.moving_left = False
        self.settings = sett
    
    def update(self):
        '''Проверка на колизи со стенами'''
        if self.moving_right and \
           self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.board_speed
        elif self.moving_left and \
           self.rect.left > 0:
            self.rect.centerx -= self.settings.board_speed
        
    def blit_me(self):
        '''Отрисовка доски'''
        self.screen.blit(self.image, self.rect)

    def stop_moving(self):
        '''Функция для остановки движения'''
        self.moving_left = False
        self.moving_right = False
