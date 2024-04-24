import sys

import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Sudoko")


from sudoko import *


board = initialize_board()
board[][]= ' '


#draw the grid
def draw_grid():
    #draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR
            (0, i*SQUARE_SIZE),
            LINE_WIDTH
        )
    #draw vertitcal lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i *SQUARE_SIZE, HEIGHT)
            LINE_WIDTH
        )



def draw_chips():
    chip_x_surf = chip_front.render("X", 0, CROSS_COLOR)
    chip_x_rect = chip_x_surf.get_rect(center = (300,300))
    screen.blit(chip_x_surf, chip_x_rect)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



