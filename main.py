import pygame
import game_functions as gf
from settings import Settings
from board import Board
from ball import Ball
from button import Button
from game_stats import GameStats
from bg import BG
from pygame.sprite import Group

def main():
    # Подключение класса настроек
    sett = Settings()

    # Подключение класса статистики
    stats = GameStats()

    # Инициализация pygame, настройка экрана
    pygame.init()
    screen = pygame.display.set_mode((sett.W, sett.H))
    pygame.display.set_caption('Arkanoid')

    # Создание группы кирпичей
    bricks = Group()
    gf.create_bricks(screen, sett, bricks)

    # Подключение класса доски
    board = Board(screen, sett)

    # Подключение класса мячика
    ball = Ball(screen, sett, board)

    # Создание кнопки Play
    play_butt = Button(sett, screen, 'Play')

    # Подключение класса фонового изображения
    bg = BG(screen)


    while True:
        # Обработка событий
        gf.check_events(sett, board, stats, play_butt, screen, bricks)
        
        # Обновлений позиций доски
        board.update()

        # Обновление позиций мячика
        ball.update()

        # Проверка коллизий с обьектами
        gf.check_colision(sett, board, ball, bricks, stats)
        
        # Проверка конца игы
        gf.check_end_game(screen, sett, bricks, ball, stats)

        # Обновление экрана
        gf.update_screen(sett, screen, board, ball, bricks, play_butt, 
                                                            stats,
                                                            bg)
        
        

if __name__ == '__main__':
    main()
