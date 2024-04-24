from board import Board
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