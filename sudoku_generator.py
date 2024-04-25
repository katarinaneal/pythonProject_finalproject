import math, random


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        for i in range(row_length):
            self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.box_length = int(math.sqrt(row_length))


    def get_board(self):
        return self.board


    def print_board(self):
        print(self.board)



    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True



    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True



    def valid_in_box(self, row_start, col_start, num):
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True


    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row//3*3, col//3*3, num)



    def fill_box(self, row_start, col_start):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(self.box_length):
            for j in range(self.box_length):
                y = random.randrange(len(values))
                self.board[row_start + i][col_start + j] = values[y]
                values.pop(y)



    def fill_diagonal(self):
        SudokuGenerator.fill_box(self, 0, 0)
        SudokuGenerator.fill_box(self, 3, 3)
        SudokuGenerator.fill_box(self, 6, 6)


    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False


    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


    def remove_cells(self):
        while self.removed_cells != 0:
            row = random.randrange(9)
            col = random.randrange(9)
            if self.board[row][col] == 0:
                pass
            else:
                self.board[row][col] = 0
                self.removed_cells -= 1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board