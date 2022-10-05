"""
Programme fait par Jacques-Conrad Calagui-Painchaud
Groupe: 405
Description: L'ordinateur choisira un nombre aléatoire entre des bornes définis par l'usager.
L'usager essayera ensuite de deviner cette nombre.
"""

import random


def choose_limits():
    """
    L'usager choisi les bornes maximales et minimales pour le nombre aléatoire choisi par l'ordinateur.
    :return: None
    """
    global lower_limit, upper_limit
    lower_limit = int(input("Choisissez la borne minimale:"))
    upper_limit = int(input("Choisissez la borne maximale:"))


while True:
    choose_limits()
    random_number = random.randint(lower_limit, upper_limit)
    print(f"\nJ'ai choisi un nombre entre {lower_limit} et {upper_limit}. À vous de le deviner...")

    guess = None
    number_of_guesses = 0

    while guess != random_number:
        guess = int(input("Entrez votre essai:"))
        number_of_guesses += 1

        if guess > random_number:
            print(f"Mauvais choix, le nombre est plus petit que {guess}.")
        elif guess < random_number:
            print(f"Mauvais choix, le nombre est plus grand que {guess}.")

    print("\nBravo! Bonne réponse.")
    print(f"Vous avez reussi en {number_of_guesses} essai(s).")

    play_again = str(input("Voulez vous jouer une autre partie? (o/n)"))
    if play_again == "o":
        continue
    elif play_again == "n":
        print("Merci et au revoir...")
        break

