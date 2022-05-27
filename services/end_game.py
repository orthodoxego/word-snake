import pygame
from setup import *

def endgame(pg: pygame, scene, GAMEMODE, word_font, level, word, clock, FPS):
    # Выводит на экран заставку перед уровнем
    mouse_y = pygame.mouse.get_pos()[1]

    # Очищаем сцену
    scene.fill((0, 0, 0))

    scene.blit(screen_img[9], ((WIDTH - 640) // 2, 80))

    msg = f"КОНЕЦ ИГРЫ... :("
    txt = word_font.render(msg, True, (255, 255, 128))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 20))

    msg = f"Жаль, но ты проиграл. Попробуй ещё раз!"

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
                return True, RESTART
            if (event.key == pg.K_SPACE):
                return True, RESTART
        elif (event.type == pg.MOUSEBUTTONDOWN):
            if event.button == 1:
                return True, RESTART

    return True, ENDGAME
