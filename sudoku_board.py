
# Imports
from typing import Tuple


class SudokuBoard:
    def __init__(self, arg_starter_sudoku_board: list):
        self.__sudoku_cubes_board = []
        for row_index in range(9):
            current_row_of_cubes_in_sudoku_board = []
            for col_index in range(9):
                if arg_starter_sudoku_board[row_index][col_index]:
                    sudoku_cube = SudokuCube(arg_value=arg_starter_sudoku_board[row_index][col_index], arg_is_an_initialized_cube=True)
                else:
                    sudoku_cube = SudokuCube(arg_value=arg_starter_sudoku_board[row_index][col_index], arg_is_an_initialized_cube=False)
                current_row_of_cubes_in_sudoku_board.append(sudoku_cube)
            self.__sudoku_cubes_board.append(current_row_of_cubes_in_sudoku_board)

    def get_cube_in_board(self, arg_row_index: int, arg_col_index: int):
        return self.__sudoku_cubes_board[arg_row_index][arg_col_index]

    @staticmethod
    def get_next_cube_indexes(arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]], arg_row_index: int, arg_col_index: int):
        if arg_row_index == arg_area_indexes[1][0] and arg_col_index == arg_area_indexes[1][1]:
            if arg_col_index == 8 and arg_row_index == 8:
                return None
            elif arg_col_index == 8:
                return ((arg_row_index+1, 0), (arg_row_index+3, 2)), arg_row_index+1, 0
            else:
                return ((arg_area_indexes[0][0], arg_col_index+1), (arg_row_index, arg_col_index + 3)), arg_area_indexes[0][0], arg_col_index+1
        if arg_col_index == arg_area_indexes[1][1]:
            return arg_area_indexes, arg_row_index+1, arg_area_indexes[0][1]
        return arg_area_indexes, arg_row_index, arg_col_index+1
    def has_duplicates_of_value_in_area_or_row_or_col(self, arg_current_cube_value: int, arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]], arg_row_index: int, arg_col_index: int):
        if self.__has_duplicates_of_value_in_area(arg_current_cube_value, arg_area_indexes) \
            or self.__has_duplicates_of_value_in_row(arg_current_cube_value, arg_row_index) \
                or self.__has_duplicates_of_value_in_col(arg_current_cube_value, arg_col_index):
            return True
        return False

    def __has_duplicates_of_value_in_area(self, arg_current_cube_value: int, arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]]):
        amount_of_cubes_with_matching_value = 0
        for row_index in range(arg_area_indexes[0][0], arg_area_indexes[1][0]+1):
            for col_index in range(arg_area_indexes[0][1], arg_area_indexes[1][1]+1):
                current_cube = self.get_cube_in_board(row_index, col_index)
                current_cube_value = current_cube.get_value_of_sudoku_cube()
                amount_of_cubes_with_matching_value += 1 if current_cube_value == arg_current_cube_value else 0
                if amount_of_cubes_with_matching_value > 1:
                    return True
        return False

    def __has_duplicates_of_value_in_row(self, arg_current_cube_value: int, arg_row_index: int):
        amount_of_cubes_with_matching_value = 0
        for col_index in range(9):
            current_cube = self.get_cube_in_board(arg_row_index, col_index)
            current_cube_value = current_cube.get_value_of_sudoku_cube()
            amount_of_cubes_with_matching_value += 1 if current_cube_value == arg_current_cube_value else 0
            if amount_of_cubes_with_matching_value > 1:
                return True
        return False

    def __has_duplicates_of_value_in_col(self, arg_current_cube_value, arg_col_index: int):
        amount_of_cubes_with_matching_value = 0
        for row_index in range(9):
            current_cube = self.get_cube_in_board(row_index, arg_col_index)
            current_cube_value = current_cube.get_value_of_sudoku_cube()
            amount_of_cubes_with_matching_value += 1 if current_cube_value == arg_current_cube_value else 0
            if amount_of_cubes_with_matching_value > 1:
                return True
        return False

    def __str__(self):
        string = ""
        for row_index in range(9):
            for col_index in range(9):
                string += str(self.get_cube_in_board(row_index, col_index).get_value_of_sudoku_cube()) + ", "
            string += "\n"
        return string

class SudokuCube:
    def __init__(self, arg_value: int, arg_is_an_initialized_cube: bool):
        self.__value = 0
        self.set_value_of_sudoku_cube(arg_value)
        self.__is_an_initialized_sudoku_cube = arg_is_an_initialized_cube

    def get_value_of_sudoku_cube(self):
        return self.__value

    def is_an_initialized_sudoku_cube(self):
        return self.__is_an_initialized_sudoku_cube

    def set_value_of_sudoku_cube(self, arg_value: int):
        if self.__is_valid_value_of_sudoku_cube(arg_value):
            self.__value = arg_value
        #else:
            #raise Exception(I need to do exeptions enum)!!!!!!!!

    @staticmethod
    def __is_valid_value_of_sudoku_cube(arg_value: int):
        return True if (0 <= arg_value <= 9) else False
