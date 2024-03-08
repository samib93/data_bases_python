import pytest
from exo6 import tuple_list

def test_tuple_list():
    assert tuple_list([(1, 2, 3)]) == (1, 2, 3)
    assert tuple_list([(1, 2), (1, 2, 3), (1, 2, 3, 4)]) == (1, 2, 3, 4)
    assert tuple_list([]) == None
    assert tuple_list([(1, 2), (3, 4), (5, 6)]) == (1, 2)