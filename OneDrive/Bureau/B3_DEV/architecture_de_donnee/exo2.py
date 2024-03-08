def count_upper_lower(sentence):
    Maj = 0
    Min = 0

    for B in sentence:
        if B.isupper():
            Maj += 1
        elif B.islower():
            Min += 1

    return Min, Maj

A = "Je suis sami Je Passe au Tableau"
minuscules, majuscules = count_upper_lower(A)
print(minuscules, majuscules)