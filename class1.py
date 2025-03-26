import random

print("Welcome to the number guessing game! , \n you will get 5 attempts to win the game \n  Let's start the game")

number_to_guess = random.randrange(50 , 100)
chances = 5
guess_counter = 0
while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please enter your guess: "))

    if my_guess == number_to_guess: 
        print(f"The number is {number_to_guess} and you guessed it right in {guess_counter} attempts")
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops sorry, the number is{ number_to_guess} better luck next time!")
        break
    elif my_guess < number_to_guess:
        print("Too low, try again!")

    elif my_guess > number_to_guess:
        print("Too high, try again!")