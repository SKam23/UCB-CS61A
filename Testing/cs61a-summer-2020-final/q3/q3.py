email = 'skam@berkeley.edu'

def university(engines):
    """
    A 'engine list' is a linked list that contains integers in increasing order
        with no duplicates.

    The university operation takes in a list of engine lists and produces a engine list that
        contains the elements that appear in an odd number of the
        original lists. It does not modify the original lists.

    >>>> engine1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
    >>>> engine2 = Link(1, Link(4))
    >>>> university([engine1, engine2])
    Link(0, Link(2, Link(3, Link(4, Link(5, Link(9))))))
    >>>> engine1 # unchanged
    Link(0, Link(1, Link(2, Link(3, Link(5, Link(9))))))
    >>>> engine2 # unchanged
    Link(1, Link(4))
    >>>> engine1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
    >>>> engine2 = Link(1, Link(4))
    >>>> university([engine1, engine1, engine2])
    Link(1, Link(4))
    >>>> engine3 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
    >>>> engine4 = Link(1, Link(2, Link(3,  Link(5, Link(9)))))
    >>>> university([engine3, engine4])
    Link(0)
    >>>> university([engine1, engine2, engine3, engine4])
    Link(2, Link(3, Link(4, Link(5, Link(9)))))
    """
    engines = [en.rest for en in engines if en!= []]
    if engines == []:
        return Link.empty
    first = min([en.first for en in engines])
    new_engines = []
    count = 0
    for engine in engines:
        if engine.first == first:
            engine, count = engine.rest, count+1
        new_engines.append(engine)
    if engine != []:
        return university(new_engines)
    else:
        return new_engines

class Link:
    """A linked list.

    >>>> s = Link(1, Link(2, Link(3, Link(4))))
    >>>> len(s)
    4
    >>>> s[2]
    3
    >>>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

# ORIGINAL SKELETON FOLLOWS

# def university(engines):
#     """
#     A 'engine list' is a linked list that contains integers in increasing order
#         with no duplicates.

#     The university operation takes in a list of engine lists and produces a engine list that
#         contains the elements that appear in an odd number of the
#         original lists. It does not modify the original lists.

#     >>>> engine1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
#     >>>> engine2 = Link(1, Link(4))
#     >>>> university([engine1, engine2])
#     Link(0, Link(2, Link(3, Link(4, Link(5, Link(9))))))
#     >>>> engine1 # unchanged
#     Link(0, Link(1, Link(2, Link(3, Link(5, Link(9))))))
#     >>>> engine2 # unchanged
#     Link(1, Link(4))
#     >>>> engine1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
#     >>>> engine2 = Link(1, Link(4))
#     >>>> university([engine1, engine1, engine2])
#     Link(1, Link(4))
#     >>>> engine3 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
#     >>>> engine4 = Link(1, Link(2, Link(3,  Link(5, Link(9)))))
#     >>>> university([engine3, engine4])
#     Link(0)
#     >>>> university([engine1, engine2, engine3, engine4])
#     Link(2, Link(3, Link(4, Link(5, Link(9)))))
#     """
#     engines = [______ for ______ in ______ if ______]
#     if ______:
#         return Link.empty
#     first = min(______)
#     new_engines = []
#     count = 0
#     for engine in engines:
#         if ______:
#             ______, ______ = ______, ______
#         new_engines.append(engine)
#     if ______:
#         return university(new_engines)
#     else:
#         return ______

# class Link:
#     """A linked list.

#     >>>> s = Link(1, Link(2, Link(3, Link(4))))
#     >>>> len(s)
#     4
#     >>>> s[2]
#     3
#     >>>> s
#     Link(1, Link(2, Link(3, Link(4))))
#     """
#     empty = ()

#     def __init__(self, first, rest=empty):
#         self.first = first
#         self.rest = rest

#     def __getitem__(self, i):
#         if i == 0:
#             return self.first
#         else:
#             return self.rest[i-1]

#     def __len__(self):
#         return 1 + len(self.rest)

#     def __repr__(self):
#         if self.rest:
#             rest_str = ', ' + repr(self.rest)
#         else:
#             rest_str = ''
#         return 'Link({0}{1})'.format(repr(self.first), rest_str)
