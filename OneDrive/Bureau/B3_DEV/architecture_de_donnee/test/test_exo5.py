import pytest
from exo5 import rotation_d

def test_rotation_d():
    assert rotation_d([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotation_d([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]
    assert rotation_d([], 2) == []
    assert rotation_d([1], 2) == [1]
    assert rotation_d([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]
    assert rotation_d([1, 2, 3, 4, 5], -7) == [3, 4, 5, 1, 2] 