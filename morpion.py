import pygame
import sys


class MorpionGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.cell_height = 200
        self.line_height = 5
        self.object_width = 8
        self.background_color = (179, 143, 242)
        self.line_color = (255, 182, 232)
        self.player_color1 = (248, 125, 110)
        self.player_color2 = (183, 245, 200)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.background_color)
        pygame.display.set_caption("Morpion game for EPITECH JAM 2023")
        self.grill = [[None, None, None], [None, None, None], [None, None, None]]
        self.actual_player = 1

    def draw_grill(self):
        pygame.draw.line(self.window, self.line_color, (0, self.cell_height), (self.width, self.cell_height),
                         self.line_height)
        pygame.draw.line(self.window, self.line_color, (0, 2 * self.cell_height), (self.width, 2 * self.cell_height),
                         self.line_height)
        pygame.draw.line(self.window, self.line_color, (self.cell_height, 0), (self.cell_height, self.height),
                         self.line_height)
        pygame.draw.line(self.window, self.line_color, (2 * self.cell_height, 0), (2 * self.cell_height, self.height),
                         self.line_height)

    def draw_x(self, x, y):
        x_pos = x * self.cell_height + self.cell_height // 2
        y_pos = y * self.cell_height + self.cell_height // 2
        radius = self.cell_height // 2 - 20
        pygame.draw.line(self.window, self.player_color1, (x_pos - radius, y_pos - radius),
                         (x_pos + radius, y_pos + radius), self.object_width)
        pygame.draw.line(self.window, self.player_color1, (x_pos + radius, y_pos - radius),
                         (x_pos - radius, y_pos + radius), self.object_width)

    def draw_o(self, x, y):
        x_pos = x * self.cell_height + self.cell_height // 2
        y_pos = y * self.cell_height + self.cell_height // 2
        radius = self.cell_height // 2 - 20
        pygame.draw.circle(self.window, self.player_color2, (x_pos, y_pos), radius, self.object_width)

    def victory_check(self, player):
        for i in range(3):
            if all(self.grill[i][j] == player for j in range(3)):
                return True
            if all(self.grill[j][i] == player for j in range(3)):
                return True

        if all(self.grill[i][i] == player for i in range(3)):
            return True
        if all(self.grill[i][2 - i] == player for i in range(3)):
            return True

        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0] // self.cell_height
                    y = event.pos[1] // self.cell_height

                    if self.grill[y][x] is None:
                        if self.actual_player == 1:
                            self.grill[y][x] = 'X'
                            self.draw_x(x, y)
                            self.actual_player = 2
                        else:
                            self.grill[y][x] = 'O'
                            self.draw_o(x, y)
                            self.actual_player = 1

                        if self.victory_check('X'):
                            print("Player 1 won!")
                            return
                        elif self.victory_check('O'):
                            print("Player 2 won!")
                            return

                        if all(self.grill[i][j] is not None for i in range(3) for j in range(3)):
                            print("Match draw!")
                            return

            self.draw_grill()
            pygame.display.flip()
