email = 'skam@berkeley.edu'

"""
Sp 16 Final q10
This question is in two parts, implementing `tree_search` and
the `categorize` method of the Organizer class. See the specifications
in each definition for details.
"""
"""
Part (a)

Fill in the tree_search function so that tree_search(t, pred) returns a linked list of all labels in
t (of type Tree) that satisfy pred (that is, for which the one-argument function pred returns a true value).
The order of the list is irrelevant.

Run tests for just this part with
    python3 ok -q a
"""
def tree_search(t, pred):
    """
    Returns a linked list ( type Link ) of labels in Tree t that
    satisfy PRED.
    >>> t = Tree(4, [Tree(5, [Tree(6, [Tree(5)])]), Tree(1, [])])
    >>> tree_search(t, lambda x: x % 2 == 1)
    Link(1, Link(5, Link(5)))
    """
    L = Link.empty
    def subtree_search(subtr):
        nonlocal L # Hint: nonlocal may be helpful in this line!
        if pred(subtr.label):
            L = Link( subtr.label, L)
        for b in subtr.branches:
            subtree_search(b)
    subtree_search(t)
    return L

"""
Part (b)

An Organizer is a kind of object that divides the labels in a tree into a sequence of disjoint lists, one for
each of a given set of categories. To create an Organizer, one provides a sequence of predicates (one-argument
functions) that define the categories. When this object is subsequently handed a Tree, it will return a sequence
of linked lists of tree labels, one per category in the same order as the original sequence of category predicates.
Once a tree label is included in one list, it must not appear again in that list, nor in any subsequent list. Fill
in the class below to fulfill this specification. You may assume that labels are numbers or strings.
"""
class Organizer:
    def __init__(self, categories):
        """ Create a new Organizer whose categories are defined by the
        predicates in CATEGORIES ( an iterable ). """
        self._categories = categories

    def categorize(self, t):
        """ Return a Python sequence of linked lists , where the kth
        list contains tree labels from TR that satisfy my kth
        category. Each tree label appears exactly once in the entire
        set of lists returned , regardless of how often it occurs in TR.
        NOTE : The order of values in the linked lists in the example
        below is just one possible result .
        >>> t = Tree(6, [Tree(3, [Tree(5, [Tree(9), Tree(2, [Tree(9)])]), Tree(1)]), Tree(4, [Tree(0, [Tree(4)])])])
        >>> org = Organizer([lambda x: x > 4, lambda x: x % 2 == 0])
        >>> org.categorize(t)
        [Link(9, Link(5, Link(6))), Link(0, Link(4, Link(2)))]
        """
        result = []
        labels_seen = set()
        def take_it(x): # Hint: you can see pred within take_it
            if x not in labels_seen and pred(x):
                labels_seen.add(x)
                return True
            return False
        for pred in self._categories:
            result.append(tree_search(t, take_it))
        return result

### Reference Code for Trees/Linked Lists ###

class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
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
        """Return a string that would evaluate to self."""
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({0}{1})'.format(self.first, rest)

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def is_leaf(self):
        return not self.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = ' ' * (4 * indent) + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

# ORIGINAL SKELETON FOLLOWS

# """
# Sp 16 Final q10
# This question is in two parts, implementing `tree_search` and
# the `categorize` method of the Organizer class. See the specifications
# in each definition for details.
# """
# """
# Part (a)

# Fill in the tree_search function so that tree_search(t, pred) returns a linked list of all labels in
# t (of type Tree) that satisfy pred (that is, for which the one-argument function pred returns a true value).
# The order of the list is irrelevant.

# Run tests for just this part with
#     python3 ok -q a
# """
# def tree_search(t, pred):
#     """
#     Returns a linked list ( type Link ) of labels in Tree t that
#     satisfy PRED.
#     >>> t = Tree(4, [Tree(5, [Tree(6, [Tree(5)])]), Tree(1, [])])
#     >>> tree_search(t, lambda x: x % 2 == 1)
#     Link(1, Link(5, Link(5)))
#     """
#     L = ______
#     def subtree_search(subtr):
#         ______ # Hint: nonlocal may be helpful in this line!
#         if ______:
#             L = ______
#         for ______ in ______:
#             ______
#     ______
#     return L

# """
# Part (b)

# An Organizer is a kind of object that divides the labels in a tree into a sequence of disjoint lists, one for
# each of a given set of categories. To create an Organizer, one provides a sequence of predicates (one-argument
# functions) that define the categories. When this object is subsequently handed a Tree, it will return a sequence
# of linked lists of tree labels, one per category in the same order as the original sequence of category predicates.
# Once a tree label is included in one list, it must not appear again in that list, nor in any subsequent list. Fill
# in the class below to fulfill this specification. You may assume that labels are numbers or strings.
# """
# class Organizer:
#     def __init__(self, categories):
#         """ Create a new Organizer whose categories are defined by the
#         predicates in CATEGORIES ( an iterable ). """
#         self._categories = categories

#     def categorize(self, t):
#         """ Return a Python sequence of linked lists , where the kth
#         list contains tree labels from TR that satisfy my kth
#         category. Each tree label appears exactly once in the entire
#         set of lists returned , regardless of how often it occurs in TR.
#         NOTE : The order of values in the linked lists in the example
#         below is just one possible result .
#         >>> t = Tree(6, [Tree(3, [Tree(5, [Tree(9), Tree(2, [Tree(9)])]), Tree(1)]), Tree(4, [Tree(0, [Tree(4)])])])
#         >>> org = Organizer([lambda x: x > 4, lambda x: x % 2 == 0])
#         >>> org.categorize(t)
#         [Link(9, Link(5, Link(6))), Link(0, Link(4, Link(2)))]
#         """
#         result = []
#         labels_seen = ______
#         def take_it(x): # Hint: you can see pred within take_it
#             if ______ and ______:
#                 ______
#                 return True
#             return False
#         for pred in ______:
#             result.append(tree_search(t, take_it))
#         return result

# ### Reference Code for Trees/Linked Lists ###

# class Link:
#     """A linked list with a first element and the rest."""
#     empty = ()
#     def __init__(self, first, rest=empty):
#         assert rest is Link.empty or isinstance(rest, Link)
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
#         """Return a string that would evaluate to self."""
#         if self.rest is Link.empty:
#             rest = ''
#         else:
#             rest = ', ' + repr(self.rest)
#         return 'Link({0}{1})'.format(self.first, rest)

# class Tree:
#     """
#     >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
#     >>> t.label
#     3
#     >>> t.branches[0].label
#     2
#     >>> t.branches[1].is_leaf()
#     True
#     """
#     def __init__(self, label, branches=[]):
#         for b in branches:
#             assert isinstance(b, Tree)
#         self.label = label
#         self.branches = list(branches)

#     def __repr__(self):
#         if self.branches:
#             return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
#         else:
#             return 'Tree({0})'.format(repr(self.label))

#     def is_leaf(self):
#         return not self.branches

#     def __str__(self):
#         def print_tree(t, indent=0):
#             tree_str = ' ' * (4 * indent) + str(t.label) + "\n"
#             for b in t.branches:
#                 tree_str += print_tree(b, indent + 1)
#             return tree_str
#         return print_tree(self).rstrip()
