email = 'skam@berkeley.edu'

"""
Let a `chisel` be a self-referential function that
    - takes in one integer
    - returns two values, another chisel and well as an integer

For an example see the function `identity_chisel` below.

You have two tasks in this assignment, to implement the functions `encyclopedia`
and `wallsocket`. Both have their behavior defined by their doctests.

It is not necessary to implement `encyclopedia` correctly to get the points for
`wallsocket`. However, the ok test cases for `wallsocket` will fail if you have not correctly
implemented `encyclopedia`.
"""

def identity_chisel(x):
    return identity_chisel, x

def encyclopedia(a=0, s=1):
    """
    This function returns a chisel function that processes a sequence
    of integers, and returns the alternating sum of all integers seen thus
    far (see doctest for an example).

    >>> chisel_a = encyclopedia()
    >>> chisel_b, x = chisel_a(2)
    >>> x                                   # 2
    2
    >>> chisel_c, x = chisel_b(8)
    >>> x                                   # 2 - 8
    -6
    >>> chisel_d, x = chisel_c(12)
    >>> x                                   # 2 - 8 + 12
    6
    >>> chisel_e, x = chisel_d(30)
    >>> x                                   # 2 - 8 + 12 - 30
    -24
    >>> chisel_b_again, x = chisel_a(100)
    >>> x                                   # 100 [note that we are using chisel_a not chisel_d here]
    100
    """
    def chisel(x):
        return encyclopedia(a+(s*x),s*-1), a+(s*x)
    return chisel

def wallsocket(chisel, items):
    """
    The function `wallsocket` takes in a `chisel` and a nonempty list of `items` and
    runs the given `chisel` on each of the `items` in turn, returning the final
    numeric result.

    For example, on the items [1, 2, 3, 4, 5] with the chisel encyclopedia
    we return 1 - 2 + 3 - 4 + 5 = 3

    >>> wallsocket(encyclopedia(), [1, 2, 3, 4, 5])
    3
    >>> wallsocket(encyclopedia(), [4000])
    4000
    >>> wallsocket(encyclopedia(), [2, 90])
    -88
    >>> wallsocket(identity_chisel, [2, 90])
    90
    """
    chisel, x = chisel(items(0))
    if len(items)==0:
        return 0
    return x + wallsocket(chisel, items[1:])


# ORIGINAL SKELETON FOLLOWS

# """
# Let a `chisel` be a self-referential function that
#     - takes in one integer
#     - returns two values, another chisel and well as an integer

# For an example see the function `identity_chisel` below.

# You have two tasks in this assignment, to implement the functions `encyclopedia`
# and `wallsocket`. Both have their behavior defined by their doctests.

# It is not necessary to implement `encyclopedia` correctly to get the points for
# `wallsocket`. However, the ok test cases for `wallsocket` will fail if you have not correctly
# implemented `encyclopedia`.
# """

# def identity_chisel(x):
#     return identity_chisel, x

# def encyclopedia(a=0, s=1):
#     """
#     This function returns a chisel function that processes a sequence
#     of integers, and returns the alternating sum of all integers seen thus
#     far (see doctest for an example).

#     >>> chisel_a = encyclopedia()
#     >>> chisel_b, x = chisel_a(2)
#     >>> x                                   # 2
#     2
#     >>> chisel_c, x = chisel_b(8)
#     >>> x                                   # 2 - 8
#     -6
#     >>> chisel_d, x = chisel_c(12)
#     >>> x                                   # 2 - 8 + 12
#     6
#     >>> chisel_e, x = chisel_d(30)
#     >>> x                                   # 2 - 8 + 12 - 30
#     -24
#     >>> chisel_b_again, x = chisel_a(100)
#     >>> x                                   # 100 [note that we are using chisel_a not chisel_d here]
#     100
#     """
#     def chisel(x):
#         return ______, ______
#     ______

# def wallsocket(chisel, items):
#     """
#     The function `wallsocket` takes in a `chisel` and a nonempty list of `items` and
#     runs the given `chisel` on each of the `items` in turn, returning the final
#     numeric result.

#     For example, on the items [1, 2, 3, 4, 5] with the chisel encyclopedia
#     we return 1 - 2 + 3 - 4 + 5 = 3

#     >>> wallsocket(encyclopedia(), [1, 2, 3, 4, 5])
#     3
#     >>> wallsocket(encyclopedia(), [4000])
#     4000
#     >>> wallsocket(encyclopedia(), [2, 90])
#     -88
#     >>> wallsocket(identity_chisel, [2, 90])
#     90
#     """
#     chisel, x = ______
#     if ______:
#         return ______
#     return ______
