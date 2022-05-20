from setup import *
from maps import *
from random import randint

def bagerMove(x, y, game_map):
    move = randint(1, 4)

    if (move == DOWN):
        if (game_map[x + 1][y] == 0):
            game_map[x + 1][y] = a
            game_map[x][y] = 0
    if (move == UP):
        if (game_map[x - 1][y] == 0):
            game_map[x - 1][y] = a
            game_map[x][y] = 0
    if (move == RIGHT):
        if (game_map[x][y + 1] == 0):
            game_map[x][y + 1] = a
            game_map[x][y] = 0
    if (move == LEFT):
        if (game_map[x][y - 1] == 0):
            game_map[x][y - 1] = a
            game_map[x][y] = 0

    return game_map