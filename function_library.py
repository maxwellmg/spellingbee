from random import choice, shuffle
import time
from all_words_gamma_list import all_words_gamma_list as dictionary
from refining_panagrams.checked_panagrams_main import mwd_checked_panagrams

# generate_game() randomly selects a panagram, a mandatory letter within that panagram, and a list of unique letters within the word

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
    return [chosen_panagram, chosen_mandatory_letter, unique_letters]

# find_all_internal_words takes arguments of the chosen panagram and chosen mandatory letter and it finds and returns a list of all words that meet criteria

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

# print_letters creates the print statement for the unique letters of the panagram

def print_letters(variables):
    chosen_mandatory_letter = variables[1]
    unique_letters = variables[2]
    print("    " + unique_letters[0] + "     " + unique_letters[1] + "\n\n" + unique_letters[2] + "     [" + chosen_mandatory_letter + "]     " + unique_letters[3] + "\n\n    " + unique_letters[4] + "     " + unique_letters[5] + "\n")

# points_system takes the argument of a new valid word and determines its value and corresponding print statement

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

# guess_checker checks validity of the new inputted word from the user. it returns None if there is an error with the word (i.e. too short, already inputted, contains non-viable letters, etc.) or it sends the word to the points_system function if its a good word.

def guess_checker(new_word, variables, words_found, good_words, score, highest_possible_score, ranking):
    new_word = new_word.upper()
    chosen_panagram = variables[0]
    chosen_mandatory_letter = variables[1]
    unique_letters = variables[2]
    if new_word.startswith("-") == True:
        return help_menu(new_word, words_found, unique_letters, score, highest_possible_score, good_words, ranking)
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

'''def menu(new_word):
    user_input = ""
    until user_input == "-e"
        if (new_word == "-SHUFFLE") or (new_word == "-SHUFFLE"):
            shuffle(unique_letters)
            print("\n")
        else:
            print'''

def help_menu(new_word, words_found, unique_letters, score, highest_possible_score, good_words, ranking):
    beginning_input = new_word.lower()
    if (beginning_input == "-s") or (beginning_input == "-shuffle"):
        help_shuffle(unique_letters)
    elif (beginning_input == "-r") or (beginning_input == "-rules"):
        help_rules()
    elif (beginning_input == "-t") or (beginning_input == "-tiers"):
        help_tiers()
    elif (beginning_input == "-w") or (beginning_input == "-words_list"):
        help_words_list(words_found)
    elif (beginning_input == "-q") or (beginning_input == "-quit"):
        return quitting_prompt(words_found, score, highest_possible_score, good_words, ranking)
    elif (beginning_input == "-h") or (beginning_input == "-help"):
        while True:
            beginning_input = input("\nHelp menu:\n\n-E: Exit Help Menu\n-S: Shuffle Letters (and Exit Help Menu)\n-R: See Rules\n-T: See Tier Rankings\n-W: See All Successful Word Attempts\n-Q: Quit Game\n\n")
            if (beginning_input == "-e") or (beginning_input == "-exit") or (beginning_input == "e"):
                print("\nExiting Help Menu\n")
                time.sleep(1)
                return None
            elif (beginning_input == "-s") or (beginning_input == "-SHUFFLE") or (beginning_input == "s"):
                return help_shuffle(unique_letters)
            elif (beginning_input == "-r") or (beginning_input == "-rules") or (beginning_input == "r"):
                help_rules()
            elif (beginning_input == "-t") or (beginning_input == "-tiers") or (beginning_input == "t"):
                help_tiers()
            elif (beginning_input == "-w") or (beginning_input == "-words_list") or (beginning_input == "w"):
                help_words_list(words_found)
            elif (beginning_input == "-q") or (beginning_input == "-quit") or (beginning_input == "q"):
                return quitting_prompt(words_found, score, highest_possible_score, good_words, ranking)
            else:
                print("\nCommand not recognized")
                time.sleep(1)
                continue
    else:
        print('\nCommand not recognized. Try "-h" for the Help Menu\n')
        time.sleep(1)

# ranking_finder takes the argument of the good word list and finds the highest possible score for the round

def ranking_finder(good_words):
    #needs to find total number of points available per round (see panagrams, normal words)
    highest_possible_score = 0
    for word in good_words:
        int_points = int(points_system(word)[0])
        highest_possible_score += int_points
    return highest_possible_score

# ranking_assessor factors in the current user score with the highest possible score for the round to find consistent ranks. Rank based on current points as a percent of the total

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
        elif percent > 22 and percent < 100:
            ranking = "How long have you been playing this game??"
        else:
            ranking = "JACK OF ALL TRADES, MASTER OF ALL TRADES. No More words go home."
    return ranking

# loading_menu_prompt picks a random print statement for the opening sequence to improve overall user experience

def loading_menu_prompt():
    possible_statements = ['(Not) picking my nose...', 'Thinking about the meaning of life...', 'Am I getting hungry?...', 'Watching paint dry...', "What's that smell?...", 'Downloading malware (jk)...', 'Converting meters to inches...', 'Descaling the Keurig...', 'Fetching the newspaper...']
    return(choice(possible_statements) + "\n")

# print_recent_inputted_words outputs a short list of inputted words in reverse chronological order

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

def quitting_prompt(words_found, score, highest_possible_score, good_words, ranking):
    while True:
        quitting_input = input("\nAre You Sure You Want to Quit? (Y/N)\n\n")
        if quitting_input.lower() == "y" or quitting_input.lower() == "yes":
            while True:
                second_quitting_input = input("\nWould you like to see the words you missed? (Y/N)\n\n")
                if (second_quitting_input.lower() == "y") or (second_quitting_input.lower() == "yes"):
                    choice = "y"
                    return closing_printout(words_found, score, highest_possible_score, good_words, choice, ranking)
                elif (second_quitting_input.lower() == "n") or (second_quitting_input.lower() == "no"):
                    choice = "n"
                    return closing_printout(words_found, score, highest_possible_score, good_words, choice, ranking)
                elif (second_quitting_input.lower() == "c"):
                    print("\nBack to the game\n")
                    time.sleep(1)
                    return None
                else:
                    print('\nChoice not recognized. Input "c" to cancel quitting.')
                    time.sleep(1)
        elif quitting_input.lower() == "n" or quitting_input.lower() == "no":
            print("\nBack to the game\n")
            time.sleep(1)
            break
        else:
            print('\nChoice not recognized. Please enter either "yes" or "no":')
            time.sleep(1)

def closing_printout(words_found, score, highest_possible_score, good_words, choice, ranking):
    print("\nWords Found:\n\n" + str(words_found))
    time.sleep(2)
    print("\nPoints Scored: " + str(score) + " out of " + str(highest_possible_score) + " potential points")
    time.sleep(2)
    if choice == "y":
        print("\nWords Remaining:\n\n" + str(good_words))
        time.sleep(2)
        print("\nFinal rank: " + ranking)
        time.sleep(2)
        print("\nGoodbye! See you soon\n")
        return "quit"
    else:
        print("\nFinal rank: " + ranking)
        time.sleep(2)
        print("\nGoodbye! See you soon\n")
        return "quit"

def help_rules():
    print("\nGameplay:\n\nThe user is provided 7 different letters, one of which is a [mandatory letter].\nThe user tries to find as many unique words as possible with the letters given\nso long as they all contain the one mandatory letter. Points are assessed based\non word length, and the user tries to obtain as many points as possible,\nachieving different acolades depending on how many points have been acquired.\nEvery game has at least one 'panagram', or word that contains all 7 letters.\n")
    time.sleep(1)
    print("Spelling Bee Rules\n\n1. There is at least 1 panagram per game\n2. Words must be at least 4 letters in length\n3. Words cannot be counted more than once\n4. Words must contain mandatory letter\n5. Point System:\n\t4-letters = 1pt\n\t5-letters = 5pt\n\t6-letters = 6pt\n\t...etc.\n\tPanagram = 7 additional points\n6. Player ranking determined by points gained vs. total points possible\n")
    time.sleep(1)

def help_tiers():
    print("\nTiers")
    time.sleep(1)

def help_words_list(words_found):
    print("\nWords List\n")
    time.sleep(1)
    if words_found == []:
        print("You haven't entered any successful words yet")
        time.sleep(1)
    else:
        sorted_list = sorted(words_found)
        print(str(sorted_list) + "\n")
        time.sleep(1)

def help_shuffle(unique_letters):
    shuffle(unique_letters)
    print("\nShuffling Letters\n")
    time.sleep(1)
