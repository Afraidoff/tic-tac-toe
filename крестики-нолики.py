import time

import pygame, random

pygame.init()

width = 300
height = 300
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
fps = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("крестики-нолики")


def draw_grid():
    pygame.draw.line(screen, black, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, black, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, black, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, black, (0, 200), (300, 200), 3)


def draw_items():
    for x in range(3):
        for y in range(3):
            if field[x][y] == 'x':
                pygame.draw.line(screen, red, (y * 100 + 5, x * 100 + 5), (y * 100 + 95, x * 100 + 95), 3)
                pygame.draw.line(screen, red, (y * 100 + 95, x * 100 + 5), (y * 100 + 5, x * 100 + 95), 3)

            elif field[x][y] == '0':
                pygame.draw.circle(screen, blue, (y * 100 + 50, x * 100 + 50), 45, 3)


field = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]


# noinspection PyGlobalUndefined
def win_check(symbol):
    flag_win = False
    global win
    for i in field:
        if i.count(symbol) == 3:
            flag_win = True
            win = [[0, field.index(i)], [1, field.index(i)], [2, field.index(i)]]

    for column in range(3):
        if field[0][column] == field[1][column] == field[2][column] == symbol:
            flag_win = True
            win = [[column, 0], [column, 1], [column, 2]]

    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]

    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2, 0]]
    return flag_win


game_over = False

run_game = True
while run_game:
    screen.fill(white)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_position = pygame.mouse.get_pos()
            if field[mouse_position[1] // 100][mouse_position[0] // 100] == '':
                field[mouse_position[1] // 100][mouse_position[0] // 100] = 'x'
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                while field[x][y] != '':
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
                field[x][y] = '0'


        player = win_check('x')
        ai = win_check('0')
        result = \
            field[0].count('x') + \
            field[0].count('0') + \
            field[1].count('x') + \
            field[1].count('0') + \
            field[2].count('x') + \
            field[2].count('0')
        if player or ai:
            game_over = True
            if player:
                pygame.display.set_caption('Вы победили')
            elif ai:
                pygame.display.set_caption('Вы проиграли')
        elif result == 8:
            pygame.display.set_caption('Ничья')
            time.sleep(2)
            break
    if game_over:
        pygame.draw.rect(screen, green, (win[0][0] * 100, win[0][1] * 100, 100, 100))
        pygame.draw.rect(screen, green, (win[1][0] * 100, win[1][1] * 100, 100, 100))
        pygame.draw.rect(screen, green, (win[2][0] * 100, win[2][1] * 100, 100, 100))
    draw_grid()
    draw_items()
    win_check('x')

    pygame.display.flip()
pygame.quit()
