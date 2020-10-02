"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

import itertools
import random

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


def create_perms(list1):

    perms = list(itertools.product(list1, repeat=4))

    return perms


def sum_diff(perms):

    success = []

    for perm in perms:
        print(perm[0])
        if (f(perm[0]) + f(perm[1])) == (f(perm[2]) - f(perm[3])):
            success.append(perm)

    return success


print(create_perms(q))
print(sum_diff(create_perms(q)))
