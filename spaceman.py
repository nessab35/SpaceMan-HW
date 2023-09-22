import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

    # Length of Word
stored_secret_word = load_word()
secret_word_length = len(stored_secret_word)
print(f"The secret word contains {secret_word_length} letters", stored_secret_word)

def is_word_guessed(secret_word, letters_guessed):
    for letters in secret_word:
        if letters not in letters_guessed:
            return False
    return True
    '''
    A function that checks if all the letters of the secret word have been guessed.
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_"
    return result 
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    
    pass


def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False
    '''
    A function to check if the guessed letter is in the secret word
    '''
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    '''
secret_word = load_word()
spaceman(secret_word)
guessed_letters = []
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h,', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_guessleft = 7
game_running = True 


    #TODO: show the player information about the game according to the project spec
print(f'''
        Welcome to Spaceman, 
        The secret word is chosen from: {len(secret_word)} 
        You will be given 7 chances to guess the letters in the word per round
        GOOD LUCK!
        ''')

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
while (game_running):
    letter = input("Enter in a letter:")
    if len(letter) == 1 and all_letters:
        break
    else:
        print("That's not a single letter, try again!")
print(f"You entered:{letter}")
        
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
def player_feedback(guessed_letters, secret_word):
    if guessed_letters in secret_word:
        return True 
    else:
        print("This letter is not in the secret word, try again")
        return False

    #TODO: show the guessed word so far
def guessed_word():#need to add into parameters
    
    #TODO: check if the game has been won or lost






#These function calls that will start the game
    secret_word = load_word()
    spaceman(secret_word)
