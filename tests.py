"""
tests

This is file that contains methods that tests the software.
"""


# Imports
import unittest
from typing import List
from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver
from sudoku_gui import SudokuGui
from image_processing import get_sudoku_board_as_array_from_img
import constants


def test_function(arg_img_path: str, arg_initialized_numbers_in_sudoku_by_order: List[int]) -> SudokuBoard:
    try:
        sudoku_board_as_numbers_array = get_sudoku_board_as_array_from_img(arg_img_path,
                                                                           arg_initialized_numbers_in_sudoku_by_order)
        sudoku_board = SudokuBoard(sudoku_board_as_numbers_array)
        sudoku_gui = SudokuGui(constants.WINDOW_SIZE, constants.AMOUNT_OF_CUBES_IN_AREA, constants.SCREEN_COLOR,
                               constants.LINE_COLOR)
        sudoku_solver = SudokuSolver(sudoku_board, sudoku_gui)
        sudoku_solver.solve_sudoku(arg_do_recursive_drawing=False)
        sudoku_gui.draw_sudoku_board(sudoku_board, arg_is_recursive_drawing=False)
        return sudoku_board
    except Exception as e:
        print("Error: ", e)


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        result = test_function('Data/sudoku_img_1.jpg', [8, 1, 9, 5, 8, 7, 1, 4, 9, 7, 6, 7, 1, 2, 5, 8, 6, 1, 7, 1, 5,
                                                         2, 9, 7, 4, 6, 8, 3, 9, 4, 3, 5, 8])
        expected_result = SudokuBoard([[8, 7, 2, 4, 1, 3, 5, 6, 9],
                                       [9, 5, 6, 8, 2, 7, 3, 1, 4],
                                       [1, 3, 4, 6, 9, 5, 7, 8, 2],
                                       [4, 6, 9, 7, 3, 1, 8, 2, 5],
                                       [5, 2, 8, 9, 6, 4, 1, 3, 7],
                                       [7, 1, 3, 5, 8, 2, 4, 9, 6],
                                       [2, 9, 7, 1, 4, 8, 6, 5, 3],
                                       [6, 8, 5, 3, 7, 9, 2, 4, 1],
                                       [3, 4, 1, 2, 5, 6, 9, 7, 8]])
        self.assertEqual(expected_result, result)

    def test_example2(self):
        result = test_function('Data/sudoku_img_2.jpg', [1, 7, 2, 9, 8, 7, 4, 2, 4, 6, 5, 7, 9, 7, 1, 3, 4, 2, 8, 1, 6,
                                                         2, 3, 1, 6, 4, 5, 3, 8])
        expected_result = SudokuBoard([[5, 4, 1, 7, 3, 2, 9, 6, 8],
                                       [8, 7, 6, 1, 9, 5, 3, 4, 2],
                                       [3, 2, 9, 6, 4, 8, 1, 7, 5],
                                       [6, 1, 3, 2, 5, 4, 7, 8, 9],
                                       [7, 8, 5, 9, 1, 6, 4, 2, 3],
                                       [4, 9, 2, 3, 8, 7, 6, 5, 1],
                                       [9, 5, 7, 8, 6, 1, 2, 3, 4],
                                       [2, 3, 8, 4, 7, 9, 5, 1, 6],
                                       [1, 6, 4, 5, 2, 3, 8, 9, 7]])
        self.assertEqual(expected_result, result)

    def test_example3(self):
        result = test_function('Data/sudoku_img_3.jpg', [9, 6, 7, 3, 1, 4, 4, 1, 5, 3, 6, 8, 9, 6, 3, 1,
                                                         7, 1, 9, 4, 3, 1, 8, 9, 2, 7, 4, 4, 7])
        expected_result = SudokuBoard([[1, 5, 9, 8, 3, 4, 6, 7, 2],
                                       [7, 6, 3, 5, 9, 2, 1, 8, 4],
                                       [2, 8, 4, 7, 1, 6, 5, 9, 3],
                                       [3, 4, 1, 6, 7, 5, 8, 2, 9],
                                       [8, 9, 6, 2, 4, 3, 7, 1, 5],
                                       [5, 7, 2, 1, 8, 9, 3, 4, 6],
                                       [4, 2, 7, 3, 5, 1, 9, 6, 8],
                                       [6, 3, 8, 9, 2, 7, 4, 5, 1],
                                       [9, 1, 5, 4, 6, 8, 2, 3, 7]])
        self.assertEqual(expected_result, result)

    def test_example4(self):
        result = test_function('Data/sudoku_img_4.jpg', [9, 1, 4, 5, 9, 5, 1, 3, 2, 5, 9, 6, 7, 8, 4, 3,
                                                         2, 3, 6, 5, 8, 6, 2])
        expected_result = SudokuBoard([[9, 3, 8, 4, 7, 6, 1, 5, 2],
                                       [1, 4, 5, 2, 3, 9, 6, 7, 8],
                                       [6, 7, 2, 5, 8, 1, 4, 3, 9],
                                       [3, 6, 7, 1, 9, 2, 5, 8, 4],
                                       [2, 1, 4, 8, 5, 3, 9, 6, 7],
                                       [8, 5, 9, 6, 4, 7, 3, 2, 1],
                                       [7, 2, 1, 3, 6, 4, 8, 9, 5],
                                       [4, 8, 6, 9, 2, 5, 7, 1, 3],
                                       [5, 9, 3, 7, 1, 8, 2, 4, 6]])
        self.assertEqual(expected_result, result)

    def test_example5(self):
        result = test_function('Data/sudoku_img_5.jpg', [9, 2, 3, 5, 6, 6, 8, 8, 4, 9, 2, 1, 6, 1, 9, 4, 1, 7, 8, 5,
                                                         6, 1, 8, 1, 7, 2, 3, 9, 5, 7])
        expected_result = SudokuBoard([[8, 4, 9, 2, 1, 7, 3, 5, 6],
                                       [6, 1, 3, 5, 9, 4, 2, 8, 7],
                                       [2, 5, 7, 8, 3, 6, 9, 1, 4],
                                       [9, 8, 5, 6, 4, 2, 1, 7, 3],
                                       [7, 3, 6, 1, 8, 9, 4, 2, 5],
                                       [4, 2, 1, 7, 5, 3, 6, 9, 8],
                                       [5, 6, 2, 3, 7, 1, 8, 4, 9],
                                       [1, 7, 4, 9, 6, 8, 5, 3, 2],
                                       [3, 9, 8, 4, 2, 5, 7, 6, 1]])
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
