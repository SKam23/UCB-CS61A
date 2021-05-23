email = 'skam@berkeley.edu'

"""
Su 15 Final q5

This question is in two parts, implementing the basic Network class, and then
the `degrees` method of the Network class. See the specifications
in each definition for details.
"""
"""
Part (a) (4 pt) The TAs are building a social networking website called CS61A+. The TAs plan to
represent the network in a class called Network that supports the following method:
    - add_friend(user1, user2): adds user1 and user2 to each other’s friends lists. If user1 or
      user2 are not in the Network, add them to the dictionary of friends.
Help the TAs implement these two methods to make their social networking website popular!

Run tests for just this part with
    python3 ok -q a
"""
class Network:
    """
    >>> cs61a_plus = Network()
    >>> cs61a_plus.add_friend('Robert', 'Jeffrey')
    >>> cs61a_plus.friends['Robert']
    ['Jeffrey']
    >>> cs61a_plus.friends['Jeffrey']
    ['Robert']
    >>> cs61a_plus.add_friend('Jessica', 'Robert')
    >>> cs61a_plus.friends['Robert']
    ['Jeffrey', 'Jessica']
    """
    def __init__(self):
        self.friends = {} # Maps users to a list of their friends

    def add_friend(self, user1, user2):
        if user1 not in self.friends:
            self.friends[user1] = []
        if user2 not in self.friends:
            self.friends[user2] = []
        self.friends[user1].append(user2)
        self.friends[user2].append(user1)

    """
    Part (b) (5 pt) CS61A+ turns out to be unpopular. To attract more users, the TAs want to implement a feature
    that checks if two users have at most n degrees of separation. Consider the following CS61A+ Network:
    self.friends = {
        'Robert': ['Jeffrey', 'Jessica'],
        'Jeffrey': ['Robert', 'Jessica', 'Yulin'],
        'Jessica': ['Robert', 'Jeffrey', 'Yulin'],
        'Yulin': ['Jeffrey', 'Jessica'],
        'Albert': []
    }

    - There is 1 degree of separation between Robert and Jeffrey, because they are direct friends.
    - There are 2 degrees of separation between Robert and Yulin (Robert → Jessica → Yulin)
    - The degree of separation between Albert and anyone else is undefined, since Albert has no friends.

    Help the TAs implement the degrees(user1, user2, n) method, which returns True if user1 and user2
    are separated by at most n degrees (fewer degrees is okay). You can assume that user1 and user2 are
    already in the Network.
    """

    def degrees(self, user1, user2, n):
        """
        >>> cs61a_plus = Network()
        >>> cs61a_plus.friends = {'Robert': ['Jeffrey', 'Jessica'], 'Jeffrey': ['Robert', 'Jessica', 'Yulin'], 'Jessica': ['Robert', 'Jeffrey', 'Yulin'], 'Yulin': ['Jeffrey', 'Jessica'], 'Albert': []}
        >>> cs61a_plus.degrees('Robert', 'Yulin', 2) # Exactly 2 degrees
        True
        >>> cs61a_plus.degrees('Robert', 'Jessica', 2) # Less than 2 degrees
        True
        >>> cs61a_plus.degrees('Yulin', 'Robert', 1) # More than 1 degree
        False
        >>> cs61a_plus.degrees('Albert', 'Jessica', 10) # No friends!
        False
        """
        if n==0:
            return False
        elif user1 in self.friends[user2]:
            return True
        for friend in self.friends[user2]:
            if self.degrees(user1 , friend, n-1):
                return True
        return False



# ORIGINAL SKELETON FOLLOWS

# """
# Su 15 Final q5

# This question is in two parts, implementing the basic Network class, and then
# the `degrees` method of the Network class. See the specifications
# in each definition for details.
# """
# """
# Part (a) (4 pt) The TAs are building a social networking website called CS61A+. The TAs plan to
# represent the network in a class called Network that supports the following method:
#     - add_friend(user1, user2): adds user1 and user2 to each other’s friends lists. If user1 or
#       user2 are not in the Network, add them to the dictionary of friends.
# Help the TAs implement these two methods to make their social networking website popular!

# Run tests for just this part with
#     python3 ok -q a
# """
# class Network:
#     """
#     >>> cs61a_plus = Network()
#     >>> cs61a_plus.add_friend('Robert', 'Jeffrey')
#     >>> cs61a_plus.friends['Robert']
#     ['Jeffrey']
#     >>> cs61a_plus.friends['Jeffrey']
#     ['Robert']
#     >>> cs61a_plus.add_friend('Jessica', 'Robert')
#     >>> cs61a_plus.friends['Robert']
#     ['Jeffrey', 'Jessica']
#     """
#     def __init__(self):
#         self.friends = {} # Maps users to a list of their friends

#     def add_friend(self, user1, user2):
#         if ______ in ______:
#             ______
#         if ______ in ______:
#             ______
#         ______
#         ______

#     """
#     Part (b) (5 pt) CS61A+ turns out to be unpopular. To attract more users, the TAs want to implement a feature
#     that checks if two users have at most n degrees of separation. Consider the following CS61A+ Network:
#     self.friends = {
#         'Robert': ['Jeffrey', 'Jessica'],
#         'Jeffrey': ['Robert', 'Jessica', 'Yulin'],
#         'Jessica': ['Robert', 'Jeffrey', 'Yulin'],
#         'Yulin': ['Jeffrey', 'Jessica'],
#         'Albert': []
#     }

#     - There is 1 degree of separation between Robert and Jeffrey, because they are direct friends.
#     - There are 2 degrees of separation between Robert and Yulin (Robert → Jessica → Yulin)
#     - The degree of separation between Albert and anyone else is undefined, since Albert has no friends.

#     Help the TAs implement the degrees(user1, user2, n) method, which returns True if user1 and user2
#     are separated by at most n degrees (fewer degrees is okay). You can assume that user1 and user2 are
#     already in the Network.
#     """

#     def degrees(self, user1, user2, n):
#         """
#         >>> cs61a_plus = Network()
#         >>> cs61a_plus.friends = {'Robert': ['Jeffrey', 'Jessica'], 'Jeffrey': ['Robert', 'Jessica', 'Yulin'], 'Jessica': ['Robert', 'Jeffrey', 'Yulin'], 'Yulin': ['Jeffrey', 'Jessica'], 'Albert': []}
#         >>> cs61a_plus.degrees('Robert', 'Yulin', 2) # Exactly 2 degrees
#         True
#         >>> cs61a_plus.degrees('Robert', 'Jessica', 2) # Less than 2 degrees
#         True
#         >>> cs61a_plus.degrees('Yulin', 'Robert', 1) # More than 1 degree
#         False
#         >>> cs61a_plus.degrees('Albert', 'Jessica', 10) # No friends!
#         False
#         """
#         if ______:
#             return ______
#         elif ______:
#             return ______
#         for friend in ______:
#             if ______:
#                 return True
#         return ______


