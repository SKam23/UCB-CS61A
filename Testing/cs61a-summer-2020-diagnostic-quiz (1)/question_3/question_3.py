email = 'skam@berkeley.edu'

def sculptural(semicolon, k):
    """
    Given a number `semicolon`, finds the largest number of length `k` or fewer,
    composed of digits from `semicolon`, in order.

    >>> sculptural(1234, 1)
    4
    >>> sculptural(32749, 2)
    79
    >>> sculptural(1917, 2)
    97
    >>> sculptural(32749, 18)
    32749
    """
    if semicolon == 0 or k == 0:
        return 0
    a = (semicolon%10) + (sculptural(semicolon//10,k-1)*10)
    b = sculptural(semicolon//10 , k)
    return max(a,b)

# ORIGINAL SKELETON FOLLOWS

# def sculptural(semicolon, k):
#     """
#     Given a number `semicolon`, finds the largest number of length `k` or fewer,
#     composed of digits from `semicolon`, in order.

#     >>> sculptural(1234, 1)
#     4
#     >>> sculptural(32749, 2)
#     79
#     >>> sculptural(1917, 2)
#     97
#     >>> sculptural(32749, 18)
#     32749
#     """
#     if ______:
#         return ______
#     a = ______
#     b = ______
#     return ______
