from random import randint
import pygame

level = 1

# Сколько попыток на прохождение игры
player_try = 3

# Считать ошибки в тесте
# Режим игры
LEARN = 0
TEST = 1
GAMEMODE = LEARN

WIDTH = 1120
HEIGHT = 640
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60
count_frame = 0
# Скорость змеи. Чем выше число, тем медленней движение
# Получается, змейка будет двигаться КАЖДЫЙ ВОСЬМОЙ КАДР
speed_snake = 10

playGame = True
viewNumberSquare = False

count_candy = 0
level_candy = 0
level_bush_c = 0

MENU = 0
SCREEN_SAVER = 1
RESTART = 2
PLAY = 3
GAME_OVER = 4
GAME_STATE = MENU

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
STOP = 0
move = STOP

badger = None


background = pygame.image.load("png/background.png")

brick = pygame.image.load("png/brick.png")
candy = pygame.image.load("png/candy.png")
snake00 = pygame.image.load("png/snake00.png")
snake01 = pygame.image.load("png/snake01.png")
snake02 = pygame.image.load("png/snake02.png")
snake03 = pygame.image.load("png/snake03.png")
snake04 = pygame.image.load("png/snake04.png")
snake_body = pygame.image.load("png/snake_body.png")
portal = pygame.image.load("png/portal.png")
i_dont_no = pygame.image.load("png/i_dont_no.png")
i_dont_no_brr = pygame.image.load("png/i_dont_no_brr.png")
agi = pygame.image.load("png/agi.png")
bush = pygame.image.load("png/bush.png")
bush_c = pygame.image.load("png/bush_c.png")


# ВСЁ, ЧТО СВЯЗАНО С МЕДОЕДОМ
honey_badger1 = pygame.image.load("png/honey_badger.1.png")
honey_badger2 = pygame.image.load("png/honey_badger.2.png")
honey_badger3 = pygame.image.load("png/honey_badger.3.png")
honey_badger4 = pygame.image.load("png/honey_badger.4.png")

# Изображения для экранной заставки
screen_img = [pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png"),
              pygame.image.load("png/animals/img001.png")]