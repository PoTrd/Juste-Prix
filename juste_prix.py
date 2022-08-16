import random

n = random.randint(1, 10)
user_number = 0
tentatives = 0

while user_number != n:

    user_number = int(input("Choisis un nombre entre 1 et 10 : "))
    tentatives += 1

    if user_number == n:
        print(
            "Bravo, tu as gagnés le Juste Prix avec {0} tentatives !" .format(tentatives))
    elif user_number < n and user_number >= 1:
        print("C'est plus !")
    elif user_number > n and user_number <= 10:
        print("C'est moins !")
    elif user_number > 10 or user_number < 1:
        print("Attention,le nombre n'est pas dans l'encadrement, choisis en un autre.")
    else:
        print(">>ERROR")
