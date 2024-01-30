from random import choice, shuffle
from all_words_beta_list import all_words_beta_list as dictionary
from refining_panagrams.checked_panagrams_main import mwd_checked_panagrams

def generate_game():
    chosen_panagram = choice(mwd_checked_panagrams)
    chosen_mandatory_letter = choice(chosen_panagram)
    #print(chosen_panagram + "\n" + chosen_mandatory_letter)
    unique_letters = []
    all_but = chosen_panagram.replace(chosen_mandatory_letter, "")
    for letter in all_but:
        if letter in unique_letters:
            pass
        else:
            unique_letters.append(letter)
    shuffle(unique_letters)
    #print("    " + unique_letters[0] + "     " + unique_letters[1] + "\n" + unique_letters[2] + "     [" + chosen_mandatory_letter + "]     " + unique_letters[3] + "\n    " + unique_letters[4] + "     " + unique_letters[5])
    #return unique_letters
    return [chosen_panagram, chosen_mandatory_letter, unique_letters]

# given arguments of chosen panagram and chosen mandatory letter, function finds and returns list of all words that meet criteria
def find_all_internal_words(variables):
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

def print_letters(variables):
    chosen_mandatory_letter = variables[1]
    unique_letters = variables[2]
    print("    " + unique_letters[0] + "     " + unique_letters[1] + "\n\n" + unique_letters[2] + "     [" + chosen_mandatory_letter + "]     " + unique_letters[3] + "\n\n    " + unique_letters[4] + "     " + unique_letters[5] + "\n")

def points_system(new_word):
    new_word_unique_letters = []
    for letter in new_word:
        if letter in new_word_unique_letters:
            pass
        else:
            new_word_unique_letters.append(letter)
    if len(new_word_unique_letters) == 7:
        points = str(len(new_word) + 7)
        return_statement = "\n" + new_word + " PANAGRAM +" + points + "\n"
    else:
        if len(new_word) == 4:
            points = "1"
        else:
            points = str(len(new_word))
        return_statement = "\n"+ new_word + " +" + points + "\n"
    return [points, return_statement]

def guess_checker(new_word, variables, words_found, good_words):
    new_word = new_word.upper()
    chosen_panagram = variables[0]
    chosen_mandatory_letter = variables[1]
    unique_letters = variables[2]
    if new_word == "-SHUFFLE":
        shuffle(unique_letters)
        print("\n")
    else:    
        for letter in new_word:
            if letter not in chosen_panagram:
                print("\nContains non-viable letter (" + letter.upper() + ")\n")
                return None
                #break
            else:
                pass
        if len(new_word) < 4:
            print("\nToo Short\n")
            return None
        elif chosen_mandatory_letter not in new_word:
            print("\nMissing middle letter\n")
            return None
        elif new_word in words_found:
            print("\n" + new_word + " has already been found\n")
            return None    
        else:
            if new_word in good_words:
                new_points = points_system(new_word)[0]
                return_statement = points_system(new_word)[1]
                return [new_points, return_statement]
            else:
                print("\n" + new_word + " not in word list\n")

def ranking_finder(good_words):
    #needs to find total number of points available per round (see panagrams, normal words)
    highest_possible_score = 0
    for word in good_words:
        int_points = int(points_system(word)[0])
        highest_possible_score += int_points
    return highest_possible_score

def ranking_assessor(highest_possible_score, current_score):
    #establish percentages for ranking, have ranking titles
    total = highest_possible_score
    current = current_score
    percent = 0

    if current == 0:
        ranking = "N/A"
    else:
        percent = (current / total) * 100
        if percent <= 1:
            ranking = "Born Yesterday"
        elif (percent > 1 and percent <= 3):
            ranking = "Pre-K Reading Level"
        elif percent > 3 and percent <= 7:
            ranking = "Somebody knows their ABCs"
        elif percent > 7 and percent <= 11:
            ranking = "Mediocrity ain't half bad (jk)"
        elif percent > 11 and percent <= 16:
            ranking = "High School Reading Level"
        elif percent > 16 and percent <= 22:
            ranking = "I May be in Debt, but I am College Educated"
        elif percent > 22 and percent <= 100:
            ranking = "How long have you been playing this game??"
        else:
            ranking = "JACK OF ALL TRADES, MASTER OF ALL TRADES. No More words go home."
    return ranking

def loading_menu_prompt():
    possible_statements = ['(Not) picking my nose...', 'Thinking about the meaning of life...', 'Am I getting hungry?...', 'Watching paint dry...', "What's that smell?...", 'Downloading malware (jk)...', 'Converting meters to inches...', 'Descaling the Keurig...', 'Fetching the newspaper...']
    return(choice(possible_statements) + "\n")

def print_recent_inputted_words(words_found):
    printed_list = []
    if words_found == []:
        return "[Recently found words here]"
    else:
        for word in reversed(words_found):
            if len(", ".join(printed_list)) < 50:
                printed_list.append(word)
            else:
                return "[" + ", ".join(printed_list) + "...]"
        return "[" + ", ".join(printed_list) + "]"