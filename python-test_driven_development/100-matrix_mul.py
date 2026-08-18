#!/usr/bin/python3
"""
Defines a matrix multiplication function.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    first_len = len(m_a[0])
    for row in m_a:
        if len(row) != first_len:
            raise TypeError("each row of m_a must be of the same size")

    second_len = len(m_b[0])
    for row in m_b:
        if len(row) != second_len:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            new_row.append(sum_val)
        result.append(new_row)

    return result
