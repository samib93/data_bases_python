import pytest
from exo2 import count_upper_lower

def test_count_upper_lower():

    sentence = "Je suis sami Je Passe au Tableau"
    
    
    minuscules, majuscules = count_upper_lower(sentence)
    
   
    assert minuscules == 17, "Le nombre de lettres minuscules n'est pas correct"
    

    assert majuscules == 9, "Le nombre de lettres majuscules n'est pas correct"




