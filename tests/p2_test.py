import pytest

from p2 import sum_of_even_fibonacci


def test_0():
    assert sum_of_even_fibonacci(0) == 0


def test_1():
    assert sum_of_even_fibonacci(1) == 0


def test_2():
    assert sum_of_even_fibonacci(2) == 2


def test_90():
    assert sum_of_even_fibonacci(90) == 44
