from setup import *
from maps import *
from random import randint

def getNewMove():
    return randint(1, 4)

def bagerMove(x, y, game_map):
    global bager_move
    if (randint(0, 100) < 25):
        bager_move = getNewMove()

    if (bager_move == DOWN):
        if (game_map[x + 1][y] == 0):
            game_map[x + 1][y] = a
            game_map[x][y] = 0
    if (bager_move == UP):
        if (game_map[x - 1][y] == 0):
            game_map[x - 1][y] = a
            game_map[x][y] = 0
    if (bager_move == RIGHT):
        if (game_map[x][y + 1] == 0):
            game_map[x][y + 1] = a
            game_map[x][y] = 0
    if (bager_move == LEFT):
        if (game_map[x][y - 1] == 0):
            game_map[x][y - 1] = a
            game_map[x][y] = 0

    return game_map