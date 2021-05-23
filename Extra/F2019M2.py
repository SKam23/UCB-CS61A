def max_tree(t, key):
"""
(6 points) Max Tree   Q3 Fall 2019 M2
(a) (4 pt) Implement max_tree, which takes a Tree instance t and a function key that takes one argument
and returns a number. The max_tree function returns the label n of t for which key(n) is largest. If
there is more than one label for which key returns the same largest value, max_tree can return any of
those labels. The Tree class is defined on the Midterm 2 Study Guide. You may not call min or max.
"""
"""
Return the label n of t for which key(n) returns the largest value.
>>> t = Tree(6, [Tree(3, [Tree(5)]), Tree(2), Tree(4, [Tree(7)])])
>>> max_tree(t, key=lambda x: x)
7
>>> max_tree(t, key=lambda x: -x)
2
>>> max_tree(t, key=lambda x: -abs(x - 4))
4
"""
    if t.is_leaf():
        return ___________________________________________________________________________
    x = __________________________________________________________________________________
    for b in t.branches:
        m = ______________________________________________________________________________
        if _______________________________________________________________________________:
            x = m
    return x


def stable(s, k, n):
"""
(4 points) Seek Once Q4 Fall 2019 M2
Implement stable, which takes a list of numbers s, a positive integer k, and a non-negative number n. It
returns whether all pairs of values in s with indices that differ by at most k have an absolute difference in value
of at most n.
You may not use lambda, if, and, or or in your solution.
Note: The “functions that aggregate iterable arguments” on the Midterm 2 Study Guide have the following
behavior when called on an empty list:
• sum([]) evaluates to 0.
• max([]) causes a ValueError.
• min([]) causes a ValueError.
• all([]) evaluates to True.
• any([]) evaluates to False.

Return whether all pairs of elements of S within distance K differ by at most N.
>>> stable([1, 2, 3, 5, 6], 1, 2) # All adjacent values differ by at most 2.
True
>>> stable([1, 2, 3, 5, 6], 2, 2) # abs(5-2) is a difference of 3.
False
>>> stable([1, 5, 1, 5, 1], 2, 2) # abs(5-1) is a difference of 4.
False
"""
    for i in range(len(s)):
        near = range(_______________________________________________________________, i)
        if ________________([ _____________________________________ > n for j in near]):
            return False
    return True



def partitions(n, m):
"""
(6 pt) Q5 2019 Fall M2
Implement partitions, which is a generator function that takes positive integers n and m. It yields
strings describing all partitions of n using parts up to size m. Each partition is a sum of non-increasing
positive integers less than or equal to m that totals n. The partitions function yields a string for each
partition exactly once.
You may not use lambda, if, and, or, lists, tuples, or dictionaries in your solution (other than what
already appears in the template).
Yield all partitions of N using parts up to size M.
>>> list(partitions(1, 1))
['1']
>>> list(partitions(2, 2))
['2', '1 + 1']
>>> list(partitions(4, 2))
['2 + 2', '2 + 1 + 1', '1 + 1 + 1 + 1']
>>> for p in partitions(6, 4):
... print(p)
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1
"""
    if __________________________________________________________________________:
        yield ___________________________________________________________________
    if n > 0 and m > 0:
        for p in partitions(_________________________, _________________________):
            yield _______________________________________________________________
        yield from partitions(_________________________, ________________________)
