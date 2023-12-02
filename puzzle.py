import pygame
import sys
import os
import random

pygame.init()

WIDTH, HEIGHT = 300, 300
ROWS, COLS = 3, 3
TILE_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Puzzle")

puzzles_folder = "puzzles"
image_files = [f for f in os.listdir(puzzles_folder) if os.path.isfile(os.path.join(puzzles_folder, f))]
random_image = os.path.join(puzzles_folder, random.choice(image_files))

image = pygame.image.load(random_image)
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

pieces = []
for row in range(ROWS):
    for col in range(COLS):
        piece = image.subsurface(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pieces.append(piece)

original_pieces = pieces.copy()

random.shuffle(pieces)

piece_positions = [(col * TILE_SIZE, row * TILE_SIZE) for row in range(ROWS) for col in range(COLS)]

selected_piece = None
selected_piece_index = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            clicked_row = mouse_y // TILE_SIZE
            clicked_col = mouse_x // TILE_SIZE

            if selected_piece is None:
                selected_piece = pieces[clicked_row * COLS + clicked_col]
                selected_piece_index = clicked_row * COLS + clicked_col
            else:
                pieces[selected_piece_index], pieces[clicked_row * COLS + clicked_col] = \
                    pieces[clicked_row * COLS + clicked_col], selected_piece
                selected_piece = None

    screen.fill(WHITE)
    for i, piece in enumerate(pieces):
        row, col = i // COLS, i % COLS
        screen.blit(piece, piece_positions[i])

    if pieces == original_pieces:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
