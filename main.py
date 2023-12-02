import pygame
import sys

pygame.init()

width, height = 600, 600
cell_height = 200
line_height = 5
object_width = 8

background_color = (179, 143, 242)

line_color = (255, 182, 232)

player_color1 = (248, 125, 110)
player_color2 = (183, 245, 200)

window = pygame.display.set_mode((width, height))
window.fill(background_color)
pygame.display.set_caption("Morpion game for EPITECH JAM 2023")


def draw_grill():
    pygame.draw.line(window, line_color, (0, cell_height), (width, cell_height), line_height)
    pygame.draw.line(window, line_color, (0, 2 * cell_height), (width, 2 * cell_height), line_height)

    pygame.draw.line(window, line_color, (cell_height, 0), (cell_height, height), line_height)
    pygame.draw.line(window, line_color, (2 * cell_height, 0), (2 * cell_height, height), line_height)


def draw_x(x, y):
    x_pos = x * cell_height + cell_height // 2
    y_pos = y * cell_height + cell_height // 2
    rayon = cell_height // 2 - 20
    pygame.draw.line(window, player_color1, (x_pos - rayon, y_pos - rayon), (x_pos + rayon, y_pos + rayon), object_width)
    pygame.draw.line(window, player_color1, (x_pos + rayon, y_pos - rayon), (x_pos - rayon, y_pos + rayon), object_width)


def draw_o(x, y):
    x_pos = x * cell_height + cell_height // 2
    y_pos = y * cell_height + cell_height // 2
    rayon = cell_height // 2 - 20
    pygame.draw.circle(window, player_color2, (x_pos, y_pos), rayon, object_width)


def victory_check(grill, player):
    for i in range(3):
        if all(grill[i][j] == player for j in range(3)):
            return True
        if all(grill[j][i] == player for j in range(3)):
            return True

    if all(grill[i][i] == player for i in range(3)):
        return True
    if all(grill[i][2 - i] == player for i in range(3)):
        return True

    return False


def morpion_game():
    grill = [[None, None, None], [None, None, None], [None, None, None]]
    actual_player = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0] // cell_height
                y = event.pos[1] // cell_height

                if grill[y][x] is None:
                    if actual_player == 1:
                        grill[y][x] = 'X'
                        draw_x(x, y)
                        actual_player = 2
                    else:
                        grill[y][x] = 'O'
                        draw_o(x, y)
                        actual_player = 1

                    if victory_check(grill, 'X'):
                        print("player 1 won!")
                        return
                    elif victory_check(grill, 'O'):
                        print("player 2 won!")
                        return

                    if all(grill[i][j] is not None for i in range(3) for j in range(3)):
                        print("Match nul!")
                        return

        draw_grill()
        pygame.display.flip()


morpion_game()
