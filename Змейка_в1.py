# Подключаем pygame
# ПРИВЕТ, ЕВГЕНИЯ АЛЕКСЕЕВНА!
import pygame
from setup import *
from maps import *
from honey_badger.honey_badger import *
from services.menu import *
from services.screen_saver import *
from services.next_try import *
from services.end_game import *

# Выводит кирпичную стену
def draw_brick():
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            SQUARE = game_map[i][j]
            if SQUARE == BRICK:
                scene.blit(brick, (j * 32, i * 32))

# Выводит пылесосы
def draw_vacuum_cleaner():
    for i in range(len(badger_position)):
        if (badger_position[i][2] == UP):
            scene.blit(honey_badger1, (badger_position[i][1] * 32, badger_position[i][0] * 32))
        if (badger_position[i][2] == LEFT):
            scene.blit(honey_badger2, (badger_position[i][1] * 32, badger_position[i][0] * 32))
        if (badger_position[i][2] == DOWN):
            scene.blit(honey_badger3, (badger_position[i][1] * 32, badger_position[i][0] * 32))
        if (badger_position[i][2] == RIGHT):
            scene.blit(honey_badger4, (badger_position[i][1] * 32, badger_position[i][0] * 32))

# Выводит змейку на экран
def draw_snake(scene, move, snake):
    # Выводим голову
    if move == STOP:
        scene.blit(snake00, (snake[0][0] * 32, snake[0][1] * 32))
    elif move == UP:
        snake, move = move_snake(snake, move)
        scene.blit(snake01, (snake[0][0] * 32, snake[0][1] * 32))
    elif move == DOWN:
        snake, move = move_snake(snake, move)
        scene.blit(snake02, (snake[0][0] * 32, snake[0][1] * 32))
    elif move == LEFT:
        snake, move = move_snake(snake, move)
        scene.blit(snake03, (snake[0][0] * 32, snake[0][1] * 32))
    elif move == RIGHT:
        snake, move = move_snake(snake, move)
        scene.blit(snake04, (snake[0][0] * 32, snake[0][1] * 32))

    # Выводим тело змеи и хвост
    for i in range(1, len(snake)):
        scene.blit(snake_body, (snake[i][0] * 32, snake[i][1] * 32))

# Есть ли свободная клетка для движения змейки
def no_move_snake(gm):
    nx = snake[0][0]
    ny = snake[0][1]

    for i in range(len(badger_position)):
        for j in range(len(snake)):
            if (badger_position[i][1] == snake[j][0] and badger_position[i][0] == snake[j][1]):
                return True

    count_field_snake = 0

    # Расчёт окружения стенами

    if (game_map[ny][nx + 1] == 1):
        count_field_snake += 1
    if (game_map[ny][nx - 1] == 1):
        count_field_snake += 1
    if (game_map[ny + 1][nx] == 1):
        count_field_snake += 1
    if (game_map[ny - 1][nx] == 1):
        count_field_snake += 1

    nnx = nx + 1
    nny = ny
    for i in range(1, len(snake)):
        if (snake[i][0] == nnx and snake[i][1] == nny):
            count_field_snake += 1

    nnx = nx - 1
    nny = ny
    for i in range(1, len(snake)):
        if (snake[i][0] == nnx and snake[i][1] == nny):
            count_field_snake += 1

    nnx = nx
    nny = ny + 1
    for i in range(1, len(snake)):
        if (snake[i][0] == nnx and snake[i][1] == nny):
            count_field_snake += 1

    nnx = nx
    nny = ny - 1
    for i in range(1, len(snake)):
        if (snake[i][0] == nnx and snake[i][1] == nny):
            count_field_snake += 1

    if (count_field_snake == 4):
        return True

    return False

def getBagerPositions():
    # Выводим изображение карты
    bp = []
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            SQUARE = game_map[i][j]
            if SQUARE == a:
                bp.append([i, j, randint(1, 4)])
                game_map[i][j] = 0
    return bp

def draw_text(scene):
    text_to_screen_color = (255, 200, 200)
    text_to_screen_word = "ГОТОВО! НАЙДИТЕ ПЕРЕХОД НА УРОВЕНЬ!"
    if not word_complete:
        text_to_screen_color = (250, 250, 255)
        text_to_screen_word = f"Соберите слово: {word[0][1]}"

    txt = word_font.render(text_to_screen_word, True, (32, 32, 32))
    scene.blit(txt, (WIDTH - word_font.size(text_to_screen_word)[0] - 5, -2))

    txt = word_font.render(text_to_screen_word, True, text_to_screen_color)
    scene.blit(txt, (WIDTH - word_font.size(text_to_screen_word)[0] - 8, -5))

    text_to_screen_color = (255, 255, 200)
    text_to_screen_word = f"Попыток: {player_try}"
    txt = word_font.render(text_to_screen_word, True, text_to_screen_color)
    scene.blit(txt, (32, -5))

def check_candy(snake, game_map):
    """ Возвращает True когда змейка ест конфету. """
    if game_map[snake[0][1]][snake[0][0]] == 2:
        game_map[snake[0][1]][snake[0][0]] = 0
        return True    
    return False

def check_bush_c(snake, game_map):
    """ Возвращает True когда змейка ест конфету с кустами. """
    if game_map[snake[0][1]][snake[0][0]] == 8:
        game_map[snake[0][1]][snake[0][0]] = 3
        return True
    return False

def check_portal(snake, game_map):
    """ Возвращает True когда змейка на портале. """
    if game_map[snake[0][1]][snake[0][0]] == 4:
        game_map[snake[0][1]][snake[0][0]] = 0
        return True    
    return False

def move_snake(snake, move):
    """ Обработает движение змейки. """        
    if count_frame % speed_snake != 0:
        return snake, move
    
    nx = snake[0][0]
    ny = snake[0][1]
    
    if move == UP:
        ny -= 1         
    elif move == DOWN:
        ny += 1
    elif move == LEFT:
        nx -= 1
    elif move == RIGHT:
        nx += 1
        
    if game_map[ny][nx] == 1:
        move = STOP    
        return snake, move

    for i in range(1, len(snake)):
        if snake[i][0] == nx and snake[i][1] == ny:
            move = STOP
            return snake, move
            
    for i in range(len(snake) - 1, 0, -1):
        snake[i][0] = snake[i - 1][0]
        snake[i][1] = snake[i - 1][1]        

    if move == UP:
        snake[0][1] -= 1
    elif move == DOWN:
        snake[0][1] += 1
    elif move == LEFT:
        snake[0][0] -= 1
    elif move == RIGHT:
        snake[0][0] += 1
    return snake, move

def getCountCandys(gm):
    """ Фукнция вернёт количество кэнди на карте gm. """
    count = 0

    for i in range(len(gm)):
        for j in range(len(gm[i])):
            if gm[i][j] == 2 or gm[i][j] == 8:
                count += 1
                
    return count

def is_letter(word, x, y):
    """Функция проверяет, съедает ли змейка букву.
    Если съедает, то отмечает букву и возвращает True.
    """
    global num_letter
    n = 0           # Номер буквы в слове
    i = 0
    letter = ""     # Буква, на которую наехала змейка
    
    while i < len(word):    
        if x == word[i][1] and y == word[i][2] and not word[i][3]:
            letter = word[i][0]
            n = i
            i = len(word)
        i += 1
    
    if n == num_letter or letter == word[num_letter][0]:
        word[n][3] = True
        return True
    elif letter != "":
        num_letter = 1
        for i in range(1, len(word)):
            word[i][3] = False
        
    return False
    


# Инициализация pygame и настройки окна
pygame.init()

word_font = pygame.font.Font("font/chava.ttf", 32)
medium_font = pygame.font.Font("font/chava.ttf", 16)
little_font = pygame.font.Font("font/chava.ttf", 13)

# Настройка ширины и высоты окнa
size = [WIDTH, HEIGHT]

# Установка заголовка окна
pygame.display.set_caption("Змейка-буквоед")

# Инициализация сцены и установка размера
scene = pygame.display.set_mode(size)

# Для работы с задержкой и организации FPS
clock = pygame.time.Clock()


# ГЛАВНЫЙ ЦИКЛ ИГРЫ
while (playGame):

    if GAME_STATE == MENU:
        playGame, select_menu, GAMEMODE = menu(pygame, scene, word_font, medium_font, clock, FPS)
        if (select_menu > 0):
            pygame.event.clear()
            GAME_STATE = RESTART

    elif GAME_STATE == RESTART:
        num_letter = 1              # Активная буква - нулевая в слове
        count_candy = 0             # Количество леденцов на карте
        word_complete = False       # Собрано ли слово полностью?
        badger_position = []
        
        if level == 1:                       
            game_map = Level01()

            word = Word01()                         # Получаем слово для карты
            # + медоеды
            badger_position = getBagerPositions()
            level_candy = getCountCandys(game_map)  # Получаем количество леденцов на карте

            snake = [[16, 4],                       # Местоположение змейки
                     [17, 4],
                     [18, 4],
                     [19, 4],
                     [20, 4],
                     [21, 4],
                     [22, 4]]

        if level == 2:            
            game_map = Level02()
            word = Word02()
            # + медоеды
            badger_position = getBagerPositions()
            level_candy = getCountCandys(game_map)
            snake = [[16, 4],
                     [17, 4],
                     [18, 4]]
            
        if level == 3:
            game_map = Level03()
            word = Word03()
            # + медоеды
            badger_position = getBagerPositions()
            level_bush_c = 10
            level_candy = getCountCandys(game_map)
            snake = [[13, 4],
                     [14, 4],
                     [15, 4]]

        if level == 4:
            game_map = Level04()
            word = Word04()
            # + медоеды
            badger_position = getBagerPositions()
            level_bush_c = 6
            level_candy = getCountCandys(game_map)
            snake = [[1, 17],
                     [1, 18]]

        if level == 5:
            game_map = Level05()
            word = Word05()
            # + медоеды
            badger_position = getBagerPositions()
            level_candy = getCountCandys(game_map)
            snake = [[8, 15],
                     [8, 16]]

        if level == 6:
            game_map = Level06()
            # + медоеды
            badger_position = getBagerPositions()

            word = Word06()
            level_bush_c = 4
            level_candy = getCountCandys(game_map)
            snake = [[32, 10],
                     [33, 10]]

        if level == 7:
            game_map = Level07()
            word = Word07()
            # + медоеды
            badger_position = getBagerPositions()
            level_bush_c = 2
            level_candy = getCountCandys(game_map)
            snake = [[28, 4],
                     [28, 3]]
        pygame.event.clear()
        GAME_STATE = SCREEN_SAVER

    # ЭКРАННАЯ ЗАСТАВКА ПЕРЕД УРОВНЕМ
    elif GAME_STATE == SCREEN_SAVER:
        playGame, GAME_STATE = screen_saver(pygame, scene, GAMEMODE, word_font, level, word, clock, FPS)

    # ЭКРАННАЯ ЗАСТАВКА ПРИ ПОРАЖЕНИИ
    elif GAME_STATE == NEXT_TRY:
        if (count_frame > 180):
            playGame, GAME_STATE = next_try(pygame, scene, GAMEMODE, word_font, level, word, clock, FPS)
            count_frame = 200
        else:
            scene.fill(BLACK)
            draw_snake(scene, move, snake)
            draw_brick()
            draw_vacuum_cleaner()
            draw_text(scene)
            pygame.display.flip()

    elif GAME_STATE == ENDGAME:
        if (count_frame > 180):
            playGame, GAME_STATE = endgame(pygame, scene, GAMEMODE, word_font, level, word, clock, FPS)
            count_frame = 200
        else:
            scene.fill(BLACK)
            draw_snake(scene, move, snake)
            draw_brick()
            draw_vacuum_cleaner()
            draw_text(scene)
            pygame.display.flip()

    elif GAME_STATE == PLAY:
        # Проверяем нажатые клавиши
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                playGame = False
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    playGame = False
                elif (event.key == pygame.K_LEFT):
                    if move != RIGHT:
                        move = LEFT
                elif (event.key == pygame.K_RIGHT):
                    if move != LEFT:
                        move = RIGHT
                elif (event.key == pygame.K_UP):
                    if move != DOWN:
                        move = UP
                elif (event.key == pygame.K_DOWN):
                    if move != UP:
                        move = DOWN
    
        # Очищаем сцену
        scene.fill(BLACK)

        # Выводим изображение карты
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                SQUARE = game_map[i][j]
                if SQUARE == BRICK:
                    scene.blit(brick, (j * 32, i * 32))
                elif SQUARE == 2:
                    scene.blit(candy, (j * 32, i * 32))
                elif SQUARE == PORTAL:
                    if level_candy == count_candy and word_complete == True:
                        scene.blit(portal, (j * 32, i * 32))
                elif SQUARE == SQUARE_APPEND_SNAKE:
                    scene.blit(i_dont_no, (j * 32, i * 32))        
                elif SQUARE == SQUARE_REMOVE_SNAKE:
                    scene.blit(i_dont_no_brr, (j * 32, i * 32))
                elif SQUARE == 7:
                    scene.blit(agi, (j * 32, i * 32))
                elif SQUARE == 8:
                    scene.blit(bush_c, (j * 32, i * 32))

                # Выводить ли номера клеток? (настраивается в setup)
                if (viewNumberSquare):
                    txt = little_font.render(f"{SQUARE}", True, (0, 0, 0))
                    scene.blit(txt, (j * 32 + 13, i * 32 + 9))
                    txt = little_font.render(f"{SQUARE}", True, (200, 200, 128))
                    scene.blit(txt, (j * 32 + 12, i * 32 + 8))


        # Рисование змеи
        draw_snake(scene, move, snake)

        # Выводим траву     
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] == 3:
                    scene.blit(bush, (j * 32, i * 32))
                    
        # Выводим буквы
        for i in range(1, len(word)):
            # Если буква НЕ СОБРАНА, то рисуем её
            if word[i][3] == False:
                txt = word_font.render(word[i][0], True, (255, 255, 0))
                scene.blit(txt, (word[i][1] * 32 + 3, word[i][2] * 32 - 3))

        # Выводим пылесосы
        draw_vacuum_cleaner()

        # Выводим сообщения поверх всего остального
        draw_text(scene)
        
            
        # Отрисовываем изображения
        pygame.display.flip()

        # Расчёты:
        SQUARE = game_map[snake[0][1]][snake[0][0]]
        if SQUARE == SQUARE_APPEND_SNAKE:
            snake.append([snake[0][0], snake[0][1]])

        if check_candy(snake, game_map):
            count_candy += 1
            snake.append([snake[0][0], snake[0][1]])

        if check_bush_c(snake, game_map):
            count_candy += 1
            snake.append([snake[0][0], snake[0][1]])

        # Если количество конфет на уровне == собранным конфетам и слово собрано
        if level_candy == count_candy and word_complete:
            if check_portal(snake, game_map):
                level += 1
                GAME_STATE = RESTART


        # Двигаем медоедов при их наличии
        # Скорость регулируется в speed_snake // 2 - чем выше число в скобках, тем медленней
        # Если медоедов нет, то len(bager_position) будет равно 0, следовательно, цикл for не выполнится
        if (count_frame % (speed_snake * 1) == 0):
            for i in range(len(badger_position)):
                badger_position[i] = bagerMove(badger_position[i], game_map)

        # Определяет, съела ли змейка правильную букву
        if count_frame % speed_snake != 0:
            if not word_complete and is_letter(word, snake[0][0], snake[0][1]):
                snake.append([snake[0][0], snake[0][1]])  # Добавляет змее кусочек за собранную букву
                num_letter += 1  # Увеличивает номер буквы (надо собирать следующую)
                if num_letter == len(word):
                    word_complete = True

            # ---------------------------------------------------------------
            # Если змейке некуда идти
            if (no_move_snake(game_map)):
                count_frame = 0
                player_try -= 1
                move = STOP
                # Если нет попыток, то конец игры, иначе ещё одна попытка
                pygame.event.clear()
                if (player_try <= 0):
                    level = 1
                    GAME_STATE = ENDGAME
                else:
                    GAME_STATE = NEXT_TRY
            # ---------------------------------------------------------------


    # Задержка для синхронизации FPS
    clock.tick(FPS)
    count_frame += 1
    if count_frame > 100000:
        count_frame = 0    

# Конец истории
pygame.quit()
