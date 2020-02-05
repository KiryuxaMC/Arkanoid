import pygame.font

class Button:
    def __init__(self, sett, screen, msg):
        '''Инициализирует атрибуты кнопки'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Назначение размеров и свойств кнопок