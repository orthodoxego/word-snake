# Подключаем pygame
import pygame
from setup import *
from maps import *
def check_candy(snake, game_map):
    """ Возвращает True когда змейка ест конфету. """
    if game_map[snake[0][1]][snake[0][0]] == 2:
        game_map[snake[0][1]][snake[0][0]] = 0
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
            if gm[i][j] == 2:
                count += 1
                
    return count

def is_letter(word, x, y):
    global num_letter
    # Функция проверяет, съедает ли змейка букву
    n = 0
    i = 1    
    letter = ""
    
    while i < len(word):    
        if x == word[i][1] and y == word[i][2] and word[i][3] == False:
            letter = word[i][0]
            n = i
            i = len(word)
        i += 1
    
    if n == num_letter:        
        word[n][3] = True
        return True
    else:
        if letter != "":
            num_letter = 1
            for i in range(1, len(word)):
                word[i][3] = False
        
    return False
    


# Инициализация pygame и настройки окна
pygame.init()
word_font = pygame.font.Font("font/chava.ttf", 32)

# Настройка ширины и высоты окнa
size = [WIDTH, HEIGHT]

# Установка заголовка окна
pygame.display.set_caption("Шаблон pygame")

# Инициализация сцены и установка размера
scene = pygame.display.set_mode(size)

# Для работы с задержкой и организации FPS
clock = pygame.time.Clock()


# ГЛАВНЫЙ ЦИКЛ ИГРЫ
while (playGame):

    if GAME_STATE == RESTART:
        # Игрок должен собрать сначала ПЕРВУЮ букву
        num_letter = 1
        count_candy = 0
        word_complete = False
        
        if level == 1:                       
            game_map = Level01()

            # Получаем слово для карты
            word = Word01()                        
            
            level_candy = getCountCandys(game_map)
            snake = [[16, 4],
                     [17, 4],
                     [18, 4],
                     [19, 4],
                     [20, 4],
                     [21, 4],
                     [22, 4]]

        if level == 2:            
            game_map = Level02()
            word = Word02()             
            level_candy = getCountCandys(game_map)
            snake = [[16, 4],
                     [17, 4],
                     [18, 4]]
            
        if level == 3:
            game_map = Level03()
            word = Word03() 
            level_candy = getCountCandys(game_map)
            snake = [[16, 4],
                     [17, 4],
                     [18, 4]]


        print(f"Количество кэнди на уровне {level} = {level_candy}")
        GAME_STATE = PLAY 

    if GAME_STATE == PLAY:
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
                if game_map[i][j] == 1:
                    scene.blit(brick, (j * 32, i * 32))
                elif game_map[i][j] == 2:
                    scene.blit(candy, (j * 32, i * 32))
                elif game_map[i][j] == 4:
                    if level_candy == count_candy and word_complete == True:
                        scene.blit(portal, (j * 32, i * 32))
                elif game_map[i][j] == 5:
                    scene.blit(i_dont_no, (j * 32, i * 32))        
                elif game_map[i][j] == 6:
                    scene.blit(i_dont_no_brr, (j * 32, i * 32))
                elif game_map[i][j] == 7:
                    scene.blit(agi, (j * 32, i * 32))
        txt = word_font.render(word[0][1], True, (255, 255, 255))
        scene.blit(txt, (WIDTH - word_font.size(word[0][1])[0], 0))
                    
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
        
            
        # Отрисовываем изображения
        pygame.display.flip()

        # Расчёты:
        if game_map[snake[0][1]][snake[0][0]] == 5:
            snake.append([snake[0][0], snake[0][1]])
        if check_candy(snake, game_map):
            count_candy += 1
            snake.append([snake[0][0], snake[0][1]])    
        if level_candy == count_candy:
            if check_portal(snake, game_map):
                level += 1
                GAME_STATE = RESTART

        # Находим букву
        if count_frame % speed_snake != 0:
            if word_complete == False and is_letter(word, snake[0][0], snake[0][1]):
                # Добавляет змее кусочек за собранную букву
                snake.append([snake[0][0], snake[0][1]])
                num_letter += 1
                if num_letter == len(word):
                    word_complete = True
                
    # Задержка для синхронизации FPS
    clock.tick(FPS)
    count_frame += 1
    if count_frame > 1000:
        count_frame = 0    

# Конец истории
pygame.quit()
