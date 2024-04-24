from sudoku_generator import SudokuGenerator, generate_sudoku


class Board:
    game = []

    def __init__(self, width, height, difficulty):
        self.width = width
        self.height = height
        self.difficulty = difficulty
        if difficulty == 'easy':
            remove = 30
        elif difficulty == 'medium':
            remove = 40
        elif difficulty == 'hard':
            remove = 50
        self.original = tuple(generate_sudoku(width, 0))
        self.board = list(self.original)
        Board.game = self.board

    def get_board(self):
        return self.board

    def draw(self):
        for i in range(9):
            if i % 3 == 0:
                print('-----------------------------')
            for j in range(9):
                if self.board[i][j] == 0:
                    print('| |', end='')
                else:
                    print(f'|{self.board[i][j]}|', end='')
            print()

    def insert_cell(self, row, col, num):
        self.board[row - 1][col - 1] = num

    def clear_board(self):
        for row in range(self.width):
            for col in range(self.height):
                self.board[row][col] = 0

    def reset_board(self):
        print(self.original)

    def board_full(self):
        '''for row in range(9):
          if 0 in self.board[row]:
              return False
        return True'''
        count = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    count += 1
                else:
                    pass
        if count == 81:
            return True
        else:
            return False

    def find_empty(self, row, col):
        if self.board[row - 1][col - 1] != 0:
            return False
        else:
            return True

    def print(self):
        for i in range(self.width):
            if i % 3 == 0:
                print('-----------------------------')
            for j in range(self.height):
                if Board.game[i][j] == 0:
                    print('| |', end='')
                else:
                    print(f'|{Board.game[i][j]}|', end='')
            print()