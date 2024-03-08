import pytest
from exo3 import addition

def test_addition():
    
    num1 = 5
    num2 = 10
    
    
    result = addition(num1, num2)
    
    assert result == 15, "La somme de 5 et 10 devrait être égale à 15"
