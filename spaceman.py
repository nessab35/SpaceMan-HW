'''Importing a module with random words'''
import random

def load_word():
    '''
    A function reads a text file of words, randomly selects one to use as secret word from the list.
    '''
    with open('words.txt', 'r', encoding='utf-8') as file:
        words_list = file.readlines()


    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    '''
    # Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letters in secret_word:
        if letters not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word
    and underscores for letters that have not been guessed yet.
    '''
    #Loop through the letters in secret_word, build string, put "_" for missing letter
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_"

    return result



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    '''
    #check if the letter guess is in the secret word
    return guess in secret_word



#def availiable letters
def available_letter(guessed_letters, all_letters):
    '''
    Function to return letter that have yet to be guessed
    '''
    remaining_letters = []
    for letters in all_letters:
        if letters not in guessed_letters:
            remaining_letters.append(letters)
    return remaining_letters




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    '''
    guessed_letters = []
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num_guessleft = 7
    game_running = True

    # show the player information about the game according to the project spec
    print(f'''
        Welcome to Spaceman, 
        The secret word contains: {len(secret_word)} letters
        You will be given 7 chances to guess the letters in the word per round
        GOOD LUCK!
        ''')

    # ask the player to guess one letter per round and check that it is only one letter
    while game_running:
        single_letter = False

        while single_letter is False:
            letter_guessed = input("Enter a letter: ")
            if len(letter_guessed) == 1:
                single_letter = True
                if letter_guessed not in guessed_letters:
                    guessed_letters.append(letter_guessed)

    # Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guessed_letters[-1], secret_word):
            print("This letter is in the secret word")
            print("".join(available_letter(guessed_letters, all_letters)))
        else:
            print("This letter is not in the secret word, try again")
            num_guessleft -= 1
            print(f"Number of guessed left: {num_guessleft}")
            print("".join(available_letter(guessed_letters, all_letters)))

    # Show the guessed word so far
        guessed_word_sofar = get_guessed_word(secret_word, "".join(guessed_letters))
        print(f"Your guessed word so far: {guessed_word_sofar}")

    #check if the game has been won or lost
        if num_guessleft <= 0 and not is_word_guessed(secret_word, "".join(guessed_letters)):
            print("Sorry, you ran out of guesses, You Lose!")
            print(f"The secret word was, {secret_word}")
            game_running = False

        elif num_guessleft > 0 and is_word_guessed(secret_word, "".join(guessed_letters)):
            print("You win!")
            game_running = False

#These function calls that will start the game
word = load_word()
spaceman(word)
 
