from setup import *
from maps import *
from random import randint

def getNewMove():
    return randint(1, 4)

def bagerMove(bp, game_map):

    bager_move = bp[2]
    x = bp[0]
    y = bp[1]

    if (randint(0, 100) < 25):
        bager_move = getNewMove()

    if (bager_move == DOWN):
        if (game_map[x + 1][y] == 0):
            game_map[x + 1][y] = a
            bp[0] += 1

    if (bager_move == UP):
        if (game_map[x - 1][y] == 0):
            game_map[x - 1][y] = a
            bp[0] -= 1

    if (bager_move == RIGHT):
        if (game_map[x][y + 1] == 0):
            game_map[x][y + 1] = a
            bp[1] += 1

    if (bager_move == LEFT):
        if (game_map[x][y - 1] == 0):
            game_map[x][y - 1] = a
            bp[1] -= 1

    bp[2] = bager_move

    return bp