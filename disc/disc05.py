import doctest
import sys
import argparse

"""
---USAGE---

python3 disc05.py <name_of_function>

e.g python3 disc05.py height

---NOTES---

- if you pass all the doctests, you will get no terminal output
    - if you want to see the verbose output (all output shown even if the function is correct), run this:

    python3 disc05.py <name_of_function> -v

- if you want to test all of your functions, run this:

    python3 disc05.py all

"""

### Discussion 05 ###

#########
# Trees
#########

# Q1.1
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    "*** UNCOMMENT SKELETON ***"
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])

# Q1.2
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                    [tree(2,
    ...                            [tree(3),
    ...                            tree(4)]),
    ...                    tree(5,
    ...                        [tree(6,
    ...                                [tree(7)]),
    ...                        tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    "*** YOUR CODE HERE ***"

# Q1.3
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    "*** UNCOMMENT SKELETON ***"
    if label(tree) == x:
        return [x]
    for b in brances(tree):
        path = find_path(b,x)
        if path:
            return [label(tree)]+path

# Q1.4
# Don't test this function until you've tried filling out the blanks,
# since the output will show you the correct answers.
def tree_wwpd():
    """
    >>> t = tree(1, [tree(2), tree(3)])
    >>> label(t)
    ____________________
    >>> t[0]
    ____________________
    >>> label(branches(t)[0])
    ____________________
    >>> label(branches(t))
    ____________________
    >>> is_leaf(t[1:][1])
    ____________________
    >>> [label(b) for b in branches(t)]
    ____________________
    >>> branches(tree(2, tree(t, [])))[0] # Challenge
    ____________________
    """
    pass

#########
# Mutation
#########

"""
>>> pizza = ['cheese', 'mushrooms']

>>> new_pizza = pizza + ['onions'] # creates a new Python list
>>> new_pizza
['cheese', 'mushrooms', 'onions']
>>> pizza # the original list is unmodified
['cheese', 'mushrooms']

>>> pizza.append('onions')
>>> pizza
['cheese', 'mushrooms', 'onions']

>>> pizza[1] = 'tomatoes'
>>> pizza
['cheese', 'tomatoes', 'onions']
"""

# Q2.1
# Don't test this function until you've tried filling out the blanks,
# since the output will show you the correct answers.
def list_wwpd():
    """
    >>> lst1 = [1, 2, 3]
    ____________________
    >>> lst2 = lst1
    ____________________
    >>> lst1 is lst2
    ____________________
    >>> lst2.extend([5, 6])
    ____________________
    >>> lst1[4]
    ____________________
    >>> lst1.append([-1, 0, 1])
    ____________________
    >>> -1 in lst1
    ____________________
    >>> lst2[5]
    ____________________
    >>> lst3 = lst2[:]
    ____________________
    >>> lst3.insert(3, lst2.pop(3))
    ____________________
    >>> len(lst1)
    ____________________
    >>> lst1[4] is lst3[6]
    ____________________
    >>> lst3[lst2[4][1]]
    ____________________
    >>> lst1[:3] is lst2[:3]
    ____________________
    >>> lst1[:3] == lst2[:3]
    ____________________
    >>> x = (1, 2, [4, 5, 6])
    ____________________
    >>> x[2] = [3, 5, 6]
    ____________________
    >>> x
    ____________________
    >>> x[2][0] = 3
    ____________________
    >>> x
    ____________________
    """
    pass

# Q2.2
def add_this_many(x, el, lst):
    """Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** UNCOMMENT SKELETON ***"
    # count = 0
    # ____________________:
    #     ____________________:
    #         ____________________
    # ____________________:
    #     ____________________
    #     ____________________

# Q2.3
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> result = group_by(range(-3, 4), lambda x: x * x)
    >>> {key:result[key] for key in sorted(result.keys())} # sorting by keys in increasing order
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    "*** UNCOMMENT SKELETON ***"
    # grouped = {}
    # ____________________:
    #     ____________________
    #     if ____________________:
    #         ____________________
    #     else:
    #         ____________________
    # return grouped

# Quiz
# Part a
def partition_options(total, biggest):
    """
    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """
    "*** UNCOMMENT SKELETON ***"
    # if _________________________________________________________:
    #     return _________________________________
    # elif _______________________________________________________:
    #     return _________________________________
    # else:
    #     with_biggest = __________________________________________
    #     without_biggest = _______________________________________
    #     ____________ = [[_________]______________________________]
    #     return with_biggest + without_biggest

# Part b
def min_elements(T, lst):
    """
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 1]) # 4 + 4 + 4
    3
    >>> min_elements(0, [1, 2, 3])
    0
    """
    "*** UNCOMMENT SKELETON ***"
    # if _________________________________________________________:
    #     return _________________________________
    # return _________________________________________________________________________________

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

### For running tests only. Not part of discussion content ###

parser = argparse.ArgumentParser(description="Test your work")
parser.add_argument("func", metavar="function_to_test", help="Function to be tested")
parser.add_argument("-v", dest="v", action="store_const", const=True, default=False, help="Verbose output")
args = parser.parse_args()
try:
    if args.func == "all":
        if args.v:
            doctest.testmod(verbose=True)
        else:
            doctest.testmod()
    else:
        if args.v:
            doctest.run_docstring_examples(globals()[args.func], globals(), verbose=True, name=args.func)
        else:
            doctest.run_docstring_examples(globals()[args.func], globals(), name=args.func)
except:
    sys.exit("Invalid Arguments")
