# Hangman in Python

import random

words = ("apple","orange","banana","coconut","pineapple")

# dictionary of key:()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/|  ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o  ",
                  "/|\\",
                  "/   "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}

# for line in hangman_art[6]:
#     print(line)

def display_man(wrong_guesses):
    print("*************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*************")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invald input")
            continue  #to skip the current iteration
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue
        
        guessed_letters.add(guess)
    
        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index]= guess
        else:
            wrong_guesses+=1
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running=False
        elif wrong_guesses >= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running=False


if __name__ == '__main__':
    main()