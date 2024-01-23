from random import choice, shuffle
from all_words_beta_list import all_words_beta_list as dictionary
from refining_panagrams.checked_panagrams_main import mwd_checked_panagrams

#sample_list = ["aabbccddeeffgg", "hhiijjkkllmmnn", "ooppqqrrssttuu"]

def generate_game():
    chosen_panagram = choice(mwd_checked_panagrams)
    chosen_mandatory_letter = choice(chosen_panagram)
    print(chosen_panagram + "\n" + chosen_mandatory_letter)
    return [chosen_panagram, chosen_mandatory_letter]

def find_all_internal_words(variables):

    # given arguments of chosen panagram and chosen mandatory letter, function finds and returns list of all words that meet criteria

    chosen_panagram = variables[0]
    chosen_mandatory_letter = variables[1]
    good_words = []
    for word in dictionary:
        current_word = []
        if chosen_mandatory_letter not in word:
            continue
        else:
            for letter in word:
                if letter not in chosen_panagram:
                    break
                else:
                    current_word.append(letter)
            if ''.join(current_word) == word:
                good_words.append(word)
            else:
                pass
    return good_words

def randomize_letters(variables, unique_letters):
    chosen_mandatory_letter = variables[1]
    shuffle(unique_letters)
    print("    " + unique_letters[0] + "     " + unique_letters[1] + "\n" + unique_letters[2] + "     [" + chosen_mandatory_letter + "]     " + unique_letters[3] + "\n    " + unique_letters[4] + "     " + unique_letters[5])

def find_game_letters(variables):
    chosen_panagram = variables[0]
    chosen_mandatory_letter = variables[1]
    unique_letters = []
    all_but = chosen_panagram.replace(chosen_mandatory_letter, "")
    for letter in all_but:
        if letter in unique_letters:
            pass
        else:
            unique_letters.append(letter)
    shuffle(unique_letters)
    print("    " + unique_letters[0] + "     " + unique_letters[1] + "\n" + unique_letters[2] + "     [" + chosen_mandatory_letter + "]     " + unique_letters[3] + "\n    " + unique_letters[4] + "     " + unique_letters[5])
    return unique_letters