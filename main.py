import random

def start_game():
    x = int(input("Choisissez la borne minimale:"))
    y = int(input("Choisissez la borne maximale:"))

    random_number = random.randint(x, y)
    number_of_guesses = 1
    guess = y+1

    print("\nJ'ai choisi un nombre entre", x," et ", y, ". À vous de le deviner...")

    while guess != random_number:
        guess = int(input("Entrez votre essai:"))

        if guess > random_number:
            print("Mauvais choix, le nombre est plus petit que", guess, "\n")
            number_of_guesses = number_of_guesses + 1

        elif guess < random_number:
            print("Mauvais choix, le nombre est plus grand que", guess, "\n")
            number_of_guesses = number_of_guesses + 1

    print("Bravo! Bonne reponse.")
    print("Vous avez reussi en:", number_of_guesses, "essai(s).")

    answer = str(input("\nVoulez vous jouer une autre partie (o/n)?"))
    if answer == "o":
        start_game()
    elif answer == "n":
        print("Merci et au revoir...")


start_game()