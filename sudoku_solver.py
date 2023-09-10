"""
sudoku_solver

This is file that handles SudokuSolver.
"""


# Imports
from sudoku_board import SudokuBoard, SudokuCube
from sudoku_gui import SudokuGui
import copy
from typing import Tuple
import time
import pygame
import constants


class SudokuSolver:
    """
    Sudoku Cube class

    This class represents a Sudoku Cube. It provides methods for handle cubes of sudoku.

    Attributes:
        __sudoku_board (SudokuBoard): The sudoku board.
        __sudoku_gui (SudokuGui): The sudoku GUI. This is enable to us to represent the sudoku in GUI.

    Methods:
        __init__(self, arg_sudoku_board: SudokuBoard, arg_sudoku_gui: SudokuGui) -> None: Initializes a new Sudoku Solver.
        This method not copy the arg_sudoku_board, and __sudoku_board will be equal in reference to arg_sudoku_board.
        solve_sudoku(self, arg_do_recursive_drawing: bool) -> None: Method that solve the __sudoku_board. This method changes the __sudoku_board
        and in the end the __sudoku_board will be solved sudoku board. The method can drawing the solving sudoku process(not the whole process but quickly)
        and represetns this in the GUI, if the user want.

    Usage:
        Solve the sudoku.
        Example:
            sudoku_solver = SudokuSolver(sudoku_board, sudoku_gui)
            sudoku_solver.solve_sudoku(arg_do_recursive_drawing=False)
    """
    def __init__(self, arg_sudoku_board: SudokuBoard, arg_sudoku_gui: SudokuGui) -> None:
        self.__sudoku_board = arg_sudoku_board
        self.__sudoku_gui = arg_sudoku_gui

    def solve_sudoku(self, arg_do_recursive_drawing: bool) -> None:
        self.__solve_sudoku_rec(((constants.INDEX_OF_FIRST_ROW_IN_SUDOKU_BOARD,constants.INDEX_OF_FIRST_COL_IN_SUDOKU_BOARD),
                               (constants.INDEX_OF_LAST_ROW_IN_FIRST_AREA_IN_LINE,constants.INDEX_OF_FIRST_COL_IN_SUDOKU_BOARD)),
                              arg_row_index=constants.INDEX_OF_FIRST_ROW_IN_SUDOKU_BOARD, arg_col_index=constants.INDEX_OF_FIRST_COL_IN_SUDOKU_BOARD,
                              arg_amount_of_recursive_calls=0, arg_do_recursive_drawing=arg_do_recursive_drawing)

    def __solve_sudoku_rec(self, arg_area_indexes: Tuple[Tuple[int, int], Tuple[int, int]], arg_row_index: int, \
        arg_col_index: int, arg_amount_of_recursive_calls: int, arg_do_recursive_drawing: bool) -> bool:
        result = False
        current_cube = self.__sudoku_board.get_cube_in_board(arg_row_index, arg_col_index)
        if current_cube.get_value_of_sudoku_cube() == constants.EMPTY_CUBE:
            current_cube.set_value_of_sudoku_cube(constants.MIN_NON_EMPTY_VALUE_OF_SUDOKU_CUBE)
        elif not current_cube.is_an_initialized_sudoku_cube():
            current_cube.set_value_of_sudoku_cube(current_cube.get_value_of_sudoku_cube()+1)
        current_cube_value = current_cube.get_value_of_sudoku_cube()
        if not self.__sudoku_board.has_duplicates_of_value_in_area_or_row_or_col(current_cube_value, arg_area_indexes, arg_row_index, arg_col_index):
            if (arg_row_index, arg_col_index) == constants.INDEXES_OF_LAST_CUBE_IN_SUDOKU_BOARD: return True
            next_cube_indexes = self.__sudoku_board.get_next_cube_indexes(arg_area_indexes, arg_row_index, arg_col_index)
            result = self.__solve_sudoku_rec(next_cube_indexes[constants.CUBE_AREA_INDEXES], next_cube_indexes[constants.CUBE_ROW_INDEX],
                                           next_cube_indexes[constants.CUBE_COL_INDEX], arg_amount_of_recursive_calls+1, arg_do_recursive_drawing)
        self.__draw_solving_sudoku_process(arg_do_recursive_drawing, arg_amount_of_recursive_calls)
        if result is False:
            if current_cube_value < constants.MAX_LEGAL_VALUE_OF_SUDOKU_CUBE and not current_cube.is_an_initialized_sudoku_cube():
                return self.__solve_sudoku_rec(arg_area_indexes, arg_row_index, arg_col_index, arg_amount_of_recursive_calls+1, arg_do_recursive_drawing)
            current_cube.set_value_of_sudoku_cube(constants.EMPTY_CUBE_VALUE) if not current_cube.is_an_initialized_sudoku_cube() else None
            return False
        return True

    def __draw_solving_sudoku_process(self, arg_do_recursive_drawing: bool, arg_amount_of_recursive_calls: int) -> None:
        if (arg_do_recursive_drawing and arg_amount_of_recursive_calls % constants.THE_DRAWING_RATE_OF_THE_SUDOKU_SOLVING_PROCESS == 0):
            self.__sudoku_gui.draw(self.__sudoku_board, arg_is_recursive_drawing=True)
