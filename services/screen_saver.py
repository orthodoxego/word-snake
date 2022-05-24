import pygame
from setup import *

def screen_saver(pg: pygame, scene, GAMEMODE, word_font, level, word, clock, FPS):
    # Выводит на экран заставку перед уровнем
    mouse_y = pygame.mouse.get_pos()[1]

    # Очищаем сцену
    scene.fill((0, 0, 0))

    scene.blit(screen_img[level - 1], ((WIDTH - 640) // 2, 100))

    msg = f"Животное: {word[0][1]}, по-английски: {word[0][0]}"
    if (GAMEMODE == TEST):
        msg = f"Животное: {word[0][1]}"

    txt = word_font.render(msg, True, (255, 255, 255))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 580))


    # Отрисовываем изображения
    pygame.display.flip()


    # Задержка для синхронизации FPS
    clock.tick(FPS)

    for event in pg.event.get():
        if (event.type == pg.QUIT):
            return False, RESTART
        elif (event.type == pg.KEYDOWN):
            if (event.key == pg.K_ESCAPE):
                return False, RESTART
            if (event.key == pg.K_RETURN):
                return True, PLAY
            if (event.key == pg.L_SPACE):
                return True, PLAY
        elif (event.type == pg.MOUSEBUTTONDOWN):
            if event.button == 1:
                return True, PLAY

    return True, SCREEN_SAVER
