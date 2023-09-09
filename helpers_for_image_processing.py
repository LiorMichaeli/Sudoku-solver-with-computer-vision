
# Imports
import numpy as np

def sort_corners_of_square(arg_corners_of_largest_square_in_img):
    leftmost_corners = get_two_leftmost_corners_in_square(arg_corners_of_largest_square_in_img)
    rightmost_corners = get_two_rightmost_corners_in_square(arg_corners_of_largest_square_in_img)
    print(leftmost_corners)
    print(rightmost_corners)
    sort_points_by_order_from_top_to_bottom(leftmost_corners)
    sort_points_by_order_from_top_to_bottom(rightmost_corners)
    return leftmost_corners[0], rightmost_corners[0], rightmost_corners[1], leftmost_corners[1]


def get_two_leftmost_corners_in_square(arg_corners_of_largest_square_in_img):
    if arg_corners_of_largest_square_in_img[0][0][0] <= arg_corners_of_largest_square_in_img[1][0][0]:
        leftmost_corner = arg_corners_of_largest_square_in_img[0][0]
        second_leftmost_corner = arg_corners_of_largest_square_in_img[1][0]
    else:
        leftmost_corner = arg_corners_of_largest_square_in_img[1][0]
        second_leftmost_corner = arg_corners_of_largest_square_in_img[0][0]
    leftmost_corner_corner_col_coordinate = leftmost_corner[0]
    second_leftmost_corner_col_coordinate = second_leftmost_corner[0]
    for corner in arg_corners_of_largest_square_in_img[2:]:
        corner_col_coordinate = corner[0][0]
        if corner_col_coordinate < leftmost_corner_corner_col_coordinate:
            second_leftmost_corner = leftmost_corner
            leftmost_corner = corner[0]
            leftmost_corner_corner_col_coordinate = leftmost_corner[0]
            second_leftmost_corner_col_coordinate = second_leftmost_corner[0]
        elif corner_col_coordinate < second_leftmost_corner_col_coordinate:
            second_leftmost_corner = corner[0]
            second_leftmost_corner_col_coordinate = second_leftmost_corner[0]
    return [leftmost_corner.tolist(), second_leftmost_corner.tolist()]


def get_two_rightmost_corners_in_square(arg_corners_of_largest_square_in_img):
    if arg_corners_of_largest_square_in_img[0][0][0] >= arg_corners_of_largest_square_in_img[1][0][0]:
        rightmost_corner = arg_corners_of_largest_square_in_img[0][0]
        second_rightmost_corner = arg_corners_of_largest_square_in_img[1][0]
    else:
        rightmost_corner = arg_corners_of_largest_square_in_img[1][0]
        second_rightmost_corner = arg_corners_of_largest_square_in_img[0][0]
    rightmost_corner_corner_col_coordinate = rightmost_corner[0]
    second_rightmost_corner_col_coordinate = second_rightmost_corner[0]
    for corner in arg_corners_of_largest_square_in_img[2:]:
        corner_col_coordinate = corner[0][0]
        if corner_col_coordinate > rightmost_corner_corner_col_coordinate:
            second_rightmost_corner = rightmost_corner
            rightmost_corner = corner[0]
            rightmost_corner_corner_col_coordinate = rightmost_corner[0]
            second_rightmost_corner_col_coordinate = second_rightmost_corner[0]
        elif corner_col_coordinate > second_rightmost_corner_col_coordinate:
            second_rightmost_corner = corner[0]
            second_rightmost_corner_col_coordinate = second_rightmost_corner[0]
    return [rightmost_corner.tolist(), second_rightmost_corner.tolist()]


def sort_points_by_order_from_top_to_bottom(arg_points):
    arg_points.sort(key=lambda point: point[1])


def get_distance_between_points(p1, p2):
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    return np.sqrt((a ** 2) + (b ** 2))

def get_cell_size_in_sudoku_board(sudoku_board_gray_scale_img):
    return sudoku_board_gray_scale_img.shape[0] // 9

