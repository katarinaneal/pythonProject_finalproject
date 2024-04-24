#added board
import pygame
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 540, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
CELL_SIZE = WIDTH // 9

# Set up the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku")

# Load fonts
font = pygame.font.SysFont(None, 40)

# Sudoku board
board = [[0 for _ in range(9)] for _ in range(9)]


def draw_grid():
    for i in range(10):
        if i % 3 == 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thick)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thick)


def draw_numbers():
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = font.render(str(board[i][j]), True, BLACK)
                screen.blit(num, (j * CELL_SIZE + (CELL_SIZE // 2 - num.get_width() // 2),
                                  i * CELL_SIZE + (CELL_SIZE // 2 - num.get_height() // 2)))


def generate_board():
    # Generate a solved Sudoku board
    solve_sudoku(board)

    # Remove some numbers to create a puzzle
    empty_cells = random.sample([(i, j) for i in range(9) for j in range(9)], 40)
    for row, col in empty_cells:
        board[row][col] = 0


def is_valid(board, row, col, num):
    # Check if the number is already in the row
    if num in board[row]:
        return False

    # Check if the number is already in the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is already in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


# Main loop
def main():
    generate_board()
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid()
        draw_numbers()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
