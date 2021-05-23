email = 'skam@berkeley.edu'

"""
Su 16 Final q4
Implement the function catch up, which takes in two linked lists of integers lnk1 and lnk2 and mutates the
linked list with the lower sum by repeatedly inserting 1 at the end until the sums are equal. See the doctests
for details. You may assume that the two linked lists that are passed in are non-empty and have
the same length. The Link class is provided for your reference.

You may only use the lines provided. You may not need to fill all the lines. You may not use
methods that are not implemented in the Link class below.
Hint: You may need the ternary operator <expr1> if <cond> else <expr2>.
"""

def catch_up(lnk1, lnk2):
    """
    >>> odds = Link (1 , Link (3 , Link (5 , Link (7))))
    >>> evens = Link (2 , Link (4 , Link (6 , Link (8))))
    >>> catch_up (odds , evens )
    >>> print ( odds ) # odds is mutated
    <1 3 5 7 1 1 1 1>
    >>> print ( evens )
    <2 4 6 8>
    """

    def catcher(lnk1, lnk2, sum1, sum2):
        sum1 = lnk1.first + sum1
        sum2 = lnk2.first + sum2
        if lnk1.rest is Link.empty:
            lower = lnk1 if sum1<sum2 else lnk2
            for _ in range(abs(sum1-sum2)):
                lower.rest = Link(1)
                lower = lower.rest
        else :
            catcher(lnk1.rest, lnk2.rest , sum1, sum2)
    catcher(lnk1, lnk2, 0, 0 )


### Reference Code for Trees/Linked Lists ###

class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __str__ (self):
        string = '<'
        while self.rest is not Link.empty :
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# ORIGINAL SKELETON FOLLOWS

# """
# Su 16 Final q4
# Implement the function catch up, which takes in two linked lists of integers lnk1 and lnk2 and mutates the
# linked list with the lower sum by repeatedly inserting 1 at the end until the sums are equal. See the doctests
# for details. You may assume that the two linked lists that are passed in are non-empty and have
# the same length. The Link class is provided for your reference.

# You may only use the lines provided. You may not need to fill all the lines. You may not use
# methods that are not implemented in the Link class below.
# Hint: You may need the ternary operator <expr1> if <cond> else <expr2>.
# """

# def catch_up(lnk1, lnk2):
#     """
#     >>> odds = Link (1 , Link (3 , Link (5 , Link (7))))
#     >>> evens = Link (2 , Link (4 , Link (6 , Link (8))))
#     >>> catch_up (odds , evens )
#     >>> print ( odds ) # odds is mutated
#     <1 3 5 7 1 1 1 1>
#     >>> print ( evens )
#     <2 4 6 8>
#     """

#     def catcher(lnk1, lnk2, sum1, sum2):
#         sum1 = ______
#         sum2 = ______
#         if ______:
#             lower = ______
#             for ______ in ______:
#                 ______ = Link(1)
#                 ______
#         else :
#             catcher(______)
#     catcher(______)


# ### Reference Code for Trees/Linked Lists ###

# class Link:
#     """A linked list with a first element and the rest."""
#     empty = ()
#     def __init__(self, first, rest=empty):
#         assert rest is Link.empty or isinstance(rest, Link)
#         self.first = first
#         self.rest = rest
#     def __str__ (self):
#         string = '<'
#         while self.rest is not Link.empty :
#             string += str(self.first) + ' '
#             self = self.rest
#         return string + str(self.first) + '>'
