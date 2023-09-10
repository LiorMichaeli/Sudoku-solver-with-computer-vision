"""
sudoku_board

This is file that handles sudoku board and sudoku cubes.
"""


# Imports
from typing import Tuple, List
import constants
from errors import Errors


class SudokuCube:
    """
    Sudoku Cube class

    This class represents a Sudoku Cube. It provides methods for handle cubes of sudoku.

    Attributes:
        __value (int): The value of sudoku cube.
        __is_an_initialized_sudoku_cube (bool): Represents if the sudoku cube was initialized from the beginning by the user.

    Methods:
        __init__(self, arg_value: int, arg_is_an_initialized_cube: bool) -> None: Initializes a new Sudoku cube.
        set_value_of_sudoku_cube(self, arg_value: int) -> None: Sets the value of the sudoku cube.
        is_an_initialized_sudoku_cube(self) -> bool: Retrieves whether the sudoku cube was initialized from the beginning by the user.
        get_value_of_sudoku_cube(self) -> int: Retrieves the value of a cube.
        __eq__(self, other): Checks if the values of cubes of two sudoku boards is equal.
         If they are equal the method will return true, else false.

    Usage:
        Create cubes while create sudoku board obj.
        Example:
            sudoku_cube = SudokuCube(arg_value=arg_starter_sudoku_board[row_index][col_index], arg_is_an_initialized_cube=True)
            current_row_of_cubes_in_sudoku_board.append(sudoku_cube)
    """
    def __init__(self, arg_value: int, arg_is_an_initialized_cube: bool) -> None:
        self.__value = constants.EMPTY_CUBE_VALUE
        self.set_value_of_sudoku_cube(arg_value)
        self.__is_an_initialized_sudoku_cube = arg_is_an_initialized_cube

    def get_value_of_sudoku_cube(self) -> int:
        return self.__value

    def is_an_initialized_sudoku_cube(self) -> bool:
        return self.__is_an_initialized_sudoku_cube

    def set_value_of_sudoku_cube(self, arg_value: int) -> None:
        """
         Sets the value of the sudoku cube. The method checks if the value is legal. The value need be integer between 0 and 9.
         :exception Illegal value: If the value is illegal, so the method will raise an exception with the appropriate error msg.
         :param arg_value:
        """
        if self.__is_valid_value_of_sudoku_cube(arg_value):
            self.__value = arg_value
        else:
            raise Exception(Errors.ILLEGAL_VALUE_OF_SUDOKU_CUBE.value)

    @staticmethod
    def __is_valid_value_of_sudoku_cube(arg_value: int) -> bool:
        return True if (constants.MIN_LEGAL_VALUE_OF_SUDOKU_CUBE <= arg_value <= constants.MAX_LEGAL_VALUE_OF_SUDOKU_CUBE) else False


class SudokuBoard:
    """
        Sudoku Board class

        This class represents a Sudoku Board. It provides methods for handle Sudoku Board.

        Attributes:
            __sudoku_board_cubes (2D list of SudokuCube): Contains the cubes of the sudoku board by order from left to
             right and top to bottom.

        Methods:
            __init__(self, arg_starter_sudoku_board: list) -> None: Initializes a new Sudoku Board.
            get_cube_in_board(self, arg_row_index: int, arg_col_index: int) -> SudokuCube: Retrieves the cube in the appropriate indexes.
            get_next_cube_indexes(arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]], arg_row_index: int, arg_col_index: int):
             Retrieves the indexes of the next cube according the given indexes that represents cube.
            has_duplicates_of_value_in_area_or_row_or_col(self, arg_current_cube_value: int,
             arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]],
              arg_row_index: int, arg_col_index: int) -> bool: Retrieves whether there are duplicates of given value
              in area or row or col according the given indexes.

        Usage:
            Create Sudoku board obj.
            Example:
                sudoku_board = SudokuBoard(starter_sudoku_board)
            In sudoku solving process, we need to check if the moves that the algoritem does are legal moves,
             that mean there are not duplicates of given value in area or row or col of the current cube.
            Example:
                sudoku_board.has_duplicates_of_value_in_area_or_row_or_col(current_cube_value, area_indexes, row_index, col_index)
        """
    def __init__(self, arg_starter_sudoku_board: List[List[int]]) -> None:
        self.__sudoku_board_cubes = []
        for row_index in range(constants.NUMBER_OF_ROWS_IN_SUDOKU_BOARD):
            current_row_of_cubes_in_sudoku_board = []
            for col_index in range(constants.NUMBER_OF_COLS_IN_SUDOKU_BOARD):
                if arg_starter_sudoku_board[row_index][col_index] != constants.EMPTY_CUBE_VALUE:
                    sudoku_cube = SudokuCube(arg_value=arg_starter_sudoku_board[row_index][col_index],
                                             arg_is_an_initialized_cube=True)
                else:
                    sudoku_cube = SudokuCube(arg_value=arg_starter_sudoku_board[row_index][col_index],
                                             arg_is_an_initialized_cube=False)
                current_row_of_cubes_in_sudoku_board.append(sudoku_cube)
            self.__sudoku_board_cubes.append(current_row_of_cubes_in_sudoku_board)

    def get_cube_in_board(self, arg_row_index: int, arg_col_index: int) -> SudokuCube:
        return self.__sudoku_board_cubes[arg_row_index][arg_col_index]

    @staticmethod
    def get_next_cube_indexes(arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]],
                              arg_row_index: int, arg_col_index: int):
        '''
        This is a method that gets indexes of cube and returns indexes of the next cube.
        :param arg_area_indexes:
        :param arg_row_index:
        :param arg_col_index:
        :return: Returns indexes of the next cube. If the cube is not the last cube in his area so the method will return
         the next cube in his area. Else if the cube is not equal to the last cube in the sudoku board
         (his indexes are not equal to (8,8)) so the method will return the first cube in the next area.
          Else the method will return None.
        '''
        if arg_row_index == arg_area_indexes[constants.LAST_CUBE_IN_AREA][constants.ROW_INDEX]\
                and arg_col_index == arg_area_indexes[constants.LAST_CUBE_IN_AREA][constants.COL_INDEX]:
            if (arg_row_index, arg_col_index) == constants.INDEXES_OF_LAST_CUBE_IN_SUDOKU_BOARD:
                return None
            elif arg_col_index == constants.INDEX_OF_LAST_COL_IN_SUDOKU_BOARD:
                # Return the indexes of the first cube in the next line of cubes.
                return ((arg_row_index+1, constants.INDEX_OF_FIRST_COL_IN_SUDOKU_BOARD),
                        (arg_row_index+constants.SIZE_OF_CUBE, constants.INDEX_OF_LAST_COL_IN_FIRST_AREA_IN_LINE)),\
                       arg_row_index+1, constants.INDEX_OF_FIRST_COL_IN_SUDOKU_BOARD
            else:
                # Return the indexes of the first cube in the next area in current line of cubes
                return ((arg_area_indexes[constants.FIRST_CUBE_IN_AREA][constants.ROW_INDEX], arg_col_index+1),
                        (arg_row_index, arg_col_index + constants.SIZE_OF_CUBE)),\
                       arg_area_indexes[constants.FIRST_CUBE_IN_AREA][constants.ROW_INDEX], arg_col_index+1
        if arg_col_index == arg_area_indexes[constants.LAST_CUBE_IN_AREA][constants.COL_INDEX]:
            return arg_area_indexes, arg_row_index+1, arg_area_indexes[constants.FIRST_CUBE_IN_AREA][constants.COL_INDEX]
        return arg_area_indexes, arg_row_index, arg_col_index+1

    def has_duplicates_of_value_in_area_or_row_or_col(self, arg_current_cube_value: int,
                                                      arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]],
                                                      arg_row_index: int, arg_col_index: int) -> bool:
        if self.__has_duplicates_of_value_in_area(arg_current_cube_value, arg_area_indexes) \
            or self.__has_duplicates_of_value_in_row(arg_current_cube_value, arg_row_index) \
                or self.__has_duplicates_of_value_in_col(arg_current_cube_value, arg_col_index):
            return True
        return False

    def __has_duplicates_of_value_in_area(self, arg_current_cube_value: int,
                                          arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:
        amount_of_cubes_with_matching_value = 0
        for row_index in range(arg_area_indexes[constants.FIRST_CUBE_IN_AREA][constants.ROW_INDEX],
                               arg_area_indexes[constants.LAST_CUBE_IN_AREA][constants.ROW_INDEX]+1):
            for col_index in range(arg_area_indexes[constants.FIRST_CUBE_IN_AREA][constants.COL_INDEX],
                                   arg_area_indexes[constants.LAST_CUBE_IN_AREA][constants.COL_INDEX]+1):
                current_cube = self.get_cube_in_board(row_index, col_index)
                current_cube_value = current_cube.get_value_of_sudoku_cube()
                amount_of_cubes_with_matching_value += 1 if current_cube_value == arg_current_cube_value else 0
                if amount_of_cubes_with_matching_value > constants.MAX_AMOUNT_OF_CUBES_WITH_THE_SAME_VALUE_IN_AREA:
                    return True
        return False

    def __has_duplicates_of_value_in_row(self, arg_current_cube_value: int, arg_row_index: int) -> bool:
        amount_of_cubes_with_matching_value = 0
        for col_index in range(constants.INDEX_OF_LAST_COL_IN_SUDOKU_BOARD+1):
            current_cube = self.get_cube_in_board(arg_row_index, col_index)
            current_cube_value = current_cube.get_value_of_sudoku_cube()
            amount_of_cubes_with_matching_value += 1 if current_cube_value == arg_current_cube_value else 0
            if amount_of_cubes_with_matching_value > constants.MAX_AMOUNT_OF_CUBES_WITH_THE_SAME_VALUE_IN_ROW:
                return True
        return False

    def __has_duplicates_of_value_in_col(self, arg_current_cube_value, arg_col_index: int) -> bool:
        amount_of_cubes_with_matching_value = 0
        for row_index in range(constants.INDEX_OF_LAST_ROW_IN_SUDOKU_BOARD+1):
            current_cube = self.get_cube_in_board(row_index, arg_col_index)
            current_cube_value = current_cube.get_value_of_sudoku_cube()
            amount_of_cubes_with_matching_value += 1 if current_cube_value == arg_current_cube_value else 0
            if amount_of_cubes_with_matching_value > constants.MAX_AMOUNT_OF_CUBES_WITH_THE_SAME_VALUE_IN_COL:
                return True
        return False

    # Override methods
    def __eq__(self, other):
        for row_index in range(constants.NUMBER_OF_ROWS_IN_SUDOKU_BOARD):
            for col_index in range(constants.NUMBER_OF_COLS_IN_SUDOKU_BOARD):
                cube_value = self.get_cube_in_board(row_index, col_index).get_value_of_sudoku_cube()
                other_cube_value = other.get_cube_in_board(row_index, col_index).get_value_of_sudoku_cube()
                if cube_value != other_cube_value:
                    return False
        return True
