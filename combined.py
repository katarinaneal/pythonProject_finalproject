from Board import Board
from sudoku_generator import SudokuGenerator, generate_sudoku


def valid_in_row(row, num):
    for i in range(9):
        if Board.game[row-1][i] == num:
            return False
            break
    return True


def valid_in_col(col, num):
    for j in range(9):
        if Board.game[j][col - 1] == num:
            return False
            break
    return True


def valid_in_box(row_start, col_start, num):
    for i in range(3):
        for j in range(3):
            if Board.game[row_start + i][col_start + j] == num:
                return False
    return True

flag = 0
while flag != 4:
    if flag == 0:
      print('Welcome to Sudoku!')
      print()
      print('1. Easy\n2. Medium\n3. Hard')
      user = input('Please select a difficulty: ')
      if user == '1':
          difficulty = 'easy'
      elif user == '2':
          difficulty = 'medium'
      elif user == '3':
          difficulty = 'hard'
      try:
          sudoku_board = Board(9, 9, difficulty)
          flag = 1
      except:
          print('Invalid selection. Please try again.\n')
    elif flag == 1:
        sudoku_board.draw()
        print('Select one of the options below:')
        print('1. Insert cell value')
        print('2. Reset')
        print('3. Restart')
        print('4. Exit')
        user = input()
        if user == '1':
            print('\nPlease select a cell to change:')
            row = int(input('Row number: '))
            col = int(input('Column number: '))
            if 0 < row < 10 and 0 < col < 10:
              if Board.game[row-1][col-1] != 0:
                  print('Error: Filled cell values cannot be changed')
              else:
                  value = -1
                  while 0 > value or value > 9:
                      print('What value would you like to input? ')
                      value = int(input())
                      if 0 <= value <= 9:
                          sudoku_board.insert_cell(row, col, value)
                      else:
                          print('Please select a value between 1 and 9.')
            else:
              print("Error: Invalid row or column number. Please Try again")
            if sudoku_board.board_full() == True:
                  for x in range(9):
                      for y in range(9):
                          if valid_in_row(x, Board.game[x][y]) is False or valid_in_col(y, Board.game[x][y]) is False or\
                                  valid_in_box(x, y, Board.game[x][y]) is False:
                              flag = 3
                          else:
                              flag = 2
        elif user == '2':
            pass
        elif user == '3':
            flag = 0
        elif user == '4':
            print('Thanks for playing Sudoku! Goodbye!')
            flag = 4


    elif flag == 2:
        print("Congratulations! You win!")
        flag == 4

    elif flag == 3:
        print("Sudoku Failed!")
        print('''Would you like to restart?
        1. Yes
        2. No''')
        user = int(input())
        if user == 1:
            flag = 0
        elif user == 2:
            flag = 4



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
