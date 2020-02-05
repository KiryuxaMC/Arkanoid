import pygame
from brick import Brick
from ball import Ball
from random import randint as rd

def check_events(sett, board, stats, button_play, screen, bricks):
    '''Проверка событий клавиатуры и мыши'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:# выход из игры
            exit()

        # Нажатие клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:# выход из игры
                game_over(screen, sett, stats)
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

        # Нажатие на кнопку Play
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, button_play, mouse_x, mouse_y, screen, sett, bricks)

def check_play_button(stats, play_butt, mouse_x, mouse_y,screen, sett, bricks):
    '''Запуск игры по нажатию на кнопку Play'''
    if play_butt.rect.collidepoint(mouse_x, mouse_y):
        # Игра активна
        stats.game_active = True

def update_screen(sett, screen, board, ball, bricks, button_play, stats, bg):
    '''Обновление экрана'''
    # Фоновое изображение
    bg.blit_me()

    # Отрисовка доски
    board.blit_me()

    # Отрисовка шарика
    ball.blit_me()

    #Отрисовка группы кирпичей
    bricks.draw(screen)

    # Отображение кнопки Play
    if not stats.game_active:
        button_play.draw_button()
        board.stop_moving()
        ball.stop_moving()

    # Обновление экрана и частоты кадров
    pygame.time.Clock().tick(sett.FPS)
    pygame.display.update()
    
def check_colision(sett, board, ball, bricks, stats):
    '''Проверка коллизий'''

    # Проверка доски с мячиком
    if board.rect.colliderect(ball):
        if (board.moving_left and ball.dx > 0) or \
           (board.moving_right and ball.dx < 0):
            ball.dx = 4
        ball.dy *= -1
    
    # Проверка кирпичей и мячика
    if pygame.sprite.spritecollideany(ball, bricks):
        brick = pygame.sprite.spritecollideany(ball, bricks)
        delete_brick(ball, brick)
        stats.score += 1
        
def delete_brick(ball, brick):
    '''Удаляет кирпичи и меняет направление мяча'''

    # Удаление кирпича
    brick.kill()

    # Изменения направления мячика
    ball.dy *= -1
    ball.dx = -2

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

def game_over(screen, sett, stats):
    '''Сценарий конца игры'''

    screen.fill(sett.black)
    font = pygame.font.SysFont('comicsans', 60)
    score_text = font.render(f"SCORE: {stats.score}", 1, sett.white)
    screen.blit(score_text, 
        (sett.W//2 - (score_text.get_width() // 2), 
        30))
    font = pygame.font.SysFont('comicsans', 80)
    game_over = font.render('GAME OVER', 1, sett.white)
    screen.blit(game_over,
                (sett.W//2 - (game_over.get_width() // 2),
                sett.H // 2))
    pygame.display.update()
    pygame.time.delay(2000)
    exit()

def check_end_game(screen, sett, bricks, ball, stats):
    '''Проверка всевозможных концов игры'''

    # Если мяч достиг края поля
    if ball.rect.centery >= ball.screen_rect.height:
        game_over(screen, sett, stats)
    
    # Если все кирпичи игры закончились
    if len(bricks) == 0:
        game_over(screen, sett, stats)
