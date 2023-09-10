
# Imports
from enum import Enum


# Enum of errors.
# Types of errors with the corresponding errors messages.
class Errors(Enum):
    ILLEGAL_VALUE_OF_SUDOKU_CUBE = "Error: Values of cubes in sudoku board must be integers between 0 and 9."
    NOT_DETECT_SUDOKU_BOARD = "Error: The program not succeeded to detect the sudoku board.\n" \
                             "Remember to bring a image with a sudoku board inside.\n" \
                             "To make it easier for the software, bring a good quality image\n" \
                             "in which the sudoku board will be placed on a smooth surface\n" \
                             " and in a straight and clear form. "

