import doctest
import sys
import argparse

"""
---USAGE---

python3 disc08.py <name_of_function>

e.g. python3 disc08.py iter_wwpd

---NOTES---

- if you pass all the doctests, you will get no terminal output
    - if you want to see the verbose output (all output shown even if the function is correct), run this:

    python3 disc08.py <name_of_function> -v

- if you want to test all of your functions, run this:

    python3 disc08.py all

"""

### Discussion 08 ###

#####################
###   Iterators   ###
#####################

# Q1.1
# Don't test this function until you've tried filling out the blanks,
# since the output will show you the correct answers.
def iter_wwpd():
    """
    >>> lst = [6, 1, "a"]
    >>> next(lst)
    _______
    >>> lst_iter = iter(lst)
    >>> next(lst_iter)
    _______
    >>> next(lst_iter)
    _______
    >>> next(iter(lst))
    _______
    >>> [x for x in lst_iter]
    _______
    """
    pass

######################
###   Generators   ###
######################

# Q2.1
def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ...     print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    subsets = ______
    n = 1
    while ______:
        ______
        ______
        n += 1

# Q2.2
def sum_paths_gen(t):
    """
    >>> t1 = tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    "*** UNCOMMENT SKELETON ***"
    if is_leaf(t):
        yield label(t)
    for b in branches(t):
        for s in sum_path_gen(b):
            yield label(t)+s

#######################################
###   Object-Oriented Programming   ###
#######################################

class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

# Q3.1
def class_wwpd():
    """
    >>> snape = Professor("Snape")
    >>> harry = Student("Harry", snape)
    _______
    >>> harry.visit_office_hours(snape)
    _______
    >>> harry.visit_office_hours(Professor("Hagrid"))
    _______
    >>> harry.understanding
    _______
    >>> [name for name in snape.students]
    _______
    >>> x = Student("Hermione", Professor("McGonagall")).name
    _______
    >>> x
    _______
    >>> [name for name in snape.students]
    _______
    """
    pass

# Q3.2
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_mame = sender_mame
        self.recipient = recipient_name
class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        "*** YOUR CODE HERE ***"
        name = email.recipient_name
        self.clients[name].receive(email)


    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        "*** YOUR CODE HERE ***"
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        "*** YOUR CODE HERE ***"
        self.name = name
        self.server = server
    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        "*** YOUR CODE HERE ***"
        email = Email(mse,self.name,recipient_name)
        self.server.send(email)
    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        "*** YOUR CODE HERE ***"
        self.inbox.append(email)

#######################
###   Inheritance   ###
#######################

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')

# Q4.1
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self,name,owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(self.name + 'says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        "*** YOUR CODE HERE ***"
        if not self.is_alive:
            print("THis cat is dead.")
        elif self.lives>0:
            self.lives -= 1
        elif self.lives ==0:
            self.is_alive = False

# Q4.2
class _____________________: # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        "*** YOUR CODE HERE ***"

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"

# Q4.3
class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

def inher_wwpd():
    """
    >>> x, y = A(), B()
    >>> x.f()
    _______
    >>> B.f()
    _______
    >>> x.g(x, 1)
    _______
    >>> y.g(x, 2)
    _______
    """
    pass

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
