import pygame

def check_events(sett, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# выход из игры
            exit()

        # Нажатие клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:# выход из игры
                exit()
            elif event.key == pygame.K_LEFT:# перемещение влево
                board.moving_left = True
            elif event.key == pygame.K_RIGHT:# перемещение вправо
                board.moving_right = True

        # Отжатие клавиш
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:# перемещение влево
                board.moving_left = False
            elif event.key == pygame.K_RIGHT:# перемещение вправо
                board.moving_right = False

def update_screen(sett, screen, board, ball):
    '''Обновление экрана'''
    # Заливка белым
    screen.fill(sett.white)

    # Отрисовка доски
    board.blit_me()

    # Отрисовка шарика
    ball.blit_me()

    # Обновление экрана и частоты кадров
    pygame.time.Clock().tick(sett.FPS)
    pygame.display.update()
    
    