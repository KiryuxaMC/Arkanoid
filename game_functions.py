import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# выход из игры
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:# выход из игры
                exit()
            if event.key == pygame.K_LEFT:# перемещение влево
                pass
            if event.key == pygame.K_RIGHT:# перемещение вправо
                pass

def update_screen(sett, screen, board):
    '''Обновление экрана'''
    screen.fill(sett.white)
    pygame.time.Clock().tick(sett.FPS)

    # Отрисовка доски
    pygame.draw.ellipse(screen, 
                        sett.red, 
                        (board.x,
                        board.y,
                        board.width,
                        board.height))
    
    # Обновление экрана
    pygame.display.update()
    