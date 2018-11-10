from random import shuffle
from math import log, e
from mathematics import product, factorial, permutations, combinations, is_prime


def shuffled(arr):
    cp = arr[:]
    shuffle(cp)
    return cp


functions = {
    'log': log,
    'e': e,
    'F': factorial,
    'P': permutations,
    'C': combinations,
    'product': product,
    'is_prime': is_prime,
    'shuffled': shuffled
}


def evaluate(expression):
    return eval(expression, functions)
