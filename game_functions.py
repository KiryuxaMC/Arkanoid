import pygame
from brick import Brick
from ball import Ball
from random import randint as rd

def check_events(sett, board):
    '''Проверка событий клавиатуры и мыши'''
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

def update_screen(sett, screen, board, ball, bricks):
    '''Обновление экрана'''
    # Заливка белым
    screen.fill(sett.blue)

    # Отрисовка доски
    board.blit_me()

    # Отрисовка шарика
    ball.blit_me()

    #Отрисовка группы кирпичей
    bricks.draw(screen)

    # Обновление экрана и частоты кадров
    pygame.time.Clock().tick(sett.FPS)
    pygame.display.update()
    
def check_colision(sett, board, ball, bricks):
    '''Проверка коллизий'''

    # Проверка доски с мячиком
    if board.rect.colliderect(ball):
        if (board.moving_left and ball.dx > 0) or \
           (board.moving_right and ball.dx < 0):
            ball.dx *= -1
        ball.dy *= -1
    
    # Проверка кирпичей и мячика
    if pygame.sprite.spritecollideany(ball, bricks):
        brick = pygame.sprite.spritecollideany(ball, bricks)
        delete_bricks(ball, brick)
        
def delete_bricks(ball, brick):
    '''Удаляет кирпичи и меняет направление мяча'''

    # Удаление кирпича
    brick.kill()

    # Изменения направления мячика
    ball.dy = -ball.dy
    ball.dx = -ball.dx

def create_bricks(screen, sett, briks):
    '''Создаёт поле кирпичей'''
    brick = Brick(screen, sett)
    available_space_x = sett.W - brick.rect.width
    number_bricks = available_space_x // brick.rect.width
    #print(f"width = {number_bricks*brick.rect.width}")

    for row_brick in range(1, 6):
        for col_brick in range(1, number_bricks):
            brick = Brick(screen, sett)
            brick.rect.x = brick.rect.width*col_brick
            brick.rect.y = brick.rect.height*row_brick
            briks.add(brick)
