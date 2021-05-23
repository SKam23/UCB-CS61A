email = 'skam@berkeley.edu'

def republic(speech, coffee):
    """
    Write a function `republic` that takes in two lists.
        `speech` is a list of strings
        `coffee` is a list of integers

    It returns a new list where every element from `speech` is copied the
    number of times as the corresponding element in `coffee`. If the number
    of times to be copied is negative (-k), then it removes the previous
    k elements added.

    Note 1: `speech` and `coffee` do not have to be the same length, simply ignore
    any extra elements in the longer list.

    Note 2: you can assume that you will never be asked to delete more
    elements than exist


    >>> republic(['a', 'b', 'c'], [1, 2, 3])
    ['a', 'b', 'b', 'c', 'c', 'c']
    >>> republic(['a', 'b', 'c'], [3])
    ['a', 'a', 'a']
    >>> republic(['a', 'b', 'c'], [0, 2, 0])
    ['b', 'b']
    >>> republic([], [1,2,3])
    []
    >>> republic(['a', 'b', 'c'], [1, -1, 3])
    ['c', 'c', 'c']
    """
    def republic_helper(speech, coffee, updated_list):
        if len(speech)==0 or len(coffee)==0:
            return updated_list
        if coffee[0]>=0:
            updated_list.extend([speech[0] for _ in range(0, coffee[0])])
        else:
            updated_list = updated_list[:coffee[0]]
        return republic_helper(speech[1:], coffee[1:], updated_list)
    return republic_helper(speech,coffee, [] )

# ORIGINAL SKELETON FOLLOWS

# def republic(speech, coffee):
#     """
#     Write a function `republic` that takes in two lists.
#         `speech` is a list of strings
#         `coffee` is a list of integers

#     It returns a new list where every element from `speech` is copied the
#     number of times as the corresponding element in `coffee`. If the number
#     of times to be copied is negative (-k), then it removes the previous
#     k elements added.

#     Note 1: `speech` and `coffee` do not have to be the same length, simply ignore
#     any extra elements in the longer list.

#     Note 2: you can assume that you will never be asked to delete more
#     elements than exist


#     >>> republic(['a', 'b', 'c'], [1, 2, 3])
#     ['a', 'b', 'b', 'c', 'c', 'c']
#     >>> republic(['a', 'b', 'c'], [3])
#     ['a', 'a', 'a']
#     >>> republic(['a', 'b', 'c'], [0, 2, 0])
#     ['b', 'b']
#     >>> republic([], [1,2,3])
#     []
#     >>> republic(['a', 'b', 'c'], [1, -1, 3])
#     ['c', 'c', 'c']
#     """
#     def republic_helper(______, ______, ______):
#         if ______:
#             return ______
#         if ______:
#             ______ = ______
#         else:
#             ______ = ______[:______]
#         return ______
#     return ______
