import pygame
from settings import Settings

def main():
    # Подключение класса настроек
    sett = Settings()

    # Инициализация pygame, настройка экрана
    pygame.init()
    screen = pygame.display.set_mode((sett.W, sett.H))
    pygame.display.set_caption('Arkanoid')

    # Переменная времени
    clock = pygame.time.Clock()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        pygame.display.update()
        screen.fill(sett.white)

if __name__ == '__main__':
    main()
