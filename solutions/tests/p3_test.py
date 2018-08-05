import pytest

from solutions.p3 import largest_prime_factor


def test_1():
    assert largest_prime_factor(2) == 2


def test_2():
    assert largest_prime_factor(25) == 5


def test_4():
    assert largest_prime_factor(7833) == 373


def test_3():
    assert largest_prime_factor(13195) == 29
