"""
constants

This is file that contains constants for the software.
"""


# Sudoku board constants
NUMBER_OF_ROWS_IN_SUDOKU_BOARD = 9
NUMBER_OF_COLS_IN_SUDOKU_BOARD = 9
EMPTY_CUBE_VALUE = 0
EMPTY_CELL_VALUE = 0
FIRST_CUBE_IN_AREA = 0
LAST_CUBE_IN_AREA = 1
ROW_INDEX = 0
COL_INDEX = 1
INDEXES_OF_LAST_CUBE_IN_SUDOKU_BOARD = (8, 8)
INDEX_OF_FIRST_COL_IN_SUDOKU_BOARD = 0
INDEX_OF_LAST_COL_IN_SUDOKU_BOARD = 8
INDEX_OF_FIRST_ROW_IN_SUDOKU_BOARD = 0
INDEX_OF_LAST_ROW_IN_SUDOKU_BOARD = 8
SIZE_OF_CUBE = 3
INDEX_OF_LAST_ROW_IN_FIRST_AREA_IN_LINE = 2
INDEX_OF_LAST_COL_IN_FIRST_AREA_IN_LINE = 2
MAX_AMOUNT_OF_CUBES_WITH_THE_SAME_VALUE_IN_AREA = 1
MAX_AMOUNT_OF_CUBES_WITH_THE_SAME_VALUE_IN_ROW = 1
MAX_AMOUNT_OF_CUBES_WITH_THE_SAME_VALUE_IN_COL = 1
MIN_LEGAL_VALUE_OF_SUDOKU_CUBE = 0
MAX_LEGAL_VALUE_OF_SUDOKU_CUBE = 9
MIN_NON_EMPTY_VALUE_OF_SUDOKU_CUBE = 1
CUBE_AREA_INDEXES = 0
CUBE_ROW_INDEX = 1
CUBE_COL_INDEX = 2


# Gui constants
THE_DRAWING_RATE_OF_THE_SUDOKU_SOLVING_PROCESS = 190
REGULAR_LINE_BORDER_IN_SUDOKU_BOARD_GUI = 7
END_AREA_LINE_BORDER_IN_SUDOKU_BOARD_GUI = 14
NUMBERS_FONT_IN_SUDOKU_BOARD_GUI = 40
RED_COLOR = (255, 0, 0)


# Image processing constants
MAX_VALUE_FOR_PIXEL = 255
RATIO_BETWEEN_BOUNDARIES_OF_A_CELL_AND_THE_CELL_ITSELF = 7
AMOUNT_OF_CORNERS_IN_SQUARE = 4
INDEXES_OF_TOP_LEFT_PIXEL_IN_IMG = (0, 0)
ROW_INDEX_OF_TOP_RIGHT_PIXEL_IN_IMG = 0
COL_INDEX_OF_BOTTOM_LEFT_PIXEL_IN_IMG = 0
TOP_LEFT_CORNER_INDEX = 0
TOP_RIGHT_CORNER_INDEX = 0
BOTTOM_LEFT_CORNER_INDEX = 1
BOTTOM_RIGHT_CORNER_INDEX = 1
INDEX_OF_FIRST_CORNER = 0
INDEX_OF_SECOND_CORNER = 1
INDEX_OF_THIRD_CORNER = 2
GET_CORNER = 0
HEIGHT_OF_THE_IMG = 0
ROW_INDEX_IN_IMG = 1
COL_INDEX_IN_IMG = 0


# Constants for main method
INDEX_OF_IMG_PATH_ARG = 0
INDEX_OF_FIRST_ARG = 1
INDEX_OF_INITIALIZED_NUMBERS_IN_SUDOKU_BY_ORDER_ARG = 1
INDEX_OF_DO_RECURSIVE_DRAWING_ARG = 2
WINDOW_SIZE = 540
AMOUNT_OF_CUBES_IN_AREA = 9
SCREEN_COLOR = (160, 185, 236)
LINE_COLOR = (0, 0, 0)
