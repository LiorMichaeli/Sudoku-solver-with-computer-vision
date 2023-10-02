"""
sudoku_solver_app

This is file that contains main method that handle the software.
"""

# Imports
from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver
from sudoku_gui import SudokuGui
from image_processing import get_sudoku_board_as_array_from_img
import sys
import constants

def main(list_of_args):
    try:
        # Get args from args list
        img_path_arg = list_of_args[constants.INDEX_OF_IMG_PATH_ARG]
        initialized_numbers_in_sudoku_by_order_arg = [int(number) for number
                                                      in list_of_args[constants.INDEX_OF_INITIALIZED_NUMBERS_IN_SUDOKU_BY_ORDER_ARG].split(" ")]
        do_recursive_drawing_arg = list_of_args[constants.INDEX_OF_DO_RECURSIVE_DRAWING_ARG].lower() == "true"

        sudoku_board_as_numbers_array = get_sudoku_board_as_array_from_img(img_path_arg, initialized_numbers_in_sudoku_by_order_arg)
        sudoku_board = SudokuBoard(sudoku_board_as_numbers_array)
        sudoku_gui = SudokuGui(constants.WINDOW_SIZE, constants.AMOUNT_OF_CUBES_IN_AREA, constants.SCREEN_COLOR, constants.LINE_COLOR)
        sudoku_solver = SudokuSolver(sudoku_board, sudoku_gui)
        sudoku_solver.solve_sudoku(arg_do_recursive_drawing=do_recursive_drawing_arg)
        sudoku_gui.draw_sudoku_board(sudoku_board, arg_is_recursive_drawing=False)
        sudoku_gui.close_gui()
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main(sys.argv[constants.INDEX_OF_FIRST_ARG:])
