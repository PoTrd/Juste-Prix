import random

n = random.randint(1, 10)


def play():
    user_number = int(input("Choisis un nombre entre 1 et 10 : "))
    if user_number == n:
        print("Bravo, tu as gagnés le Juste Prix !")
    elif user_number != n and user_number < 10 and user_number > 1:
        print("Mince, tu dois retenter ta chance si tu veux gagner.")
        play()
    else:
        print(">>ERROR")
        play()


play()
