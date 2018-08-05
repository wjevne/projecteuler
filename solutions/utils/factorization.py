from functools import reduce
from operator import mul


def wheel(primes, start=2, end=None):
    mod = reduce(mul, primes, 1)
    spokes = set()

    # Find the spokes (relatively prime positive integers)less than the
    # primorial (first turn)
    for i in range(1, mod):
        for p in primes:
            if i % p == 0:
                break
        else:
            spokes.add(i)

    # Find spokes in subsequent turns (skip evens aside from 2)
    i = start if start % 2 == 1 else start + 1

    if primes and start <= 2:
        yield 2
    while end is None or i < end:
        if i in primes or i % mod in spokes:
            yield i
        i += 2


def factor(n):
    factors = []
    whl = wheel([2, 3, 5, 7])
    i = next(whl)

    while i**2 <= n:
        while n % i == 0:
            n /= i
            factors.append(i)
        i = next(whl)

    if n != 1:
        factors.append(int(n))

    return factors
