email = 'skam@berkeley.edu'

def envelope(password, limit):
    """ Write a higher-order function `envelope` that returns a one-argument
    function `attempt`. Every time `attempt` is called, it checks to see if its argument
    matches the password at the corresponding index.

    If the password entirely matches, return a success string. If more than `limit`
    number of incorrect hacks are attempted, you should return an error string.
    For details, see the doctest.


    Note: to comment out a blank that covers an entire line, just put down 'unnecessary' (with quotes)

    >>> hacker = envelope([1,2], 2)
    >>> hacker(1)
    >>> hacker(2)
    'Access granted!'
    >>> hacker = envelope([1,2], 1)
    >>> hacker(1)
    >>> hacker(3) # used up attempts to gain access
    >>> hacker(2) # correct attempt to gain access, but already locked
    'The safe is now inaccessible!'
    >>> hacker = envelope([1,2], 2)
    >>> hacker(1)
    >>> hacker(3) # 1 attempt left to gain access
    >>> hacker(2) # correct attempt to gain access
    'Access granted!'
    """
    count = 0
    'unnecessary'
    def attempt(digit):
        nonlocal count
        'unnecessary'
        if count>= limit:
            return "The safe is now inaccessible!"
        if digit == password[0]:
            password.remove(digit)
            if len(password)==0:
                return 'Access granted!'
        else:
            count+=1
    return attempt

# ORIGINAL SKELETON FOLLOWS

# def envelope(password, limit):
#     """ Write a higher-order function `envelope` that returns a one-argument
#     function `attempt`. Every time `attempt` is called, it checks to see if its argument
#     matches the password at the corresponding index.

#     If the password entirely matches, return a success string. If more than `limit`
#     number of incorrect hacks are attempted, you should return an error string.
#     For details, see the doctest.


#     Note: to comment out a blank that covers an entire line, just put down 'unnecessary' (with quotes)

#     >>> hacker = envelope([1,2], 2)
#     >>> hacker(1)
#     >>> hacker(2)
#     'Access granted!'
#     >>> hacker = envelope([1,2], 1)
#     >>> hacker(1)
#     >>> hacker(3) # used up attempts to gain access
#     >>> hacker(2) # correct attempt to gain access, but already locked
#     'The safe is now inaccessible!'
#     >>> hacker = envelope([1,2], 2)
#     >>> hacker(1)
#     >>> hacker(3) # 1 attempt left to gain access
#     >>> hacker(2) # correct attempt to gain access
#     'Access granted!'
#     """
#     ______
#     ______
#     def attempt(digit):
#         ______
#         ______
#         if ______:
#             return ______
#         if ______:
#             ______
#             if ______:
#                 return ______
#         else:
#             ______
#     return ______
