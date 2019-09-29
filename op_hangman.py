# Hangman game 
import random
import resources

#wordlist = "monkey banana castle king princess".upper().split()

random.shuffle(resources.items)

#print(hangman_board)
secret_word = resources.items.pop()
correct = []
incorrect = []

#print("DEBUG: %s" % secret_word)

def draw_board():
    # board setup
    print(resources.hangman_board[len(incorrect)])
    print("\n")
    for i in secret_word:
        if i == " ":
            print(" ", end="  ")
        elif i in correct:
            print(i, end="  ")
        else:
            print("__", end="  ")
    print("\n")
    print("******MISSED LETTERS*******")
    for i in incorrect:
        print(i, end="  ")
    print("\n***************************")

def user_guess():
    # letters guess by user
    while True:
        guess = input("Enter a letter: ").upper()
        print("\n")
        if guess in correct or guess in incorrect:
            print("SAME LETTER AGAIN.")
        elif guess.isnumeric():
            print("NOT NUMBER, LETTER. L.E.T.T.E.R, LETTER.")
        elif len(guess) > 1:
            print("ONE LETTER.")
        elif len(guess) == 0:
            print("A LETTER.")
        else:
            break
    if guess in secret_word:
        correct.append(guess)
    else:
        incorrect.append(guess)

def check_win():
    # check number of turns
    turns = 5
    # for peeps with SPACE in name(BUG -->SOLVED)
    if ' ' in secret_word:
        correct.append(' ')

    if len(incorrect) >= turns:
        return "LOSER"
    for i in secret_word:
        if i not in correct:
            return "Keep going."
    draw_board()
    return "WINNER WINNER CHICKEN DINNER"

while True:
    print("\n")
    print("*******************************************************************")
    print("**************         H__A__N__G__M__A__N         ****************")
    print("*******************************************************************\n")
    draw_board()
    user_guess()
    win_condition = check_win()
    print(win_condition)
    if win_condition == "LOSER":
        print(resources.hangman_board[-1])
        print("GAME OVER! THE WORD WAS *****%s*****" % secret_word)
        break
    elif win_condition == "WINNER WINNER CHICKEN DINNER":
        print("YOU WIN! THE WORD WAS *****%s*****" % secret_word)
        break
