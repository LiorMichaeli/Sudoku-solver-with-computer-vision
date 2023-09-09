
# Imports
from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver
from sudoku_gui import SudokuGui
from image_processing import get_sudoku_board_as_array_from_img

def main():
    # tests
    '''sudoku_board = SudokuBoard([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                                [0, 0, 0, 0, 8, 0, 0, 7, 9]])

    sudoku_board = SudokuBoard([[0, 6, 0, 0, 0, 0, 0, 0, 1],
                                [5, 0, 0, 2, 0, 0, 9, 0, 0],
                                [0, 0, 0, 0, 1, 9, 0, 3, 0],
                                [0, 9, 0, 0, 0, 0, 3, 0, 5],
                                [1, 2, 0, 0, 9, 0, 0, 7, 4],
                                [3, 0, 4, 0, 0, 0, 0, 6, 0],
                                [0, 1, 0, 8, 6, 0, 0, 0, 0],
                                [0, 0, 5, 0, 0, 3, 0, 0, 8],
                                [2, 0, 0, 0, 0, 0, 0, 1, 0]])'''

    sudoku_board = SudokuBoard([[0, 6, 0, 0, 0, 0, 0, 0, 1],
                                [5, 0, 0, 2, 0, 0, 9, 0, 0],
                                [0, 0, 0, 0, 1, 9, 0, 3, 0],
                                [0, 9, 0, 0, 0, 0, 3, 0, 5],
                                [1, 2, 0, 0, 9, 0, 0, 7, 4],
                                [3, 0, 4, 0, 0, 0, 0, 6, 0],
                                [0, 1, 0, 8, 6, 0, 0, 0, 0],
                                [0, 0, 5, 0, 0, 3, 0, 0, 8],
                                [2, 0, 0, 0, 0, 0, 0, 1, 0]])

    # print(sudoku_solver)
    '''WINDOW_SIZE = 540
    GRID_SIZE = 9
    WHITE = (160, 185, 236)
    LINE_COLOR = (0, 0, 0)
    sudoku_gui = SudokuGui(WINDOW_SIZE, GRID_SIZE, WHITE, LINE_COLOR)
    sudoku_solver = SudokuSolver(sudoku_board, sudoku_gui)
    sudoku_solver.solve_sudoku(arg_do_recursive_drawing=True)
    sudoku_gui.draw(sudoku_board, arg_is_recursive_drawing=False)
    sudoku_gui.close_screen()'''

    sudoku_board_as_numbers_array1 = get_sudoku_board_as_array_from_img('Data/sudoku_img_1.jpg',
                                                                       [8, 1, 9, 5, 8, 7, 1, 4, 9, 7, 6, 7, 1, 2, 5, 8,
                                                                       6, 1, 7, 1, 5, 2, 9, 7, 4, 6, 8, 3, 9, 4, 3, 5, 8])
    sudoku_board_as_numbers_array2 = get_sudoku_board_as_array_from_img('Data/sudoku_img_2.jpg',
                                                                       [1, 7, 2, 9, 8, 7, 4, 2, 4, 6, 5, 7, 9, 7, 1, 3,
                                                                        4, 2, 8, 1, 6, 2, 3, 1, 6, 4, 5, 3, 8])
    sudoku_board_as_numbers_array3 = get_sudoku_board_as_array_from_img('Data/sudoku_img_3.jpg',
                                                                        [9, 6, 7, 3, 1, 4, 4, 1, 5, 3, 6, 8, 9, 6, 3, 1,
                                                                         7, 1, 9, 4, 3, 1, 8, 9, 2, 7, 4, 4, 7])
    sudoku_board_as_numbers_array4 = get_sudoku_board_as_array_from_img('Data/sudoku_img_4.jpg',
                                                                        [9, 1, 4, 5, 9, 5, 1, 3, 2, 5, 9, 6, 7, 8, 4, 3,
                                                                         2, 3, 6, 5, 8, 6, 2])

    sudoku_board_as_numbers_array5 = get_sudoku_board_as_array_from_img('Data/sudoku_img_5.jpg',
                                                                        [9, 2, 3, 5, 6, 6, 8, 8, 4, 9, 2, 1, 6, 1, 9, 4,
                                                                         1, 7, 8, 5, 6, 1, 8, 1, 7, 2, 3, 9, 5, 7])
    sudoku_board = SudokuBoard(sudoku_board_as_numbers_array5)
    WINDOW_SIZE = 540
    GRID_SIZE = 9
    WHITE = (160, 185, 236)
    LINE_COLOR = (0, 0, 0)
    sudoku_gui = SudokuGui(WINDOW_SIZE, GRID_SIZE, WHITE, LINE_COLOR)
    sudoku_solver = SudokuSolver(sudoku_board, sudoku_gui)
    sudoku_gui.draw(sudoku_board, arg_is_recursive_drawing=False)
    sudoku_solver.solve_sudoku(arg_do_recursive_drawing=False)
    sudoku_gui.draw(sudoku_board, arg_is_recursive_drawing=False)
    sudoku_gui.close_screen()










if __name__ == "__main__":
    main()