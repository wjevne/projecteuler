import pytest

from utils.factorization import wheel, factor


def test_1():
    assert list(wheel([], end=10)) == []


def test_2():
    assert list(wheel([2], end=10)) == [2, 3, 5, 7, 9]


def test_3():
    assert list(wheel([2, 3], 10, 30)) == [11, 13, 17, 19, 23, 25, 29]


def test_4():
    assert factor(23) == [23]


def test_5():
    assert factor(25) == [5, 5]


def test_6():
    assert factor(3331) == [3331]


def test_7():
    assert factor(7833) == [3, 7, 373]
