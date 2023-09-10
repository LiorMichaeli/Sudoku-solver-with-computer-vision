"""
sudoku_gui

This is file that handles sudoku gui.
"""


# Imports
import pygame
import sys
from sudoku_board import SudokuBoard
from typing import Tuple
import math
import constants


class SudokuGui:
    """
        Sudoku Gui class

        This class represents a Sudoku Gui. It provides methods for handle the Gui.

        Attributes:
            __window_size (int): The window size of the gui. The Screen is __window_size x __window_size.
            __amount_of_cubes_in_area (int): The amount of cubes in area in sudoku board. In most times, this is will be 9.
            __screen_color (Tuple[int, int, int]): The color of the screen.
            __line_color (Tuple[int, int, int]): The color of the lines in the sudoku board.
            __screen (pygame.Surface): The screen obj of the gui.

        Methods:
            __init__(self, arg_window_size: int, arg_amount_of_cubes_in_area: int, arg_screen_color: Tuple[int, int, int],
                 arg_line_color: Tuple[int, int, int]) -> None: Initializes a new Sudoku Gui.
            draw_sudoku_board(self, arg_sudoku_board: SudokuBoard, arg_is_recursive_drawing): Draw the arg_sudoku_board on the gui.
            If arg_is_recursive_drawing is true so this will draw once the current state of the arg_sudoku_board and will terminate.
            Else this will draw the arg_sudoku_board and the gui will terminate when the user will quit.
            close_gui() -> None: This is a static method that terminate the gui.

        Usage:
            Draw sudoku board on gui.
            Example:
                sudoku_gui = SudokuGui(500, 9, (255,255,255), (0,0,0))
                sudoku_gui.draw(sudoku_board, arg_is_recursive_drawing=False)
            Close gui.
            Example:
                sudoku_gui.close_gui()
    """
    def __init__(self, arg_window_size: int, arg_amount_of_cubes_in_area: int, arg_screen_color: Tuple[int, int, int],
                 arg_line_color: Tuple[int, int, int]) -> None:
        pygame.init()
        self.__window_size = arg_window_size
        self.__amount_of_cubes_in_area = arg_amount_of_cubes_in_area
        self.__screen_color = arg_screen_color
        self.__line_color = arg_line_color
        self.__screen = pygame.display.set_mode((self.__window_size, self.__window_size))
        self.__screen.fill(self.__screen_color)
        pygame.display.set_caption("Sudoku Solver")

    def draw_sudoku_board(self, arg_sudoku_board: SudokuBoard, arg_is_recursive_drawing):
        self.__screen.fill(self.__screen_color)
        if arg_is_recursive_drawing:
            self.__draw_lines_of_sudoku_board()
            self.__fill_numbers_in_sudoku_board(arg_sudoku_board)
            pygame.display.flip()
        else:
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                self.__draw_lines_of_sudoku_board()
                self.__fill_numbers_in_sudoku_board(arg_sudoku_board)
                pygame.display.flip()

    def __draw_lines_of_sudoku_board(self):
        cube_size = self.__window_size // self.__amount_of_cubes_in_area
        for cube_index in range(self.__amount_of_cubes_in_area-1):
            line_border = constants.REGULAR_LINE_BORDER_IN_SUDOKU_BOARD_GUI
            # Checks if we are in cube index that represents the end of the area
            if cube_index % math.sqrt(self.__amount_of_cubes_in_area) == math.sqrt(self.__amount_of_cubes_in_area)-1:
                line_border = constants.END_AREA_LINE_BORDER_IN_SUDOKU_BOARD_GUI
            # Draw vertical line
            pygame.draw.line(self.__screen, self.__line_color, [(cube_index+1)*cube_size, constants.INDEX_OF_FIRST_ROW_IN_SUDOKU_BOARD],
                             [(cube_index+1)*cube_size, self.__window_size], line_border)
            # Draw horizontal line
            pygame.draw.line(self.__screen, self.__line_color, [constants.INDEX_OF_FIRST_COL_IN_SUDOKU_BOARD, (cube_index+1)*cube_size],
                             [self.__window_size, (cube_index+1)*cube_size], line_border)

    def __fill_numbers_in_sudoku_board(self, arg_sudoku_board: SudokuBoard):
        cube_size = self.__window_size // self.__amount_of_cubes_in_area
        for row_index in range(self.__amount_of_cubes_in_area):
            for col_index in range(self.__amount_of_cubes_in_area):
                current_cube = arg_sudoku_board.get_cube_in_board(row_index, col_index)
                number = current_cube.get_value_of_sudoku_cube()
                if number:
                    font = pygame.font.Font(None, constants.NUMBERS_FONT_IN_SUDOKU_BOARD_GUI)
                    if current_cube.is_an_initialized_sudoku_cube():
                        text = font.render(str(number), True, color=self.__line_color)
                    else:
                        text = font.render(str(number), True, color=constants.RED_COLOR)
                    self.__screen.blit(text, (col_index * cube_size + cube_size//2.5, row_index * cube_size + cube_size//2.5))

    @staticmethod
    def close_gui() -> None:
        pygame.quit()
        sys.exit()
