import pygame
from setup import *

def win_game(pg: pygame, scene, word_font, clock, FPS):
    # Выводит на экран заставку перед уровнем
    mouse_y = pygame.mouse.get_pos()[1]

    # Очищаем сцену
    scene.fill((0, 0, 0))

    scene.blit(screen_img[10], ((WIDTH - 640) // 2, 60))

    msg = f"ПОЛНАЯ И БЕЗОГОВОРОЧНАЯ ПОБЕДА!"

    txt = word_font.render(msg, True, (255, 255, 128))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 20))

    msg = f"Надеюсь, что вы выучили новые слова!"
    txt = word_font.render(msg, True, (255, 255, 255))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 550))

    msg = f"С уважением, юная разработчица Женя Рябухо!"
    txt = word_font.render(msg, True, (255, 255, 255))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 580))



    # Отрисовываем изображения
    pygame.display.flip()


    # Задержка для синхронизации FPS
    clock.tick(FPS)

    for event in pg.event.get():
        if (event.type == pg.QUIT):
            return False, MENU
        elif (event.type == pg.KEYDOWN):
            if (event.key == pg.K_ESCAPE):
                return False, MENU
            if (event.key == pg.K_RETURN):
                return True, MENU
            if (event.key == pg.K_SPACE):
                return True, MENU
        elif (event.type == pg.MOUSEBUTTONDOWN):
            if event.button == 1:
                return True, MENU

    return True, WINGAME
