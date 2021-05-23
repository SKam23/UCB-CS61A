email = 'skam@berkeley.edu'

def compress(kale, spinach):
    """
    Write a function compress that takes in two lists of positive integers,
        kale and spinach, and determines if kale can be compressed into spinach.

    A compression is when two adjacent elements in the list are either addded or
        subtracted from each other to form one single new element.

    For example, for the list [1,2,1] the first compression could result in either

        [3, 1] (adding)
        [-1, 1] (subtraction)

    >>>> compress([1,1,1], [3])
    True
    >>>> compress([1,1,1], [2])
    False
    >>>> compress([1,1,1], [1])
    True
    >>>> compress([1,2,3], [1,5])
    True
    >>>> compress([1,2,3], [2])
    True
    >>>> compress([], [1,2,3])
    False
    >>>> compress([1,2,3], [])
    False
    >>>> compress([], [])
    True
    >>>> compress([1,4,2,8,3,9,4], [31])
    True
    >>>> compress([1,4,2,8,3,9,4], [3,5,5])
    True
    """
    if kale == spinach:
        return True
    elif kale == [] or len(kale) <= 2  :
        return False
    compress_add = compress(([kale[0]+kale[1]])+(kale[2:]), spinach)
    compress_sub = compress(([kale[0]-kale[1]])+(kale[2:]), spinach)
    compress_eq = kale[0]==spinach[0] and compress(kale[1:], spinach[1:] )
    return compress_add or compress_sub or compress_eq

# ORIGINAL SKELETON FOLLOWS

# def compress(kale, spinach):
#     """
#     Write a function compress that takes in two lists of positive integers,
#         kale and spinach, and determines if kale can be compressed into spinach.

#     A compression is when two adjacent elements in the list are either addded or
#         subtracted from each other to form one single new element.

#     For example, for the list [1,2,1] the first compression could result in either

#         [3, 1] (adding)
#         [-1, 1] (subtraction)

#     >>>> compress([1,1,1], [3])
#     True
#     >>>> compress([1,1,1], [2])
#     False
#     >>>> compress([1,1,1], [1])
#     True
#     >>>> compress([1,2,3], [1,5])
#     True
#     >>>> compress([1,2,3], [2])
#     True
#     >>>> compress([], [1,2,3])
#     False
#     >>>> compress([1,2,3], [])
#     False
#     >>>> compress([], [])
#     True
#     >>>> compress([1,4,2,8,3,9,4], [31])
#     True
#     >>>> compress([1,4,2,8,3,9,4], [3,5,5])
#     True
#     """
#     if ______ == ______:
#         return ______
#     elif ______ or ______:
#         return ______
#     compress_add = ______
#     compress_sub = ______
#     compress_eq = ______ and ______
#     return ______
