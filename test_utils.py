import pytest
import utils

@pytest.mark.parametrize("a, b, expected", [(0, 0, 0), (1, 1, 2), (3, 3, 6), (4, 5, 9)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(0, 0, 0), (1, 1, 0), (3, 1, 2), (2, 3, -1)])
def test_substract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(0, 0, 0), (1, 1, 1), (3, 1, 3), (3, 3, 9)])
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(1, 1, 1), (4, 2, 2), (5, 5, 1), (9, 3, 3)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(1, 1, 1), (2, 2, 4), (5, 0, 1), (3, 3, 27)])
def test_power(a, b, expected):
    result = utils.power(a, b)
    assert result == expected