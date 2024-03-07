def find_word(sentence):
    words = sentence.split()
    for word in words:
        if word == "python":
            return True
    return False

if __name__ == "__main__":
    A = "python est un langage de programmation puissant et facile a apprendre"
    if find_word(A):
        print("Mot trouvé : Python")
    else:
        print("Mot 'Python' non trouvé dans la chaîne de caractères.")

