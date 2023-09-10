"""
    image_processing

    This is file that handles the image processing of the sudoku board image.

    Functions:
        get_sudoku_board_as_array_from_img(arg_img_path: str, initialized_numbers_in_sodoku_by_order: List)
         -> List[List[int]]: This is a function that gets img path and the numbers that were initialized in sodoku by order
         from left to right and top to bottom, and returns 2D array of numbers that represents the sudoku board.

    Usage:
        Detect sudoku board and convert him to 2D array of numbers that represents the sudoku board.
        Example:
            sudoku_board_as_numbers_array = get_sudoku_board_as_array_from_img('Data/sudoku_img_example.jpg',
                                                                       [8, 1, 9, 5, 8, 7, 1, 4, 9, 7, 6, 7, 1, 2, 5, 8,
                                                                       6, 1, 7, 1, 5, 2, 9, 7, 4, 6, 8, 3, 9, 4, 3, 5, 8])
    """


# Imports
import cv2 as cv
import numpy as np
from typing import Tuple, List, Union
from helpers_for_image_processing import sort_corners_of_square, get_distance_between_points, get_cell_size_in_sudoku_board
import constants
from errors import Errors


def get_sudoku_board_as_array_from_img(arg_img_path: str, initialized_numbers_in_sodoku_by_order: List) -> List[List[int]]:
    '''
    This is a function that gets img path and the numbers that were initialized in sodoku by order
         from left to right and top to bottom, and returns 2D array of numbers that represents the sudoku board.
    :param arg_img_path:
    :param initialized_numbers_in_sodoku_by_order:
    :exception Not succeeded to detect the sudoku board: If the program not succeeded to detect the sudoku board so
     the function will raise an exception with the appropriate error msg.
    :return: 2D array of numbers that represents the sudoku_board.
    '''
    img_after_pre_processing = __pre_processing(arg_img_path)
    try:
        sudoku_board_gray_scale_img = __get_sudoku_board_as_gray_scale_img(img_after_pre_processing)
    except Exception as e:
        raise e
    cells_imgs_list_in_sorted_order = __get_sudoku_board_cells_in_sorted_order(sudoku_board_gray_scale_img)
    sudoku_board_as_numbers_array = __convert_cells_imgs_to_numbers(sudoku_board_gray_scale_img,
                                                                  cells_imgs_list_in_sorted_order,
                                                                  initialized_numbers_in_sodoku_by_order)
    return sudoku_board_as_numbers_array

def __pre_processing(arg_img_path: str) -> np.ndarray:
    img = cv.imread(arg_img_path)
    gray_scale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur_gray_scale_img = cv.GaussianBlur(gray_scale_img, (3, 3), 5)
    threshold_img = cv.adaptiveThreshold(blur_gray_scale_img, constants.MAX_VALUE_FOR_PIXEL, cv.ADAPTIVE_THRESH_MEAN_C,
                                         cv.THRESH_BINARY_INV, blockSize=11, C=12)
    return threshold_img


def __get_sudoku_board_as_gray_scale_img(img_after_pre_processing: np.ndarray) -> np.ndarray:
    try:
        top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner = __get_corners_of_sudoku_board(img_after_pre_processing)
    except Exception as e:
        raise e
    sudoku_board_gray_scale_img = __warp_sudoku_board(img_after_pre_processing, top_left_corner, top_right_corner,
                                                    bottom_right_corner, bottom_left_corner)
    return sudoku_board_gray_scale_img

def __get_sudoku_board_cells_in_sorted_order(sudoku_board_gray_scale_img: np.ndarray) -> List[np.ndarray]:
    sudoku_board_cells = []
    cell_size = get_cell_size_in_sudoku_board(sudoku_board_gray_scale_img)
    for row_index in range(constants.NUMBER_OF_ROWS_IN_SUDOKU_BOARD):
        for col_index in range(constants.NUMBER_OF_COLS_IN_SUDOKU_BOARD):
            # We use constants.RATIO_BETWEEN_BOUNDARIES_OF_A_CELL_AND_THE_CELL_ITSELF
            # to cut the boundaries from the cell
            digit_img = sudoku_board_gray_scale_img[
                        (row_index * cell_size) + (cell_size // constants.RATIO_BETWEEN_BOUNDARIES_OF_A_CELL_AND_THE_CELL_ITSELF):
                        ((row_index + 1) * cell_size) - (cell_size // constants.RATIO_BETWEEN_BOUNDARIES_OF_A_CELL_AND_THE_CELL_ITSELF),
                        (col_index * cell_size) + (cell_size // constants.RATIO_BETWEEN_BOUNDARIES_OF_A_CELL_AND_THE_CELL_ITSELF):
                        ((col_index + 1) * cell_size) - (cell_size // constants.RATIO_BETWEEN_BOUNDARIES_OF_A_CELL_AND_THE_CELL_ITSELF)
                        ]
            # We do threshold in order to in each cell in the img if there is number he will be in white
            _, threshold_digit_img = cv.threshold(digit_img, thresh=250, maxval=constants.MAX_VALUE_FOR_PIXEL, type=cv.THRESH_BINARY)
            sudoku_board_cells.append(threshold_digit_img)
    return sudoku_board_cells


def __convert_cells_imgs_to_numbers(sudoku_board_gray_scale_img: np.ndarray, cells_imgs_list_in_sorted_order: np.ndarray,
                                    initialized_numbers_in_sodoku_by_order: List[int]) -> List[List[int]]:
    cell_size = get_cell_size_in_sudoku_board(sudoku_board_gray_scale_img)
    threshold = ((cell_size // 8) ** 2) * constants.MAX_VALUE_FOR_PIXEL
    sudoku_board_as_numbers_array = []
    sudoku_board_row = []
    iterator_for_initialized_numbers_in_sodoku = 0
    for index, cell in enumerate(cells_imgs_list_in_sorted_order):
        # Checks if the cell contains number
        if cell.sum() >= threshold:
            sudoku_board_row.append(initialized_numbers_in_sodoku_by_order[iterator_for_initialized_numbers_in_sodoku])
            iterator_for_initialized_numbers_in_sodoku += 1
        else:
            sudoku_board_row.append(constants.EMPTY_CELL_VALUE)
        if index % constants.NUMBER_OF_COLS_IN_SUDOKU_BOARD == constants.NUMBER_OF_COLS_IN_SUDOKU_BOARD-1:
            sudoku_board_as_numbers_array.append(sudoku_board_row)  # Add the current row of cells
            sudoku_board_row = []
    return sudoku_board_as_numbers_array


def __get_corners_of_sudoku_board(img_after_pre_processing: np.ndarray) -> Tuple[List[int], List[int], List[int], List[int]]:
    # Find contours in the binary image
    contours, _ = cv.findContours(img_after_pre_processing, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    corners_of_largest_square_in_img = __get_corners_of_largest_square_in_img(contours)
    if corners_of_largest_square_in_img is None:
        raise Exception(Errors.NOT_FOUND_SUDOKU_BOARD)
    sorted_corners_of_largest_square_in_img = sort_corners_of_square(corners_of_largest_square_in_img)
    return sorted_corners_of_largest_square_in_img


def __get_corners_of_largest_square_in_img(contours: List[np.ndarray]) -> Union[np.ndarray, None]:
    corners_of_largest_square = None
    largest_square_area = 0
    for contour in contours:
        # Approximate the contour to a polygon with fewer corners
        epsilon = 0.04 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)
        # Checks if the polygon has 4 corners (a square)
        if len(approx) == constants.AMOUNT_OF_CORNERS_IN_SQUARE:
            # Calculate the area of the square
            area = cv.contourArea(contour)
            if area > largest_square_area:
                corners_of_largest_square = approx
                largest_square_area = area
    return corners_of_largest_square if corners_of_largest_square is not None else None


def __warp_sudoku_board(img_after_pre_processing: np.ndarray, top_left_corner: List[int], top_right_corner: List[int],
                        bottom_right_corner: List[int], bottom_left_corner: List[int]) -> np.ndarray:
    # The width of the sudoku board img will be the max distance between two adjacent corners in a square
    sudoku_board_img_width = max([get_distance_between_points(top_left_corner, top_right_corner),
                                  get_distance_between_points(top_right_corner, bottom_right_corner),
                                  get_distance_between_points(bottom_right_corner, bottom_left_corner),
                                  get_distance_between_points(bottom_left_corner, top_left_corner)])
    # Matching the indexes of the sudoku_board corners to their indexes in the new sudoku board img
    src_img = np.array([top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner], dtype='float32')
    dst_img = np.array([constants.INDEXES_OF_TOP_LEFT_PIXEL_IN_IMG,
                        (sudoku_board_img_width - 1, constants.ROW_INDEX_OF_TOP_RIGHT_PIXEL_IN_IMG),
                        (sudoku_board_img_width - 1, sudoku_board_img_width - 1),
                        (constants.COL_INDEX_OF_BOTTOM_LEFT_PIXEL_IN_IMG, sudoku_board_img_width - 1)], dtype='float32')
    # Calculate the perspective transformation matrix
    perspective_transformation_matrix = cv.getPerspectiveTransform(src_img, dst_img)
    sudoku_board_gray_scale_img = cv.warpPerspective(img_after_pre_processing, perspective_transformation_matrix,
                                                     (int(sudoku_board_img_width), int(sudoku_board_img_width)))
    return sudoku_board_gray_scale_img
