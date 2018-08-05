import pytest

from utils.fibonacci import fibonacci


def test_1():
    assert list(fibonacci(0)) == [0]


def test_2():
    assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8]
