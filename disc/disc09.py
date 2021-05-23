import doctest
import sys
import argparse
from operator import mul

"""
---USAGE---

python3 disc09.py <name_of_function>

e.g. python3 disc09.py sum_nums

---NOTES---

- if you pass all the doctests, you will get no terminal output
    - if you want to see the verbose output (all output shown even if the function is correct), run this:

    python3 disc09.py <name_of_function> -v

- if you want to test all of your functions, run this:

    python3 disc09.py all

"""

### Discussion 09 ###

########################
###   Linked Lists   ###
########################

# Q1.1
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** UNCOMMENT SKELETON ***"
    if lnk == Link.empty:
        return 0
    return lnk.first +  sum_nums(lnk.rest)

# Q1.2
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    "*** YOUR CODE HERE ***"
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    return Link(product, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))

# Q1.3a
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    Traceback (most recent call last):
        ...
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link !=  Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

# Q1.3b
def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link == Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)

#################
###   Trees   ###
#################

# Tree Class

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

# Q2.1
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** UNCOMMENT SKELETON ***"
    if t.label %2 != 0:
        t.label += 1
    for b in t.branches:
        make_even(b)

# Q2.2
def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    "*** UNCOMMENT SKELETON ***"
    # ____________
    # ____________:
    #     ____________

# Q2.3
def find_path(t, entry):
    """Return a list containing the nodes along the path
    required to get from the root of t to entry. If entry
    is not present in t, return False. Assume that the
    elements in t are unique. Find the path to an element.

    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1)])
    >>> find_path(tree_ex, 5)
    [2, 7, 6, 5]
    """
    "*** UNCOMMENT SKELETON ***"
    if t.label == entry:
        return [entry]
    for b in t.branches:
        path = find_path(b,entry)
        if path:
            return [t.label] + path
    return False

# Q2.4
def average(t):
    """
    Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    "*** UNCOMMENT SKELETON ***"
    # def sum_helper(t):
    #     total, count = _______________________________________________________________
    #     for __________________________________________________________________________:
    #         __________________________________________________________________________
    #         __________________________________________________________________________
    #         __________________________________________________________________________
    #     return total, count
    # total, count = ___________________________________________________________________
    # return total / count

# Q2.5
def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    "*** YOUR CODE HERE ***"

# Q2.6
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    "*** YOUR CODE HERE ***"

# Link Class

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Tree Class

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

# Tree ADT (For comparison)

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
