import doctest
import sys
from sys import argv
### Discussion 04 ###

#########
# Recursion
#########

# Q1.1
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n ==  0:
        return 0
    else:
        return multiply(m,n-1) +m

# Q1.2
def is_prime(n):
    """Iterative solution to is_prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def is_prime(n):
    """Recursive.
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(number, count ):
        if number == count:
            return True
        elif number%count ==0 or number == 1:
            return False
        else:
            return True and prime_helper(number, count+1)
    return prime_helper(n, 2)


#########
# Tree Recursion
#########

# Example: Fibonacci sequence
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Q2.1
def count_stair_ways(n):
    if n == 0:
        return 1
    elif n< 0:
        return 0
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

# Q2.2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n< 0:
        return 0
    else:
        total = 0
        i=1
        while i<=k:
            total += count_k(n-i,k)
            i += 1
        return total

#########
# Lists
#########

"""
>>> fantasy_team = ['aaron rodgers', 'desean jackson']
>>> print(fantasy_team)
['aaron rodgers', 'desean jackson']
>>> fantasy_team[0]
'aaron rodgers'
>>> fantasy_team[len(fantasy_team) - 1]
'desean jackson'
>>> fantasy_team[-1]
'desean jackson'
"""

"""
>>> directors = ['jenkins', 'spielberg', 'bigelow', 'kubrick']
>>> directors[:2]
['jenkins', 'spielberg']
>>> directors[1:3]
['spielberg', 'bigelow']
>>> directors[1:]
['spielberg', 'bigelow', 'kubrick']
>>> directors[0:4:2]
['jenkins', 'bigelow']
>>> directors[::-1]
['kubrick', 'bigelow', 'spielberg', 'jenkins']
"""

# Q3.1
def wwpd():
    """
    >>> a = [1, 5, 4, [2, 3], 3]
    >>> print(a[0], a[-1])
    ____________________
    >>> len(a)
    ____________________
    >>> 2 in a
    ____________________
    >>> 4 in a
    ____________________
    >>> a[3][0]
    ____________________
    """
    pass

# Q3.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """

    return [i *s[i] for i in range(len(s)) if i%2==0]

# Q3.3
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    "*** YOUR CODE HERE ***"

# Quiz
def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """

    if _________________________________________________________:
        return _________________________________________________________
    return ______________________________________________________________

def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """

    def helper(_________________________________________________________):

        if _________________________________________________________:

            return _________________________________________________________

        if _________________________________________________________:

            return _________________________________________________________

        return _________________________________________________________

    return helper(_________________________________________________________)

try:
    doctest.run_docstring_examples(globals()[argv[1]], globals(), name=argv[1])
except:
    sys.exit("Invalid Arguments")
