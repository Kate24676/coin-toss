import random

def toss_coin():
    coin_toss = random.randit(0, 2)

    if coin_toss == 0:
    return "heads"

    else:
    return "tails"

def prompt():
    user_guess = ""

    while True:
        user_guess = input("Please enter 'heads' or 'tails'(withot quotes): ").lower()
        if user_guess ="heads" pr user_guess = "tails"
        break

    return user_guess

    print(promt())
