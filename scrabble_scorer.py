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

def simple_scorer(word):
    return len(word)

def vowel_bonus_scorer(word):
    VOWELS = 'AEIOU'
    score = 0
    for char in word.upper():
        if char in VOWELS:
            score += 3
        else:
            score += 1
    return score

def scrabble_scorer():
    return

scoring_algorithms = (
    {
        "name" : "Simple Score",
        "description" : "Each letter is worth 1 point.",
        "scoring_function" : "A function with a parameter for user input that returns a score."
    },
    {
        "name" : "Bonus Vowels",
        "description" : "Vowels are 3 pts, consonants are 1 pt.",
        "scoring_function" : "A function that returns a score based on the number of vowels and consonants."
    },
    {
        "name" : "Scrabble",
        "description" : "The traditional scoring algorithm.",
        "scoring_function" : "Uses the old_scrabble_scorer() function to determine the score for a given word."
    }
    )

def scorer_prompt():
    return 

def transform():
    return

def run_program():
    word = initial_prompt()
    letter_points = old_scrabble_scorer(word)
    print(letter_points)
