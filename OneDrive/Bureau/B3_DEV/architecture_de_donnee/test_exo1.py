import pytest
from exo1 import find_word

def test_find_word():
   
    assert find_word("python est un langage de programmation puissant et facile a apprendre") == True

    assert find_word("Python est un langage de programmation puissant et facile a apprendre") == True
    
    assert find_word("Le langage de programmation préféré de nombreux développeurs est JavaScript") == False
