import random

number = random.randint(0, 100)


while True:
    try:
        guess = int(input("I thought a number what is it?: "))
    except ValueError:
        print(f"Bad number {guess}!")
    if guess > number:
        print("Too big!")
    elif guess < number:
        print("Too lower!")
    else:
        print("You guessed! Win! Great!")
        break