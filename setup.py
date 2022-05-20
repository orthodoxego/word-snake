from random import randint
import pygame

# Считать ошибки в тесте
# Режим игры
LEARN = 0
TEST = 1

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

count_candy = 0
level_candy = 0
level_bush_c = 0

MENU = 0
RESTART = 1
PLAY = 2
GAME_OVER = 3

GAME_STATE = RESTART
level = 6

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
STOP = 0
move = STOP


badger = None

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
honey_badger3 = pygame.image.load("png/honey_badger.3.png")
honey_badger4 = pygame.image.load("png/honey_badger.4.png")
