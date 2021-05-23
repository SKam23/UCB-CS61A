email = 'skam@berkeley.edu'

def night(zl):
    """
    A night-copy is a perfect replica of a nested list's box-and-pointer structure.
        If an environment diagram were drawn out, the two should be entirely
        separate but identical.

    A `zl` is a list that only contains ints and other lists.

    The function `night` generates a night-copy of the given list `zl`.

    Note: The `isinstance` function takes in a value and a type and determines
        whether the value is of the given type. So

        >>> isinstance("abc", str)
        True
        >>> isinstance("abc", list)
        False

    Here's an example, where night_y = night(y)


                             +-----+-----+            +-----+-----+-----+
                             |     |     |            |     |     |     |
                             |  +  |  +-------------> | 200 | 300 |  +  |
        y +----------------> |  |  |     |            |     |     |  |  |
                             +-----+-----+       +--> +-----+-----+-----+
        night_y +-+             |                |       ^           |
                  |             +----------------+       |           |
                  |                                      +-----------+
                  |
                  |          +-----+-----+            +-----+-----+-----+
                  |          |     |     |            |     |     |     |
                  +------->  |  +  |  +-------------> | 200 | 300 |  +  |
                             |  |  |     |            |     |     |  |  |
                             +-----+-----+       +--> +-----+-----+-----+
                                |                |       ^           |
                                +----------------+       |           |
                                                         +-----------+

    >>> x = [200, 300]
    >>> x.append(x)
    >>> y = [x, x]              # this is the `y` from the doctests
    >>> night_y = night(y)      # this is the `night_y` from the doctests
    >>> # check that night_y has the same structure as y
    >>> len(night_y)
    2
    >>> night_y[0] is night_y[1]
    True
    >>> len(night_y[0])
    3
    >>> night_y[0][0]
    200
    >>> night_y[0][1]
    300
    >>> night_y[0][2] is night_y[0]
    True
    >>> # check that night_y and y have no list objects in common
    >>> night_y is y
    False
    >>> night_y[0] is y[0]
    False
    """
    night_lookup = []
    def helper(zl):
        if len(zl)==0:
            return []
        for old_new in zl:
            if isinstance(old_new, list):
                return old_new[1]
        new_zl = []
        night_lookup.append((zl, new_zl))
        for element in night_lookup:
            new_zl += [helper(element)]
        return new_zl
    return helper(zl)

# ORIGINAL SKELETON FOLLOWS

# def night(zl):
#     """
#     A night-copy is a perfect replica of a nested list's box-and-pointer structure.
#         If an environment diagram were drawn out, the two should be entirely
#         separate but identical.

#     A `zl` is a list that only contains ints and other lists.

#     The function `night` generates a night-copy of the given list `zl`.

#     Note: The `isinstance` function takes in a value and a type and determines
#         whether the value is of the given type. So

#         >>> isinstance("abc", str)
#         True
#         >>> isinstance("abc", list)
#         False

#     Here's an example, where night_y = night(y)


#                              +-----+-----+            +-----+-----+-----+
#                              |     |     |            |     |     |     |
#                              |  +  |  +-------------> | 200 | 300 |  +  |
#         y +----------------> |  |  |     |            |     |     |  |  |
#                              +-----+-----+       +--> +-----+-----+-----+
#         night_y +-+             |                |       ^           |
#                   |             +----------------+       |           |
#                   |                                      +-----------+
#                   |
#                   |          +-----+-----+            +-----+-----+-----+
#                   |          |     |     |            |     |     |     |
#                   +------->  |  +  |  +-------------> | 200 | 300 |  +  |
#                              |  |  |     |            |     |     |  |  |
#                              +-----+-----+       +--> +-----+-----+-----+
#                                 |                |       ^           |
#                                 +----------------+       |           |
#                                                          +-----------+

#     >>> x = [200, 300]
#     >>> x.append(x)
#     >>> y = [x, x]              # this is the `y` from the doctests
#     >>> night_y = night(y)      # this is the `night_y` from the doctests
#     >>> # check that night_y has the same structure as y
#     >>> len(night_y)
#     2
#     >>> night_y[0] is night_y[1]
#     True
#     >>> len(night_y[0])
#     3
#     >>> night_y[0][0]
#     200
#     >>> night_y[0][1]
#     300
#     >>> night_y[0][2] is night_y[0]
#     True
#     >>> # check that night_y and y have no list objects in common
#     >>> night_y is y
#     False
#     >>> night_y[0] is y[0]
#     False
#     """
#     night_lookup = []
#     def helper(zl):
#         if ______:
#             return ______
#         for old_new in ______:
#             if ______:
#                 return old_new[1]
#         new_zl = []
#         night_lookup.append((zl, new_zl))
#         for element in ______:
#             ______
#         return new_zl
#     return helper(zl)
