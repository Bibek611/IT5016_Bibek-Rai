import random
def user_number_guess(computer_num):
    prompt="Enter your guess (1-99):"
    count=0

    while True:
        user_guess=int(input("prompt"))
        count+=1

        if user_guess>computer_num:
            print("Too high")

        elif user_guess<computer_num:
            print("Too low")
        else:
            print(f"Correct! Number of guess:{count}")
            break

def main():
    computer_num=(random.randrange(1,100))
    user_number_guess(computer_num)
main()