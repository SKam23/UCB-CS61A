import doctest
import sys
import argparse

"""
---USAGE---

python3 disc06.py <name_of_function>

e.g python3 disc06.py memory

---NOTES---

- if you pass all the doctests, you will get no terminal output
    - if you want to see the verbose output (all output shown even if the function is correct), run this:

    python3 disc06.py <name_of_function> -v

- if you want to test all of your functions, run this:

    python3 disc06.py all

"""

### Discussion 06 ###

#########
# Nonlocal
#########

# Q1.2
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    "*** UNCOMMENT SKELETON ***"
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

#########
# Midterm Review
#########

# RQ1
def in_nested(v, L):
    """Implement in_nested which takes in a value v and a nested list or an individual value L and returns whether
    the value is contained in the list.
    Hint: The built-in function type takes an object and returns the type of that object

    >>> in_nested(5, [1, 2, [[3], 4]])
    False
    >>> in_nested(9, [[[1], [6, 4, [5, [9]]], 7], 7, 7])
    True
    >>> in_nested(1, 1)
    True
    """
    "*** UNCOMMENT SKELETON ***"
    if type(L)== int:
        return v==L
    else:
        return any([in_nested(v,l) for l in L])

# RQ2
def factorize(n, k=2):
    """Implement factorize, which takes two integers n and k, both larger than 1. It returns the number
    of ways that n can be expressed as a product of non-decreasing integers greater than or equal to k.
    Return the number of ways to factorize positive integer n.

    >>> factorize(7) # 7
    1
    >>> factorize(12) # 2*2*3, 2*6, 3*4, 12
    4
    >>> factorize(36) # 2*2*3*3, 2*2*9, 2*3*6, 2*18, 3*3*4, 3*12, 4*9, 6*6, 36
    9
    """
    "*** UNCOMMENT SKELETON ***"
    if n==k:
        return 1
    elif k > n:
        return 0
    elif n%k!= 0:
        return factorize(n, k+1)
    return factorize(n//k,k)+factorize(n,k+1)

# RQ3
def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).

    >>> combo(531, 432)      # 45312 contains both _531_ and 4_3_2.
    45312
    >>> combo(531, 4321)     # 45321 contains both _53_1 and 4_321.
    45321
    >>> combo(1234, 9123)    # 91234 contains both _1234 and 9123_.
    91234
    >>> combo(0, 321)        # The number 0 has no digits, so 0 is not in the result.
    321
    """
    "*** UNCOMMENT SKELETON ***"
    if a == 0  or b ==0 :
        return a + b
    elif a%10==b%10:
        return combo(a//10, b//10)*10 +a%10
    return min(combo(a//10,b)*10 +a%10, combo(a,b//10)*10 +b%10)

# RQ4
def siblings(t):
    """Definition. A sibling of a node in a tree is another node with the same parent.
    Return a list of the labels of all nodes that have siblings in t.

    >>> a = tree(4, [tree(5), tree(6), tree(7, [tree(8)])])
    >>> siblings(tree(1, [tree(3, [a]), tree(9, [tree(10)])]))
    [3, 9, 5, 6, 7]
    """
    "*** UNCOMMENT SKELETON ***"
    result = [label(b) for b in branches(t) if len(branches(t))>1]
    for b in branches(t):
        result.extend(siblings(b))
    return result

# RQ5
def scurry(f, n):
    """Return a function that calls f on a list of arguments after being called n times.
    >>> scurry(sum, 4)(1)(1)(3)(2) # equivalent to sum([1, 1, 3, 2])
    7
    >>> scurry(len, 3)(7)([8])(-9) # equivalent to len([7, [8], -9])
    3
    """
    "*** UNCOMMENT SKELETON ***"
    # def h(k, args_so_far):
    #     if k == 0:
    #         return ________________________________________________________________________
    #     return ____________________________________________________________________________
    # return ________________________________________________________________________________

# Tree ADT

# Constructor
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selector
def label(tree):
    """Return the label value of a tree."""
    return tree[0]

# Selector
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

# For convenience
def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise."""
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
