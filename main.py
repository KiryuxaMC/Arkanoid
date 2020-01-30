import pygame
import game_functions as gf
from settings import Settings
from board import Board


def main():
    # Подключение класса настроек
    sett = Settings()

    #Подключение класса доски
    board = Board([sett.W // 2 - 50, sett.H - 40])

    # Инициализация pygame, настройка экрана
    pygame.init()
    screen = pygame.display.set_mode((sett.W, sett.H))
    pygame.display.set_caption('Arkanoid')


    

    while True:
        # Обработка событий
        gf.check_events()
        
        #Обновление экрана
        gf.update_screen(sett, screen, board)
        

if __name__ == '__main__':
    main()
