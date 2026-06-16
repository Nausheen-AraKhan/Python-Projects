import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
guess_num=random.randint(0,100)
def guess_no():
    global guess_num
    level=input("Choose level: 'easy' or 'hard': ")
    if level == "easy":
        i=10
        while i>0:
            print(f"You have {i} guesses left!")
            you_guess=int(input("Guess the number: "))
            if you_guess==guess_num:
                print(f"Congratulations! You guessed the number {guess_num}!")
                break
            elif you_guess>guess_num:
                print("Oops! Too high!\n")
                i-=1
            else:
                print("Oops! Too low!\n")
                i-=1
    elif level == "hard":
        i=5
        while i>0:
            print(f"You have {i} guesses left!")
            you_guess=int(input("Guess the number: "))
            if you_guess==guess_num:
                print(f"Congratulations! You guessed the number {guess_num}!")
                break
            elif you_guess>guess_num:
                print("Oops! Too high!\n")
                i-=1
            else:
                print("Oops! Too low!\n")
                i-=1
    else:
        print("Please enter either 'easy' or 'hard'!")
    print("Refresh The page to play again!")

guess_no()
