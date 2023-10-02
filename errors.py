"""
errors

This is file that contains errors that may occur in the software.
"""


# Imports
from enum import Enum


class Errors(Enum):
    """
    Errors enum

    This enum represents a collection of errors.

    This enum has types of errors with the corresponding errors messages.

    Usage:
            Prints error because illegal value of sudoku cube.
            Example:
                print(Errors.ILLEGAL_VALUE_OF_SUDOKU_CUBE.value)
    """

    ILLEGAL_VALUE_OF_SUDOKU_CUBE = "Values of cubes in sudoku board must be integers between 0 and 9(include 0 and 9)."
    NOT_DETECT_SUDOKU_BOARD = "The program not succeeded to detect the sudoku board.\n" \
                              "Remember to bring a image with a sudoku board inside.\n" \
                              "To make it easier for the software, bring a good quality image\n" \
                              "in which the sudoku board will be placed on a smooth surface\n" \
                              " and in a straight and clear form. "
