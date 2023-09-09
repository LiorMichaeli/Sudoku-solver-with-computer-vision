import cv2 as cv
import numpy as np
from helpers_for_image_processing import sort_corners_of_square, get_distance_between_points, get_cell_size_in_sudoku_board

def get_sudoku_board_as_array_from_img(arg_img_path: str, initialized_numbers_in_sodoku_by_order: list):
    img_after_pre_processing = pre_processing(arg_img_path)
    sudoku_board_gray_scale_img = get_sudoku_board_as_gray_scale_img(img_after_pre_processing)
    cells_imgs_list_in_sorted_order = get_sudoku_board_cells_in_sorted_order(sudoku_board_gray_scale_img)
    sudoku_board_as_numbers_array = convert_cells_imgs_to_numbers(sudoku_board_gray_scale_img,
                                                                  cells_imgs_list_in_sorted_order,
                                                                  initialized_numbers_in_sodoku_by_order)
    return sudoku_board_as_numbers_array

def pre_processing(arg_img_path: str):
    img = cv.imread(arg_img_path)
    gray_scale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur_gray_scale_img = cv.GaussianBlur(gray_scale_img, (3, 3), 5)
    threshold_img = cv.adaptiveThreshold(blur_gray_scale_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 12)
    return threshold_img


def get_sudoku_board_as_gray_scale_img(img_after_pre_processing):
    top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner = get_corners_of_sudoku_board(img_after_pre_processing)
    sudoku_board_gray_scale_img = warp_sudoku_board(img_after_pre_processing, top_left_corner, top_right_corner,
                                                    bottom_right_corner, bottom_left_corner)
    return sudoku_board_gray_scale_img

def get_sudoku_board_cells_in_sorted_order(sudoku_board_gray_scale_img):
    sudoku_board_cells = []
    cell_size = get_cell_size_in_sudoku_board(sudoku_board_gray_scale_img)
    i = 0
    for row_index in range(9):
        for col_index in range(9):
            digit_img = sudoku_board_gray_scale_img[
                        (row_index * cell_size) + (cell_size // 7):((row_index + 1) * cell_size) - (cell_size // 7),
                        (col_index * cell_size) + (cell_size // 7):((col_index + 1) * cell_size) - (cell_size // 7)
                        ]#cut borders (7)
            _, threshold_digit_img = cv.threshold(digit_img, 250, 255, cv.THRESH_BINARY)
            sudoku_board_cells.append(threshold_digit_img)
    return sudoku_board_cells


def convert_cells_imgs_to_numbers(sudoku_board_gray_scale_img, cells_imgs_list_in_sorted_order,
                                  initialized_numbers_in_sodoku_by_order: list):
    print(initialized_numbers_in_sodoku_by_order)
    cell_size = get_cell_size_in_sudoku_board(sudoku_board_gray_scale_img)
    threshold = ((cell_size // 8) ** 2) * 255
    sudoku_board_as_numbers_array = []  # zero when empty
    sudoku_board_row = []
    iterator_for_initialized_numbers_in_sodoku = 0
    for index, cell in enumerate(cells_imgs_list_in_sorted_order):
        if cell.sum() >= threshold:
            sudoku_board_row.append(initialized_numbers_in_sodoku_by_order[iterator_for_initialized_numbers_in_sodoku])
            iterator_for_initialized_numbers_in_sodoku += 1
        else:
            sudoku_board_row.append(0)
        if index % 9 == 8:
            sudoku_board_as_numbers_array.append(sudoku_board_row)
            sudoku_board_row = []
    return sudoku_board_as_numbers_array


def get_corners_of_sudoku_board(img_after_pre_processing):
    # Find contours in the binary image
    contours, _ = cv.findContours(img_after_pre_processing, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    corners_of_largest_square_in_img = get_corners_of_largest_square_in_img(contours)
    sorted_corners_of_largest_square_in_img = sort_corners_of_square(corners_of_largest_square_in_img)
    return sorted_corners_of_largest_square_in_img


def get_corners_of_largest_square_in_img(contours):
    corners_of_largest_square = None
    largest_square_area = 0
    for contour in contours:
        # Approximate the contour to a polygon with fewer vertices
        epsilon = 0.04 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)
        # Check if the polygon has 4 vertices (a square)
        if len(approx) == 4:
            # Calculate the area of the square
            area = cv.contourArea(contour)
            if area > largest_square_area:
                corners_of_largest_square = approx
                largest_square_area = area
    return corners_of_largest_square if corners_of_largest_square is not None else None


def warp_sudoku_board(img_after_pre_processing, top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner):
    sudoku_board_img_width = max([get_distance_between_points(top_left_corner, top_right_corner),
                                  get_distance_between_points(top_right_corner, bottom_right_corner),
                                  get_distance_between_points(bottom_right_corner, bottom_left_corner),
                                  get_distance_between_points(bottom_left_corner, top_left_corner)])

    src_img = np.array([top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner], dtype='float32')
    dst_img = np.array([(0, 0), (sudoku_board_img_width - 1, 0), (sudoku_board_img_width - 1, sudoku_board_img_width - 1),
                        (0, sudoku_board_img_width - 1)], dtype='float32')
    # Calculate the perspective transformation matrix
    perspective_transformation_matrix = cv.getPerspectiveTransform(src_img, dst_img)
    sudoku_board_gray_scale_img = cv.warpPerspective(img_after_pre_processing, perspective_transformation_matrix,
                                                     (int(sudoku_board_img_width), int(sudoku_board_img_width)))
    return sudoku_board_gray_scale_img
