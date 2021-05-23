email = 'skam@berkeley.edu'

def subdrama(hall):
    """
    A 'drama' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
        1
        4444
        7777777

    Note that `1 <= d <= 9`; there are no 0-length dramas.

    Your task is to implement the `subdrama` function, which takes in an integer `hall` and returns
        whether `hall` contains a drama as a consecutive subinteger of its digits.

    >>> subdrama(2233) # 22 counts
    True
    >>> subdrama(2444423) # 4444 counts
    True
    >>> subdrama(82223) # 22 counts even if it appears as part of 222
    True
    >>> subdrama(234562) # 2...2 does not count if the 2s are not consecutive
    False
    >>> subdrama(1) # 1 counts
    True
    >>> subdrama(498729879871) # 1 counts
    True
    >>> subdrama(149872987987) # 1 counts
    True
    >>> subdrama(4445555) # no dramas in this number
    False
    >>> subdrama(20) # no dramas in this number
    False
    """
    current_digit = hall%10
    count = 0
    while hall >0:
        last = hall%10
        if last==current_digit:
            count += 1
        else:
            count = 1
            current_digit = hall%10
        if count==current_digit :
            return True
        hall = hall//10
    return False

# ORIGINAL SKELETON FOLLOWS

# def subdrama(hall):
#     """
#     A 'drama' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
#         1
#         4444
#         7777777

#     Note that `1 <= d <= 9`; there are no 0-length dramas.

#     Your task is to implement the `subdrama` function, which takes in an integer `hall` and returns
#         whether `hall` contains a drama as a consecutive subinteger of its digits.

#     >>> subdrama(2233) # 22 counts
#     True
#     >>> subdrama(2444423) # 4444 counts
#     True
#     >>> subdrama(82223) # 22 counts even if it appears as part of 222
#     True
#     >>> subdrama(234562) # 2...2 does not count if the 2s are not consecutive
#     False
#     >>> subdrama(1) # 1 counts
#     True
#     >>> subdrama(498729879871) # 1 counts
#     True
#     >>> subdrama(149872987987) # 1 counts
#     True
#     >>> subdrama(4445555) # no dramas in this number
#     False
#     >>> subdrama(20) # no dramas in this number
#     False
#     """
#     current_digit = ______
#     count = ______
#     while ______:
#         last = ______
#         if ______:
#             count += 1
#         else:
#             count = ______
#             ______
#         if ______:
#             ______
#         hall = ______
#     return ______
