from functools import reduce
from operator import mul


def product(numbers):
    return reduce(mul, numbers)


def factorial(n):
    return product(range(2, n)) if n > 1 else 1


def permutations(n, k):
    return factorial(n) // factorial(n - k)


def combinations(n, k):
    return permutations(n, k) // factorial(k)


def floor_root(n):
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        square = mid**2
        if square == n:
            return mid
        if square > n:
            high = mid - 1
            continue
        if square < n:
            low = mid + 1
            continue
    return mid if high * high > n else high


def is_prime(n):
    return sum(i for i in range(3, floor_root(n), 2) if not n % i) == 0 and n % 2 if n > 2 else n == 2
