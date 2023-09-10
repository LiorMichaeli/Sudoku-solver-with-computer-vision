"""
helpers_for_image_processing

This is file that handles helpers functions for image processing.
"""


# Imports
import numpy as np
from typing import Tuple, List
import constants

def sort_corners_of_square(arg_corners_of_largest_square_in_img: np.ndarray) -> Tuple[List[int], List[int], List[int], List[int]]:
    leftmost_corners = get_two_leftmost_corners_in_square(arg_corners_of_largest_square_in_img)
    rightmost_corners = get_two_rightmost_corners_in_square(arg_corners_of_largest_square_in_img)
    sort_points_by_order_from_top_to_bottom(leftmost_corners)
    sort_points_by_order_from_top_to_bottom(rightmost_corners)
    return leftmost_corners[constants.TOP_LEFT_CORNER_INDEX], rightmost_corners[constants.TOP_RIGHT_CORNER_INDEX],\
        rightmost_corners[constants.BOTTOM_RIGHT_CORNER_INDEX], leftmost_corners[constants.BOTTOM_LEFT_CORNER_INDEX]


def get_two_leftmost_corners_in_square(arg_corners_of_largest_square_in_img: np.ndarray) -> list[List[int], List[int]]:
    if arg_corners_of_largest_square_in_img[constants.INDEX_OF_FIRST_CORNER][constants.GET_CORNER][constants.COL_INDEX_IN_IMG]\
            <= arg_corners_of_largest_square_in_img[constants.INDEX_OF_SECOND_CORNER][constants.GET_CORNER][constants.COL_INDEX_IN_IMG]:
        leftmost_corner = arg_corners_of_largest_square_in_img[constants.INDEX_OF_FIRST_CORNER][constants.GET_CORNER]
        second_leftmost_corner = arg_corners_of_largest_square_in_img[constants.INDEX_OF_SECOND_CORNER][constants.GET_CORNER]
    else:
        leftmost_corner = arg_corners_of_largest_square_in_img[constants.INDEX_OF_SECOND_CORNER][constants.GET_CORNER]
        second_leftmost_corner = arg_corners_of_largest_square_in_img[constants.INDEX_OF_FIRST_CORNER][constants.GET_CORNER]
    leftmost_corner_col_coordinate = leftmost_corner[constants.COL_INDEX_IN_IMG]
    second_leftmost_corner_col_coordinate = second_leftmost_corner[constants.COL_INDEX_IN_IMG]
    for corner in arg_corners_of_largest_square_in_img[constants.INDEX_OF_THIRD_CORNER:]:
        corner_col_coordinate = corner[constants.GET_CORNER][constants.COL_INDEX_IN_IMG]
        if corner_col_coordinate < leftmost_corner_col_coordinate:
            second_leftmost_corner = leftmost_corner
            leftmost_corner = corner[constants.GET_CORNER]
            leftmost_corner_col_coordinate = leftmost_corner[constants.COL_INDEX_IN_IMG]
            second_leftmost_corner_col_coordinate = second_leftmost_corner[constants.COL_INDEX_IN_IMG]
        elif corner_col_coordinate < second_leftmost_corner_col_coordinate:
            second_leftmost_corner = corner[constants.GET_CORNER]
            second_leftmost_corner_col_coordinate = second_leftmost_corner[constants.COL_INDEX_IN_IMG]
    return [leftmost_corner.tolist(), second_leftmost_corner.tolist()]


def get_two_rightmost_corners_in_square(arg_corners_of_largest_square_in_img: np.ndarray) -> list[List[int], List[int]]:
    if arg_corners_of_largest_square_in_img[constants.INDEX_OF_FIRST_CORNER][constants.GET_CORNER][constants.COL_INDEX_IN_IMG]\
            >= arg_corners_of_largest_square_in_img[constants.INDEX_OF_SECOND_CORNER][constants.GET_CORNER][constants.COL_INDEX_IN_IMG]:
        rightmost_corner = arg_corners_of_largest_square_in_img[constants.INDEX_OF_FIRST_CORNER][constants.GET_CORNER]
        second_rightmost_corner = arg_corners_of_largest_square_in_img[constants.INDEX_OF_SECOND_CORNER][constants.GET_CORNER]
    else:
        rightmost_corner = arg_corners_of_largest_square_in_img[constants.INDEX_OF_SECOND_CORNER][constants.GET_CORNER]
        second_rightmost_corner = arg_corners_of_largest_square_in_img[constants.INDEX_OF_FIRST_CORNER][constants.GET_CORNER]
    rightmost_corner_corner_col_coordinate = rightmost_corner[constants.COL_INDEX_IN_IMG]
    second_rightmost_corner_col_coordinate = second_rightmost_corner[constants.COL_INDEX_IN_IMG]
    for corner in arg_corners_of_largest_square_in_img[constants.INDEX_OF_THIRD_CORNER:]:
        corner_col_coordinate = corner[constants.GET_CORNER][constants.COL_INDEX_IN_IMG]
        if corner_col_coordinate > rightmost_corner_corner_col_coordinate:
            second_rightmost_corner = rightmost_corner
            rightmost_corner = corner[constants.GET_CORNER]
            rightmost_corner_corner_col_coordinate = rightmost_corner[constants.COL_INDEX_IN_IMG]
            second_rightmost_corner_col_coordinate = second_rightmost_corner[constants.COL_INDEX_IN_IMG]
        elif corner_col_coordinate > second_rightmost_corner_col_coordinate:
            second_rightmost_corner = corner[constants.GET_CORNER]
            second_rightmost_corner_col_coordinate = second_rightmost_corner[constants.COL_INDEX_IN_IMG]
    return [rightmost_corner.tolist(), second_rightmost_corner.tolist()]


def sort_points_by_order_from_top_to_bottom(arg_points: List[List[int]]) -> None:
    arg_points.sort(key=lambda point: point[constants.ROW_INDEX_IN_IMG])


def get_distance_between_points(arg_p1: List[int], arg_p2: List[int]) -> int:
    a = arg_p2[constants.COL_INDEX_IN_IMG] - arg_p1[constants.COL_INDEX_IN_IMG]
    b = arg_p2[constants.ROW_INDEX_IN_IMG] - arg_p1[constants.ROW_INDEX_IN_IMG]
    return np.sqrt((a ** 2) + (b ** 2))

def get_cell_size_in_sudoku_board(arg_sudoku_board_gray_scale_img: np.ndarray) -> int:
    return arg_sudoku_board_gray_scale_img.shape[constants.HEIGHT_OF_THE_IMG] // constants.NUMBER_OF_ROWS_IN_SUDOKU_BOARD

