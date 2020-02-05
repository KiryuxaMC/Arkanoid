import pygame.font

class Button:
    '''Класс кнопки'''
    def __init__(self, sett, screen, msg):
        '''Инициализирует атрибуты кнопки'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Назначение размеров и свойств кнопки
        self.width = 100
        self.height = 50
        self.button_color = sett.orange
        self.text_color = sett.white
        self.font = pygame.font.SysFont(None, 48)

        # Построение обьекта rect и кнопки
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        '''Преобразует текст в прямоугольник и варавинвает по цетру'''
        self.msg_image = self.font.render(msg, 
                                        True,
                                        self.text_color,
                                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
