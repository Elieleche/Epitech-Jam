import pygame
import sys


class Connect4:
    def __init__(self):
        pygame.init()

        self.row_count = 6
        self.column_count = 7
        self.square_size = 100
        self.radius = self.square_size // 2 - 5
        self.width = self.column_count * self.square_size
        self.height = (self.row_count + 1) * self.square_size

        self.background_color = (179, 143, 242)
        self.line_color = (255, 182, 232)
        self.player_color1 = (248, 125, 110)
        self.player_color2 = (183, 245, 200)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect Four for EPITECH JAM 2023")

        self.board = self.create_board()
        self.turn = 1

    def create_board(self):
        return [[0] * self.column_count for _ in range(self.row_count)]

    def is_valid_location(self, col):
        return self.board[self.row_count - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.row_count):
            if self.board[r][col] == 0:
                return r

    def draw_board(self):
        for c in range(self.column_count):
            for r in range(self.row_count):
                pygame.draw.rect(self.screen, self.line_color,
                                 (c * self.square_size, (r + 1) * self.square_size, self.square_size, self.square_size))
                pygame.draw.circle(self.screen, self.background_color, (
                    c * self.square_size + self.square_size // 2, (r + 1) * self.square_size + self.square_size // 2),
                                   self.radius)

        for c in range(self.column_count):
            for r in range(self.row_count):
                if self.board[r][c] == 1:
                    pygame.draw.circle(
                        self.screen, self.player_color1, (c * self.square_size + self.square_size // 2,
                                                self.height - r * self.square_size - self.square_size // 2),
                        self.radius)
                elif self.board[r][c] == 2:
                    pygame.draw.circle(self.screen, self.player_color2, (c * self.square_size + self.square_size // 2,
                                                                  self.height - r * self.square_size - self.square_size // 2),
                                       self.radius)

    def check_winner(self, player):
        for r in range(self.row_count):
            for c in range(self.column_count - 3):
                if self.board[r][c] == player and self.board[r][c + 1] == player and self.board[r][c + 2] == player and \
                        self.board[r][c + 3] == player:
                    return True

        for r in range(self.row_count - 3):
            for c in range(self.column_count):
                if self.board[r][c] == player and self.board[r + 1][c] == player and self.board[r + 2][c] == player and \
                        self.board[r + 3][c] == player:
                    return True

        for r in range(self.row_count - 3):
            for c in range(self.column_count - 3):
                if self.board[r][c] == player and self.board[r + 1][c + 1] == player and self.board[r + 2][
                    c + 2] == player and self.board[r + 3][c + 3] == player:
                    return True

        for r in range(self.row_count - 3):
            for c in range(3, self.column_count):
                if self.board[r][c] == player and self.board[r + 1][c - 1] == player and self.board[r + 2][
                    c - 2] == player and self.board[r + 3][c - 3] == player:
                    return True

        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, self.background_color, (0, 0, self.width, self.square_size))
                    col = event.pos[0] // self.square_size
                    pygame.draw.circle(self.screen, self.player_color1 if self.turn == 1 else self.player_color2,
                                       (col * self.square_size + self.square_size // 2, self.square_size // 2),
                                       self.radius)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // self.square_size
                    if self.is_valid_location(col):
                        row = self.get_next_open_row(col)
                        self.board[row][col] = self.turn
                        self.turn = 3 - self.turn

            self.screen.fill(self.background_color)
            self.draw_board()
            pygame.display.flip()

            if self.check_winner(1):
                print("Player red won!")
                pygame.quit()
                sys.exit()
            elif self.check_winner(2):
                print("Player yellow won!")
                pygame.quit()
                sys.exit()
