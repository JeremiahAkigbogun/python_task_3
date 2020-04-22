
# INTRODUCTION
print('Hello! What is your name? ')
user_name = input()
print("Hi " + str(user_name) + "!" + " Welcome to the number guessing game.")


def guessing_game():

    play = True
    while play:

        easy = 7
        medium = 12
        hard = 21

        print("Would you like to play easy, medium, or hard level?"
              "\nType 'e' for easy, 'm' for medium, or 'h' for hard!")

    # LEVEL SELECTION
        level_selection = True
        while level_selection:
            level = input()
            if level == "e":
                print("\nEasy level selected!")
                level_selection = False
                break
            if level == "m":
                print("\nMedium level selected!")
                level_selection = False
                break
            if level == "h":
                print("\nHard level selected!")
                level_selection = False
                break
            else:
                print("Invalid input!\nPlease enter either 'e', 'm', or 'h'. ")

    # EASY LEVEL
        if level == 'e':
            print("You have 6 tries to guess a number between 1-10.")
            guesses_left = 6
            while guesses_left != 0:
                try1 = input("What's your guess? \n")
                if try1.isnumeric():
                    try1 = int(try1)
                else:
                    print("Invalid input! Please enter an integer")
                if try1 == easy:
                    print("You got it right! ")
                    print("Congratulations " + str(user_name) + "!")
                    play = False
                    break
                guesses_left -= 1
                print('That was wrong!\nYou now have ' + str(guesses_left) + ' guesses left!')
                play = False

                # If the user runs out of guesses
                if guesses_left == 0:
                    print("Game Over!")

    # MEDIUM LEVEL
        if level == 'm':
            print("You have 4 tries to guess a number between 1-20.")
            guesses_left = 4
            while guesses_left != 0:
                try1 = input("What's your guess? \n")
                if try1.isnumeric():
                    try1 = int(try1)
                else:
                    print("Invalid input! Please enter an integer")
                if try1 == medium:
                    print("You got it right! ")
                    print("Congratulations " + str(user_name) + "!")
                    play = False
                    break
                guesses_left -= 1
                print('That was wrong!\nYou now have ' + str(guesses_left) + ' guesses left!')
                play = False

                # If the user runs out of guesses
                if guesses_left == 0:
                    print("Game Over!")

    # HARD LEVEL
        if level == 'h':
            print("You have 3 tries to guess a number between 1-50.")
            guesses_left = 3
            while guesses_left != 0:
                try1 = input("What's your guess? \n")
                if try1.isnumeric():
                    try1 = int(try1)
                else:
                    print("Invalid input! Please enter an integer")
                if try1 == hard:
                    print("You got it right! ")
                    print("Congratulations " + str(user_name) + "!")
                    play = False
                    break
                guesses_left -= 1
                print("That was wrong\nYou now have " + str(guesses_left) + " guesses left!")
                play = False

                # If the user runs out of guesses
                if guesses_left == 0:
                    print("Game Over!")
                    play = False


guessing_game()