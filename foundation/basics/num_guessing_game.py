import random


def guess_game():
    num = random.randint(1, 100)

    while True:
        guess = int(input("Guess (1-100): "))
        if guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
        else:
            print("Correct!")
            break


guess_game()
