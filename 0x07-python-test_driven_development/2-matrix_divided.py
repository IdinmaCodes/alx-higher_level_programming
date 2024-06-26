#!/usr/bin/python3
"""
Module: matrix_operations

This module provides functions for performing operations on matrices.

Functions:
- matrix_divided(matrix, div): Divides each element in the matrix by div,
  squares the result, and rounds it to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide each element in the matrix by div, square the result, and round it
    to two decimal places.

    Args:
    - matrix (list of lists): Matrix of integers or floats.
    - div (int or float): Number to divide each element in the matrix.

    Returns:
    - list of lists: New matrix where each element is the squared and rounded
      result of the corresponding element in the input matrix divided by div.

    Raises:
    - TypeError: If matrix is not a list of lists of integers/floats,
    if any row in the matrix has a different length, or if div is not a number.
    - ZeroDivisionError: If div is zero.
    """
    new_matrix = []

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    base_length = len(matrix[0])
    if any(len(row) != base_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        for element in row:
            result = element / div
            squared_result = result ** 2
            rounded_result = round(squared_result, 2)
            new_row.append(rounded_result)
        new_matrix.append(new_row)

    return new_matrix
