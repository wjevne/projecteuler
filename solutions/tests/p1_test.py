import pytest

from solutions.p1 import sum_of_multiples_of_3_and_5


def test_1():
    assert sum_of_multiples_of_3_and_5(0) == 0


def test_2():
    assert sum_of_multiples_of_3_and_5(4) == 3


def test_3():
    assert sum_of_multiples_of_3_and_5(6) == 8


def test_4():
    assert sum_of_multiples_of_3_and_5(10) == 23
