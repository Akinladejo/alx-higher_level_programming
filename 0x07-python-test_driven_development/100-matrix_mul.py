#!/usr/bin/python3
"""
matrix mul module
contains:
matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """ Multiplicates two matrices """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if m_b == [] or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_b should contain only integers or floats")

    if any(len(m_a[0]) != len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(m_b[0]) != len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return res
