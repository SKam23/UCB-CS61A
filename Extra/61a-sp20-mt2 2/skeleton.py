##############
# QUESTION 1 #
##############

"""This question involves plucking the leaves off a tree one by one.

Definitions:

1) A "number tree" is a Tree whose labels are _unique_ positive integers.
   No repeated labels appear in a number tree.

2) A "plucking order" for a number tree t is a sequence of unique positive
   integers that are all labels of t.

3) A plucking order is "valid" if both of these conditions are true:
   (a) the plucking order contains all labels of t, and
   (b) in the plucking order, the label for each node of t appears after
       the labels of all its descendant nodes. Thus, leaves appear first.

Note: redwood, pine, and cyprus are all kinds of trees.
"""

"""A: (3 pts) Implement order, which takes a number tree called redwood. It returns
a valid plucking order as a list of numbers. If there is more than one valid
plucking order for redwood, your order function can return any one of them.

IMPORTANT: You do not need to return EVERY valid plucking order; just one.

Check the doctests with: python3 ok -q a
"""
def order(redwood):
    """Return a list containing a valid plucking order for the labels of t.

    >>> order(Tree(1, [Tree(2, [Tree(3, [Tree(4)])])]))               # The only valid plucking order.
    [4, 3, 2, 1]
    >>> order(Tree(1, [Tree(2), Tree(3)])) in [[2, 3, 1], [3, 2, 1]]  # There are 2 valid orders.
    True
    >>> o = order(Tree(1, [Tree(2, [Tree(3)]), Tree(4, [Tree(5)])]))  # There are many valid orders,
    >>> o.index(5) < o.index(4)                                       # but all have 5 before 4,
    True
    >>> o.index(3) < o.index(2)                                       # and 3 before 2,
    True
    >>> o[4:]                                                         # and 1 at the end.
    [1]

    >>> order(Tree(7, [Tree(4, [Tree(6)]), Tree(5)])) in [[6, 5, 4, 7], [5, 6, 4, 7], [6, 4, 5, 7]]
    True
    """
    plucking_order = []
    for b in branches(redwood):
        plucking_order += order(b)
    return plucking_order + label(redwood)

    # ORIGINAL TEMPLATE for your reference (do not edit this part)
    # for b in _____:
    #     _____
    # return _____


"""B: (5 pts) Implement pluck, which takes a number tree called pine and returns
a function that is called repeatedly on the elements of a plucking order. If that
plucking order is valid, the final call returns 'success!'. Otherwise, if one of
the repeated calls is on a number that is not part of a valid plucking order, the
error string 'Hey, not valid!' is returned.

Since pine is a number tree and the values passed to plucker form a plucking
order, you can assume that:
- The labels of pine are unique,
- All values k passed to the plucker function are unique for a given pine, and
- All values k are labels of pine.

Check the doctests with: python3 ok -q b
"""
def pluck(pine):
    """Return a function that returns whether a plucking order is valid
    for a number tree t when called repeatedly on elements of a plucking order.

    Calling the function returned by pluck should not mutate pine.

           +---+
           | 1 |
           +---+
           /   \----\
          /          \
       +---+         +---+
       | 2 |         | 6 |
       +---+         +---+
         |            / \
         |           /   \
       +---+      +---+ +---+
       | 3 |      | 7 | | 8 |
       +---+      +---+ +---+
        / \               |
       /   \              |
    +---+ +---+         +---+
    | 4 | | 5 |         | 9 |
    +---+ +---+         +---+

    >>> b0 = Tree(2, [Tree(3, [Tree(4), Tree(5)])])
    >>> b1 = Tree(6, [Tree(7), Tree(8, [Tree(9)])])
    >>> t = Tree(1, [b0, b1])
    >>> pluck(t)(9)(8)(7)(6)(5)(4)(3)(2)(1)
    'success!'
    >>> pluck(t)(5)(9)(4)(7)(3)(8)(6)(2)(1)
    'success!'
    >>> pluck(t)(2)
    'Hey, not valid!'
    >>> pluck(t)(5)(9)(7)(6)
    'Hey, not valid!'

    >>> pluck(b0)(5)(2)
    'Hey, not valid!'
    >>> pluck(b0)(4)(5)(3)(2)
    'success!'
    """
    def plucker(k):
        def pluck_one_leaf(cyprus):
            """Return a copy of cyprus without leaf k and check that k is a
            leaf label, not an interior node label.
            """
            if _____:
                _____
            plucked_branches = []
            for b in cyprus.branches:
                skip_this_leaf = _____ and _____
                if not skip_this_leaf:
                    plucked_branch_or_error = pluck_one_leaf(b)
                    if isinstance(plucked_branch_or_error, str):
                        return plucked_branch_or_error
                    else:
                        _____
            return Tree(_____, plucked_branches)
        nonlocal pine
        if pine.is_leaf():
            assert k == pine.label, 'all k must appear in pine'
            return 'success!'
        _____
        if isinstance(pine, str):
            return pine
        return plucker
    return plucker

    # ORIGINAL TEMPLATE for your reference (do not edit this part)
    #         if _____:
    #             _____
    #         plucked_branches = []
    #         for b in cyprus.branches:
    #             skip_this_leaf = _____ and _____
    #             if not skip_this_leaf:
    #                 plucked_branch_or_error = pluck_one_leaf(b)
    #                 if isinstance(plucked_branch_or_error, str):
    #                     return plucked_branch_or_error
    #                 else:
    #                     _____
    #         return Tree(_____, plucked_branches)
    #     nonlocal pine
    #     if pine.is_leaf():
    #         assert k == pine.label, 'all k must appear in pine'
    #         return 'success!'
    #     _____
    #     if isinstance(pine, str):
    #         return pine
    #     return plucker
    # return plucker

##############################
# NO FURTHER QUESTIONS BELOW #
##############################

class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches


##############
# QUESTION 2 #
##############

"""A: (3 pts) Implement is_power, which takes a positive integer base and a
non-negative integer s. It returns whether s is a power of base, meaning that there
is some non-negative integer n such that pow(base, n) equals s.

IMPORTANT: You may not call pow, use the ** operator, or import any function
(such as math.log). Your solution must be recursive.

Check the doctests with: python3 ok -q a
"""
def is_power(base, s):
    """Return whether s is a power of base.

    >>> is_power(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
    True
    >>> is_power(5, 1)    # pow(5, 0) = 1
    True
    >>> is_power(5, 5)    # pow(5, 1) = 5
    True
    >>> is_power(5, 15)   # 15 is not a power of 5 (it's a multiple)
    False
    >>> is_power(3, 9)
    True
    >>> is_power(3, 8)
    False
    >>> is_power(3, 10)
    False
    >>> is_power(1, 8)
    False
    >>> is_power(2, 0)    # 0 is not a power of any positive base.
    False

    >>> is_power(4, 16)
    True
    >>> is_power(4, 64)
    True
    >>> is_power(4, 63)
    False
    >>> is_power(4, 65)
    False
    >>> is_power(4, 32)
    False
    """
    assert base > 0 and s >= 0
    assert type(base) is int and type(s) is int
    if s==1:
        return True
    elif s<base :
        return False
    else:
        return is_power(base, s//base)

    # ORIGINAL TEMPLATE for your reference (do not edit this part)
    # if _____:
    #     return True
    # elif _____:
    #     return False
    # else:
    #     return _____

curry2 = lambda f: lambda x: lambda y: f(x, y)

"""B: (5 pts) Implement powers, a generator function which takes positive
integers n and k. It yields all integers m that are both powers of k and whose
digits appear in order in n.

Assume that is_power is implemented correctly.

Note: powers may yield its results in any order. The doctests below check what
is yielded, but not the order. The built-in sorted function used in the doctests
takes in an iterable object and returns a list containing the elements of the
iterable in non-decreasing order.

Check the doctests with: python3 ok -q b
"""
def powers(n, k):
    """Yield all powers of k whose digits appear in order in n.

    >>> sorted(powers(12345, 5))
    [1, 5, 25, 125]
    >>> sorted(powers(54321, 5))  # 25 and 125 are not in order
    [1, 5]
    >>> sorted(powers(2493, 3))
    [3, 9, 243]

    >>> sorted(powers(2493, 2))
    [2, 4]
    >>> sorted(powers(164352, 2))
    [1, 2, 4, 16, 32, 64]
    """
    def build(seed):
        """Yield all non-negative integers whose digits appear in order in seed.
        0 is yielded because 0 has no digits, so all its digits are in seed.
        """
        if seed == 0:
            yield 0
        else:
            for x in range():
                _____
                _____
    yield from filter(curry2(_____)(_____), build(n))

    # ORIGINAL TEMPLATE for your reference (do not edit this part)
    #         for x in _____:
    #             _____
    #             _____
    # yield from filter(curry2(_____)(_____), build(n))


##############
# QUESTION 3 #
##############

"""A: (2 pts) Implement sum_link, which takes a Link instance s and a
one-argument function transform that takes an element of s and returns a number.
The sum_link function returns the sum of the results of calling transform on
each element of the linked list s.

Check the doctests with: python3 ok -q a
"""
def sum_link(s, transform):
    """Sum the result of calling transform on each element of Link s.

    >>> s = Link(3, Link(5, Link(7)))
    >>> sum_link(s, lambda x: x)       # 3 + 5 + 7
    15
    >>> double = lambda x: 2 * x
    >>> sum_link(s, double)            # double(3) + double(5) + double(7)
    30
    >>> sum_link(Link.empty, double)
    0

    >>> sum_link(Link(2, Link(6)), lambda x: x * x)
    40
    """
    if _____:
        return 0
    else:
        return _____

    # ORIGINAL TEMPLATE for your reference (do not edit this part)
    # if _____:
    #     return 0
    # else:
    #     return _____


"""B: (3 pts) Implement CreditCard, a class whose methods are described below.

Check the doctests with: python3 ok -q b
"""
class CreditCard:
    """A CreditCard.

    >>> c = CreditCard(50)
    >>> c.purchase(5)      # 45 remaining
    45
    >>> c.purchase(30)     # now only 15 remaining
    15
    >>> c.purchase(30)
    'declined'
    >>> c.pay_bill()       # current balance is 35
    35
    >>> c.purchase(30)     # 20 remaining
    20
    >>> [CreditCard(10), CreditCard(20, 5)]
    [CreditCard(10, 0), CreditCard(20, 5)]

    >>> d = CreditCard(100)
    >>> d.purchase(10)
    90
    >>> d.purchase(60)
    30
    >>> d.purchase(60)
    'declined'
    >>> d.pay_bill()
    70
    >>> d.purchase(60)
    40
    """

    def __init__(self, maximum, balance=0):
        """A CreditCard is constructed from a maximum and an optional balance,
        which defaults to 0. The maximum represents the greatest value that
        balance is allowed to take after a purchase.
        """
        assert balance <= maximum
        self.maximum = maximum
        self.balance = balance

    def purchase(self, price):
        """When the CreditCard is used to make a purchase, the purchase price
        is added to the balance unless the purchase is declined. A purchase is
        declined if the result of adding the price to the current balance would
        exceed the maximum. If the purchase is not declined, return the highest
        price of the next purchase that would not be declined.
        """
        assert price > 0
        if _____:
            return 'declined'
        _____
        return _____

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # if _____:
        #     return 'declined'
        # _____
        # return _____

    def pay_bill(self):
        """Reduce the balance to 0 and return the value of the balance before
        it was reset to 0.
        """
        _____
        _____
        return _____

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # _____
        # _____
        # return _____

    def __repr__(self):
        return 'CreditCard(' + repr(self.maximum) + ', ' + repr(self.balance) + ')'


"""C: (4 pts) Implement Wallet, a class whose methods are described below.

Check the doctests with: python3 ok -q c
"""
class Wallet:
    """A Wallet with a linked list of CreditCards.

    >>> a = Wallet(Link(CreditCard(1000), Link(CreditCard(2000))))
    >>> a.total_available
    3000
    >>> a.procure(10).procure(30).procure(1000).procure(160)
    Wallet(Link(CreditCard(1000, 200), Link(CreditCard(2000, 1000))))
    >>> a.total_available
    1800
    >>> a.procure(1500)
    'No CreditCard can purchase an item of that price.'

    >>> b = Wallet(Link(CreditCard(10), Link(CreditCard(20), Link(CreditCard(30)))))
    >>> b.total_available
    60
    >>> b.procure(20).procure(10).procure(20)
    Wallet(Link(CreditCard(10, 10), Link(CreditCard(20, 20), Link(CreditCard(30, 20)))))
    """
    def __init__(self, s):
        """A Wallet is constructed from a linked list of CreditCard instances s.
        """
        assert s is Link.empty or isinstance(s, Link)
        self.cards = _____

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # self.cards = _____

    @property
    def total_available(self):
        """The sum of the difference between the maximum and balance for all
        CreditCards held by the Wallet.
        """
        return sum_link(_____, _____)

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # return sum_link(_____, _____)

    def procure(self, price):
        """Attempt to purchase at price using each CreditCard in order, continuing
        as long as the purchase is declined. Return the Wallet if procure resulted
        in a successful purchase for one of the CreditCards, or otherwise return
        a string describing that no CreditCard can purchase at that price.

        IMPORTANT: The price cannot be split between multiple CreditCards.
        """
        _____
        while _____:
            if _____ != 'declined':
                _____
            _____
        return 'No CreditCard can purchase an item of that price.'

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # _____
        # while _____:
        #     if _____ != 'declined':
        #         _____
        #     _____
        # return 'No CreditCard can purchase an item of that price.'

    def __repr__(self):
        return 'Wallet(' + repr(self.cards) + ')'

##############################
# NO FURTHER QUESTIONS BELOW #
##############################

class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3 4 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> s.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s.rest)
    <7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1 <2 3> 4>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
