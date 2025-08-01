import random

random_number = random.randint(1,50)
user_guesses = 10
is_winner = False

while user_guesses > 0:
    user_guess = int(input("Enter Your Guess: "))

    if user_guess == random_number:
        is_winner = True
        break

    elif user_guess > random_number:
        print("Hint: You Choose Too High!")
        user_guesses -= 1
        
    else:
        print("Hint: You Choose Too Low!")
        user_guesses -= 1


if is_winner:
    print(f"Your Guess is right, You guess Secret Number {random_number} with the {user_guesses} attempts still remaining.")


else:
    print(f"Sorry 😢, You could not guess the right number, The Secret Number was: {random_number}")