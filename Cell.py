class Cell:


    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col


    def set_cell_value(self, value):
        self.value = value