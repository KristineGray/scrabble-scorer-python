# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


OLD_POINT_STRUCTURE = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letter_points = ""

    for char in word:
        for point_value in OLD_POINT_STRUCTURE:
            if char in OLD_POINT_STRUCTURE[point_value]:
                letter_points += f'Points for {char}: {point_value}\n'

    return letter_points

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
    print("Let's play some Scrabble!\n")
    word = input("\nEnter a word to score: ")
    return word

def simple_scorer():
    return 

def vowel_bonus_scorer():
    return 

def scrabble_scorer():
    return

scoring_algorithms = ()

def scorer_prompt():
    return 

def transform():
    return

def run_program():
    word = initial_prompt()
    letter_points = old_scrabble_scorer(word)
    print(letter_points)
