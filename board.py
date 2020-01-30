
class Board:
    '''Класс доски'''
    def __init__(self, pos):
        '''Инициализация координат, размеров'''
        self.x = pos[0]
        self.y = pos[1]
        self.width = 100
        self.height = 20
        self.speed = 2


