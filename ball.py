import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    '''Класс шарика'''
    def __init__(self, screen, sett, board):
        '''Загрузка изображения шарика'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sett
        self.image = pygame.image.load('Arkanoid_Im/ball.png')
        self.rect = self.image.get_rect(bottomright=(board.rect.centerx,
                                                    board.rect.y))
        self.dx = 4
        self.dy = -3
        self.board = board

    def update(self):
        '''Проверка на коллизии со стенами'''
        if self.rect.centerx >= self.screen_rect.right or \
           self.rect.centerx <= self.screen_rect.left:
            self.dx = -self.dx

        if self.rect.centery >= self.screen_rect.height or \
           self.rect.centery <= 0:
            self.dy = -self.dy

        self.rect.centery += self.dy
        self.rect.centerx += self.dx
        
    
    def blit_me(self):
        '''Отрисовка шарика'''
        self.screen.blit(self.image, self.rect)
