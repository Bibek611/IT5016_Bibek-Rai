import random

def user_number_guess(computer_number):
    prompt="Enter your guess(1-99)"
    num_guesses=0
    number=0
    while number!=computer_number:
        number=int(input(prompt))
        num_guesses+=1
        if number<computer_number:
            print("too low")
        elif number>computer_number:
            print("too high")
        else:
            print(f"Correct ! number of guess: {num_guesses}")



def main():
    user_number_guess(random.randrange(1,100))
main()