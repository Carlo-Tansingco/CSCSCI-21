# Carlo Josemaria C. Tansingco, 226232
# March 18, 2024

# I/we certify that this submission complies with the DISCS Academic Integrity
# Policy.

# If I/we have discussed my/our Python language code with anyone other than
# my/our instructor(s), my/our groupmate(s), the teaching assistant(s),
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my/our program.

# If any Python language code or documentation used in my/our program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website, or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

import random 

def print_hangman(num_guesses):
    stages_1 = [

"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  | | 
|  | | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| |   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  ---
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   
|
|
|
|
|
|
|
--------
""",
"""

|   
|
|
|
|
|
|
|
--------
""",
"""

   







--------
"""
"""

   








"""
 #17
]

    stages_2 = [
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  | | 
|  | | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| |   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  ---
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   
|
|
|
|
|
|
|
--------
""", #14
]

    stages_3 = [

"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  | | 
|  | | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| | | |
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
| |   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  ---
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
 #7
]

    if maxguesses <= 7:
        print (stages_3[num_guesses], "\n")
    
    if maxguesses >= 8 and maxguesses <= 14:
        print(stages_2[num_guesses], "\n")

    if maxguesses >= 15:
        if num_guesses >= 17:
            num_guesses = 16
        print(stages_1[num_guesses], "\n")


def wordfinding(guessedletter, guesses):
    letter_found = False  
    for x in range(len(hangman_word)):
        if guessedletter.upper() == hangman_word[x].upper(): 
            correct_guesses[x] = guessedletter.upper()
            letter_found = True  
    if not letter_found:
        guesses -= 1   
    return guesses

def invalid_input(guessedletter):
    invalid_letter = False
    for x in range(len(hangman_word)):
        if guessedletter.upper() == correct_guesses[x].upper():
            print("You have already used that letter. Please choose another valid letter.")
            invalid_letter = True
    
    for x in range(len(unused_letters)):
        if guessedletter.upper() != unused_letters[x].upper() and len(guessedletter) > 1:
            print("Your inputted letter is invalid. Please choose a valid letter.")
            invalid_letter = True

    if invalid_letter:
        return 

word_list_easy = ["CAT", "AXE", "DOG", "BALL", "BOOK", "SUN", "MOON", "CUP", "HAT", "TREE", "WATER", "CUP"]

word_list_medium = ["GUITAR", "PENCIL", "GLASSES", "DRAGON", "PAPER", "PICTURE", "SOLDIER", "STATUE", "MOUSE", "WINDOW", "DARWIN"]

word_list_hard = ["RESONANCE", "COMPUTER", "EUPHORIA", "SYMPHONY", "HYPOTHESIS", "HELLDIVER", "DEMOCRACY", 
                  "RENAISSANCE", "KALEIDOSCOPE", "EQUILIBRIUM", "SERENDIPITY", "TRAITOR"]

word_list_brutal = ["SUPERCALIFRAGILISTICEXPIALIDOCIOUS", "EXACERBATE", "INSURMOUNTABLE", "PHENOMENOLOGY", "ECCENTRICITY", "MAGNANIMOUS", 
                    "CRYPTOCURRENCY", "JUXTAPOSITION", "QUIZZICAL", "RAMBUNCTIOUS", "PSEUDONYM", "PERSPIRATION"]

play_again = True

while play_again:
    randomword = str(input("Would you like the program to choose a random word? (Yes/No)")).upper()
    
    if randomword == "YES":
        difficulty = str(input("What level of difficulty do you want the word to be (Easy, Medium, Hard, Brutal): ")).upper()
        if difficulty == "EASY":
            random_index = int(random.random() * len(word_list_easy))
            word = word_list_easy[random_index]
        if difficulty == "MEDIUM":
            random_index = int(random.random() * len(word_list_medium))
            word = word_list_medium[random_index]
        if difficulty == "HARD":
            random_index = int(random.random() * len(word_list_hard))
            word = word_list_hard[random_index]
        if difficulty == "BRUTAL":
            random_index = int(random.random() * len(word_list_brutal))
            word = word_list_brutal[random_index]
    else:
        word = str(input("Please enter a word for the other player to guess: ")).upper()

    hangman_word = list(word)

    hangman_length = len(hangman_word)

    correct_guesses = ["-" for _ in range(hangman_length)]

    guesses = int(input("Please enter the number of guesses allowed:"))
    maxguesses = guesses

    unused_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    

    while guesses != 0 and hangman_word != correct_guesses:
        
        print("Guess the word, " + str(guesses) + " guess(es) left:" , end="")
        for i in correct_guesses:
            print(i, end="") 
        print("\nUnused letters: ", end="")
        for i in unused_letters:
            print(i, end=" ") 
        
        player_guess = str(input("\n\nPlease select a letter between A-Z: ")).upper()
            
        invalid_input(player_guess)
        guesses = wordfinding(player_guess, guesses)
        unused_letters = [letter for letter in unused_letters if letter != player_guess]  
        print_hangman(guesses-1)
    
    if hangman_word == correct_guesses:
        print ("CONGRATULATIONS! YOU WIN!")

    else:
        print ("SORRY, YOU ARE HANGED!")

    print("\nThe correct word was ", end="")
    for i in hangman_word:
        print(i, end="")
    
    play_again = input("\n\nDo you want to play again? (yes/no): ").upper()
    if play_again == "YES":
        play_again = True
    if play_again == "NO":
        play_again = False
