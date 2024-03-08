import pytest
from exo4 import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates("aabbcc") == ["a", "b", "c"]
    assert remove_duplicates("abc") == ["a", "b", "c"]
    assert remove_duplicates("") == []
    assert remove_duplicates("aa") == ["a"]
    