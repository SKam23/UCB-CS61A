email = 'skam@berkeley.edu'

"""
Su 19 Final q4
This question is in three parts, implementing `is_combo`, 'apply_tree', and
'make_checker_tree'. See the specifications in each definition for details.

Definition. A combo of a non-negative integer n is the result of adding or multiplying the digits of n from
left to right, starting with 0. For n = 357, combos include 15 = (((0 + 3) + 5) + 7), 35 = (((0 ∗ 3) + 5) ∗ 7), and
0 = (((0 ∗ 3) ∗ 5) ∗ 7), as well as 0, 7, 12, 22, 56, and 105. But 36 = ((0 + 3) ∗ (5 + 7)) is not a combo of 357.
"""

"""
Part (a) (6 pt)
Implement is_combo, which takes non-negative integers n and k. It returns whether k is a combo of
n. You may assume that 0 is not one of the digits of n.

Run tests for just this part with
    python3 ok -q a
"""

def is_combo(n, k):
    """Is k a combo of n?
    >>> [k for k in range(1000) if is_combo(357, k)]
    [0, 7, 12, 15, 22, 35, 56, 105]
    """
    assert n >= 0 and k >= 0
    if k==0:
        return True
    if n==0:
        return False
    rest, last = n // 10, n % 10
    added = k-last>=0 and is_combo(rest, k-last)
    multiplied = k/last >0 and is_combo(rest, k/last)
    return added or multiplied

"""
Part (b) (4 pt)
Implement apply_tree, which takes in two trees. The labels of the first tree are all functions.
apply_tree should mutate the the second tree such that each label is the result of applying each function
in the first tree to the corresponding node in the second tree.
You may assume the two trees have the same shape (that is, each node has the same number of children).

Run tests for just this part with
    python3 ok -q b
"""

def apply_tree(fn_tree, val_tree):
    """ Mutates val_tree by applying each function stored in fn_tree
    to the corresponding labels in val_tree
    >>> double = lambda x: x*2
    >>> square = lambda x: x**2
    >>> identity = lambda x: x
    >>> t1 = Tree(double, [Tree(square), Tree(identity)])
    >>> t2 = Tree(6, [Tree(2), Tree(10)])
    >>> apply_tree(t1, t2)
    >>> t2
    Tree(12, [Tree(4), Tree(10)])
    """
    val_tree.label = fn_tree.label(val_tree.label)
    for i in range(len(val_tree.branches)):
        apply_tree(fn_tree.branches[i], val_tree.branches[i])

"""
Part (c) (4 pt) Implement make_checker_tree which takes in a tree, t containing digits as its labels and returns a
tree with functions as labels (a function tree). When applied to another tree, the function tree should mutate
it so each label is True if the label is a combo of the number formed by concatenating the labels from the
root to the corresponding node of t. You may use is_combo in your solution.
The default argument for make_checker_tree is part of the solution, but will not be present in the initial call.

Run tests for just this part with
    python3 ok -q c
"""

def make_checker_tree(t, so_far=0):
    """ Returns a function tree that, when applied to another tree, will mutate its labels to be
    True if the label is a combination of the path in t from the root to its corresponding node.
    >>> t1 = Tree(5, [Tree(2), Tree(1)])
    >>> fn_tree = make_checker_tree(t1)
    >>> t2 = Tree(5, [Tree(10), Tree(7)])
    >>> apply_tree(fn_tree, t2) #5 is a combo of 5, 10 is a combo of 52, 7 isn't a combo of 51
    >>> t2
    Tree(True, [Tree(True), Tree(False)])
    """
    new_path = so_far *10 +t.label
    branches = [make_checker_tree(b, new_path) for b in t.branches]
    fn = lambda k : is_combo(new_path, k)
    return Tree(fn, branches)

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

    def is_leaf(self):
        return not self.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = ' ' * (4 * indent) + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def __repr__(self):
        if self.branches:
            return "Tree({}, {})".format(self.label, self.branches)
        return "Tree({})".format(self.label)


# ORIGINAL SKELETON FOLLOWS

# """
# Su 19 Final q4
# This question is in three parts, implementing `is_combo`, 'apply_tree', and
# 'make_checker_tree'. See the specifications in each definition for details.

# Definition. A combo of a non-negative integer n is the result of adding or multiplying the digits of n from
# left to right, starting with 0. For n = 357, combos include 15 = (((0 + 3) + 5) + 7), 35 = (((0 ∗ 3) + 5) ∗ 7), and
# 0 = (((0 ∗ 3) ∗ 5) ∗ 7), as well as 0, 7, 12, 22, 56, and 105. But 36 = ((0 + 3) ∗ (5 + 7)) is not a combo of 357.
# """

# """
# Part (a) (6 pt)
# Implement is_combo, which takes non-negative integers n and k. It returns whether k is a combo of
# n. You may assume that 0 is not one of the digits of n.

# Run tests for just this part with
#     python3 ok -q a
# """

# def is_combo(n, k):
#     """Is k a combo of n?
#     >>> [k for k in range(1000) if is_combo(357, k)]
#     [0, 7, 12, 15, 22, 35, 56, 105]
#     """
#     assert n >= 0 and k >= 0
#     if ______:
#         return True
#     if ______:
#         return False
#     rest, last = n // 10, n % 10
#     added = ______ and is_combo(______, ______)
#     multiplied = ______ and is_combo(______, ______)
#     return added or multiplied

# """
# Part (b) (4 pt)
# Implement apply_tree, which takes in two trees. The labels of the first tree are all functions.
# apply_tree should mutate the the second tree such that each label is the result of applying each function
# in the first tree to the corresponding node in the second tree.
# You may assume the two trees have the same shape (that is, each node has the same number of children).

# Run tests for just this part with
#     python3 ok -q b
# """

# def apply_tree(fn_tree, val_tree):
#     """ Mutates val_tree by applying each function stored in fn_tree
#     to the corresponding labels in val_tree
#     >>> double = lambda x: x*2
#     >>> square = lambda x: x**2
#     >>> identity = lambda x: x
#     >>> t1 = Tree(double, [Tree(square), Tree(identity)])
#     >>> t2 = Tree(6, [Tree(2), Tree(10)])
#     >>> apply_tree(t1, t2)
#     >>> t2
#     Tree(12, [Tree(4), Tree(10)])
#     """
#     ______
#     for ______ in ______:
#         ______

# """
# Part (c) (4 pt) Implement make_checker_tree which takes in a tree, t containing digits as its labels and returns a
# tree with functions as labels (a function tree). When applied to another tree, the function tree should mutate
# it so each label is True if the label is a combo of the number formed by concatenating the labels from the
# root to the corresponding node of t. You may use is_combo in your solution.
# The default argument for make_checker_tree is part of the solution, but will not be present in the initial call.

# Run tests for just this part with
#     python3 ok -q c
# """

# def make_checker_tree(t, so_far=0):
#     """ Returns a function tree that, when applied to another tree, will mutate its labels to be
#     True if the label is a combination of the path in t from the root to its corresponding node.
#     >>> t1 = Tree(5, [Tree(2), Tree(1)])
#     >>> fn_tree = make_checker_tree(t1)
#     >>> t2 = Tree(5, [Tree(10), Tree(7)])
#     >>> apply_tree(fn_tree, t2) #5 is a combo of 5, 10 is a combo of 52, 7 isn't a combo of 51
#     >>> t2
#     Tree(True, [Tree(True), Tree(False)])
#     """
#     new_path = ______
#     branches = ______
#     fn = ______
#     return Tree(fn, branches)

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

#     def is_leaf(self):
#         return not self.branches

#     def __str__(self):
#         def print_tree(t, indent=0):
#             tree_str = ' ' * (4 * indent) + str(t.label) + "\n"
#             for b in t.branches:
#                 tree_str += print_tree(b, indent + 1)
#             return tree_str
#         return print_tree(self).rstrip()

#     def __repr__(self):
#         if self.branches:
#             return "Tree({}, {})".format(self.label, self.branches)
#         return "Tree({})".format(self.label)

