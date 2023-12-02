import pygame
import sys
import os
import random


class PuzzleGame:
    def __init__(self, width=300, height=300, rows=3, cols=3, puzzles_folder="puzzles"):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.tile_size = self.width // self.cols
        self.puzzles_folder = puzzles_folder

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Puzzle for EPITECH JAM 2023")

        self.load_random_image()
        self.create_pieces()
        self.shuffle_pieces()
        self.create_piece_positions()

        self.selected_piece = None
        self.selected_piece_index = None

    def load_random_image(self):
        image_files = [f for f in os.listdir(self.puzzles_folder) if
                       os.path.isfile(os.path.join(self.puzzles_folder, f))]
        random_image = os.path.join(self.puzzles_folder, random.choice(image_files))
        self.image = pygame.image.load(random_image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def create_pieces(self):
        self.pieces = []
        for row in range(self.rows):
            for col in range(self.cols):
                piece = self.image.subsurface(col * self.tile_size, row * self.tile_size, self.tile_size,
                                              self.tile_size)
                self.pieces.append(piece)

        self.original_pieces = self.pieces.copy()

    def shuffle_pieces(self):
        random.shuffle(self.pieces)

    def create_piece_positions(self):
        self.piece_positions = [(col * self.tile_size, row * self.tile_size) for row in range(self.rows) for col in
                                range(self.cols)]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_mouse_click(event.pos)

    def handle_mouse_click(self, pos):
        mouse_x, mouse_y = pos
        clicked_row = mouse_y // self.tile_size
        clicked_col = mouse_x // self.tile_size

        if self.selected_piece is None:
            self.selected_piece = self.pieces[clicked_row * self.cols + clicked_col]
            self.selected_piece_index = clicked_row * self.cols + clicked_col
        else:
            self.pieces[self.selected_piece_index], self.pieces[clicked_row * self.cols + clicked_col] = \
                self.pieces[clicked_row * self.cols + clicked_col], self.selected_piece
            self.selected_piece = None

    def draw(self):
        self.screen.fill((0, 0, 0))
        for i, piece in enumerate(self.pieces):
            row, col = i // self.cols, i % self.cols
            self.screen.blit(piece, self.piece_positions[i])

        if self.pieces == self.original_pieces:
            pygame.quit()
            sys.exit()

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
