import pygame
from setup import *

def menu(pg: pygame, scene, word_font, medium_font, clock, FPS):
    # Выводит на экран меню. Возвращает False,
    # если пользователь выбрал выход

    select_menu = -1

    mouse_y = pygame.mouse.get_pos()[1]

    # Очищаем сцену
    scene.fill((0, 0, 0))

    scene.blit(background, (0, 0))


    msg = "Выберите режим игры:"
    txt = word_font.render(msg, True, (255, 255, 255))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 150))


    if (mouse_y > 250 and mouse_y < 300):
        pygame.draw.rect(scene, (150, 200, 0), (250, 250, 650, 40), 0)
        select_menu = 1
    msg = "1. Обучение"
    txt = word_font.render(msg, True, (200, 255, 255))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 250))


    if (mouse_y > 300 and mouse_y < 350):
        pygame.draw.rect(scene, (150, 200, 0), (250, 300, 650, 40), 0)
        select_menu = 2
    msg = "2. Без подсказок"
    txt = word_font.render(msg, True, (225, 255, 255))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 300))

    if (mouse_y > 350 and mouse_y < 400):
        pygame.draw.rect(scene, (150, 200, 0), (250, 350, 650, 40), 0)
        select_menu = 3
    msg = "3. Выход"
    txt = word_font.render(msg, True, (225, 255, 255))
    scene.blit(txt, ((WIDTH - word_font.size(msg)[0]) // 2, 350))


    msg = "(с) 2022 Евгения Рябухо, 4 класс"
    txt = medium_font.render(msg, True, (50, 255, 255))
    scene.blit(txt, (50, 530))

    msg = "Текстуры, изображения, звуки: Евгения Рябухо"
    txt = medium_font.render(msg, True, (50, 255, 255))
    scene.blit(txt, (50, 550))

    msg = "Научный руководитель проекта: В.Г. Трофимов"
    txt = medium_font.render(msg, True, (50, 255, 255))
    scene.blit(txt, (50, 570))

    # Отрисовываем изображения
    pygame.display.flip()


    # Задержка для синхронизации FPS
    clock.tick(FPS)

    for event in pg.event.get():
        if (event.type == pg.QUIT):
            return False, 0, 0
        elif (event.type == pg.KEYDOWN):
            if (event.key == pg.K_ESCAPE):
                return False, 0, 0
            if (event.key == pg.K_RETURN):
                return True, 1, 0
        elif (event.type == pg.MOUSEBUTTONDOWN):
            if event.button == 1:
                if (select_menu != -1):
                    if (select_menu == 1):
                        return True, 1, LEARN
                    if (select_menu == 2):
                        return True, 1, TEST
                    if (select_menu == 3):
                        return False, 0, 0

    return True, 0, 0
