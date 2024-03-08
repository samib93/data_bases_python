import pytest
from exo7 import inverse

def test_inverse():
    assert inverse([(1, 2, 3)]) == [(3, 2, 1)]
    assert inverse([(1, 2), (1, 2, 3), (1, 2, 3, 4)]) == [(2, 1), (3, 2, 1), (4, 3, 2, 1)]
    assert inverse([]) == []
    assert inverse([(1, 2), (3, 4), (5, 6)]) == [(2, 1), (4, 3), (6, 5)]
