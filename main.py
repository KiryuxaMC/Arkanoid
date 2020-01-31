import pygame
import game_functions as gf
from settings import Settings
from board import Board
from ball import Ball
from pygame.sprite import Group

def main():
    # Подключение класса настроек
    sett = Settings()

    # Инициализация pygame, настройка экрана
    pygame.init()
    screen = pygame.display.set_mode((sett.W, sett.H))
    pygame.display.set_caption('Arkanoid')

    # Создание группы кирпичей
    bricks = Group()

    # Подключение класса доски
    board = Board(screen, sett)

    # Подключение класса мячика
    ball = Ball(screen, sett, board)


    while True:
        # Обработка событий
        gf.check_events(sett, board)
        
        # Обновлений позиций доски
        board.update()

        # Обновление позиций мячика
        ball.update()

        #Обновление экрана
        gf.update_screen(sett, screen, board, ball)
        

if __name__ == '__main__':
    main()
