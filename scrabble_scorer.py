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

def is_valid_entry(entry_type, user_input):
    if entry_type == "word":
        if len(user_input) == 0:
            return False
        elif len(user_input) > 0:
            for char in user_input:
                if char.isalpha() != True:
                    return False
        else:
            return True
    elif entry_type == "number":
        if user_input not in ["0", "1", "2"]:
            return False
        else:
            return True

def initial_prompt():
    print("Let's play some Scrabble!\n")
    word = input("\nEnter a word to score: ")
    is_valid_word = is_valid_entry("word", word)
    while is_valid_word == False:
        word = input("\nEnter a word to score: ")
        is_valid_word = is_valid_entry("word", word)
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

def scrabble_scorer(word):
    score = 0
    for letter in word.lower():
        score += new_point_structure[letter]
    return score

scoring_algorithms = (
    {
        "name" : "Simple Score",
        "description" : "Each letter is worth 1 point.",
        "scoring_function" : "simple_scorer"
    },
    {
        "name" : "Bonus Vowels",
        "description" : "Vowels are 3 pts, consonants are 1 pt.",
        "scoring_function" : "vowel_bonus_scorer"
    },
    {
        "name" : "Scrabble",
        "description" : "The traditional scoring algorithm.",
        "scoring_function" : "scrabble_scorer"
    }
    )

def scorer_prompt():
    print('Which scoring algorithm would you like to use? ')
    for index in range(len(scoring_algorithms)):
        print(f'{index} - {scoring_algorithms[index]["name"]}: {scoring_algorithms[index]["description"]}')
    
    scorer_choice_str = input('Enter 0, 1, or 2: ')
    is_valid_num = is_valid_entry("number", scorer_choice_str)
    while is_valid_num == False:
        scorer_choice_str = input('Enter 0, 1, or 2: ')
        is_valid_num = is_valid_entry("number", scorer_choice_str)
    scorer_choice = int(scorer_choice_str)
    if scorer_choice == 0:
        return scoring_algorithms[0]
    elif scorer_choice == 1:
        return scoring_algorithms[1]
    else:
        return scoring_algorithms[2]

def transform(old_dict):
    new_dict = {}
    for (key, value) in old_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key
    return new_dict

new_point_structure = transform(OLD_POINT_STRUCTURE)

def run_program():
    word = initial_prompt()
    algorithm_choice = scorer_prompt()
    print(f'Algorithm Name: {algorithm_choice["name"]}')
    
    scorer_function = algorithm_choice["scoring_function"]
    score = globals()[scorer_function](word)

    print(f"Score for '{word}': {score}")
    
