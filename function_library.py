import json
from random import choice, shuffle
import time
from dictionary import dictionary
from panagrams import checked_panagrams

# check_save_file checks if a previous game was saved in an outfile, and prompts the user to either start a new game or continue a previous run (and allows for unlimited save spots)

def check_save_file():
    with open("savefile.json") as savefile:
        save_dicts = json.load(savefile)
    if save_dicts == [{}]:
        return None
    else:
        while True:
            if len(save_dicts) == 2:
                save_input = str(input("There is a save file from your last play. Would you like to Continue or Start a New Game?\n\n1: Continue Game\n2: Start New Game\n\n"))
            else:
                save_input = str(input("There are multiple save files from previous plays. Would you like to Continue a Game or Start a New Game?\n\n1: Continue Game\n2: Start New Game\n\n"))
            if save_input == "1":
                count = 1
                for save in save_dicts:
                    if save == {}:
                        continue
                    else:
                        print("\nSave Slot #" + str(count) + "\n")
                        for keys, values in save.items():
                            print(keys + ":", values)
                        count += 1
                        time.sleep(0.5)
                while True:
                    selection = input('\nSelect the Number of the Save Slot you would like to Resume, or input "n" for a New Game\n\n')
                    try:
                        user_choice = int(selection)
                        if (int(user_choice) > 0) and (int(user_choice)<= len(save_dicts)):
                            choice = save_dicts[user_choice]
                            save_state = list(choice.values())
                            return(save_state, user_choice)
                        else:
                            print('\nPlease enter a valid number, or "n" for a New Game\n')
                            continue
                    except ValueError:
                        if selection == "n":
                            print("\n")
                            return None
                        else:
                            print("Please enter a valid number")
                            continue
            elif save_input == "2":
                print("\n")
                return None
            else:
                print("\nPlease select either Continue or New Game\n")
                continue

# generate_game randomly selects a panagram, a mandatory letter within that panagram, and a list of unique letters within the word

def generate_game():
    chosen_panagram = choice(checked_panagrams)
    chosen_mandatory_letter = choice(chosen_panagram)
    unique_letters = []
    all_but = chosen_panagram.replace(chosen_mandatory_letter, "")
    for letter in all_but:
        if letter in unique_letters:
            pass
        else:
            unique_letters.append(letter)
    shuffle(unique_letters)
    return [chosen_mandatory_letter, unique_letters]

# find_all_internal_words takes arguments of the chosen panagram and chosen mandatory letter and it finds and returns a list of all words that meet criteria

def find_all_internal_words(variables):
    chosen_mandatory_letter = variables[0]
    unique_letters = variables[1]  
    all_letters = unique_letters
    all_letters.append(chosen_mandatory_letter)
    good_words = []
    for word in dictionary:
        current_word = []
        if chosen_mandatory_letter not in word:
            continue
        else:
            for letter in word:
                if letter not in all_letters:
                    break
                else:
                    current_word.append(letter)
            if ''.join(current_word) == word:
                good_words.append(word)
            else:
                pass
    unique_letters.remove(chosen_mandatory_letter)      
    return good_words

# print_letters creates the print statement for the unique letters of the panagram

def print_letters(chosen_mandatory_letter, unique_letters):
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

def guess_checker(new_word, variables, words_found, good_words, score, highest_possible_score, ranking_variables, user_choice):
    new_word = new_word.upper()
    chosen_mandatory_letter = variables[0]
    unique_letters = variables[1]
    if new_word.startswith("-") == True:
        return help_menu(variables, new_word, words_found, score, highest_possible_score, good_words, ranking_variables, user_choice)
    else:    
        for letter in new_word:
            if (letter not in unique_letters) and (letter != chosen_mandatory_letter):
                print("\nContains non-viable letter (" + letter.upper() + ")\n")
                return None
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

#help_menu allows the user to use "-" commands look up rules, tiers, words_entered, and shuffle, or to break out of the normal guess_checker function into the help menu and complete those same functions

def help_menu(variables, new_word, words_found, score, highest_possible_score, good_words, ranking_variables, user_choice):
    unique_letters = variables[1]
    ranking = ranking_variables[0]
    rank_marker_list = ranking_variables[1]
    rankings = ranking_variables[2]
    beginning_input = new_word.lower()
    if (beginning_input == "-s") or (beginning_input == "-shuffle"):
        help_shuffle(unique_letters)
    elif (beginning_input == "-r") or (beginning_input == "-rules"):
        help_rules()
    elif (beginning_input == "-t") or (beginning_input == "-tiers"):
        help_tiers(rank_marker_list, rankings)
    elif (beginning_input == "-w") or (beginning_input == "-words_list"):
        help_words_list(words_found)
    elif (beginning_input == "-c") or (beginning_input == "-clean"):
        help_clean_savefile()
    elif (beginning_input == "-q") or (beginning_input == "-quit"):
        return quitting_prompt(variables, words_found, score, highest_possible_score, good_words, ranking, user_choice)
    elif (beginning_input == "-h") or (beginning_input == "-help"):
        while True:
            beginning_input = input("Help menu:\n\n-E: Exit Help Menu\n-S: Shuffle Letters (and Exit Help Menu)\n-R: See Rules\n-T: See Tier Rankings\n-W: See All Successful Word Attempts\n-C: Clean Save File\n-Q: Quit Game\n\n")
            if (beginning_input == "-e") or (beginning_input == "-exit") or (beginning_input == "e"):
                print("\nExiting Help Menu\n")
                time.sleep(1)
                return None
            elif (beginning_input == "-s") or (beginning_input == "-SHUFFLE") or (beginning_input == "s"):
                return help_shuffle(unique_letters)
            elif (beginning_input == "-r") or (beginning_input == "-rules") or (beginning_input == "r"):
                help_rules()
            elif (beginning_input == "-t") or (beginning_input == "-tiers") or (beginning_input == "t"):
                help_tiers(rank_marker_list, rankings)
            elif (beginning_input == "-w") or (beginning_input == "-words_list") or (beginning_input == "w"):
                help_words_list(words_found)
            elif (beginning_input == "-c") or (beginning_input == "-clean") or (beginning_input == "c"):
                help_clean_savefile()
            elif (beginning_input == "-q") or (beginning_input == "-quit") or (beginning_input == "q"):
                return quitting_prompt(variables, words_found, score, highest_possible_score, good_words, ranking, user_choice)
            else:
                print("\nCommand not recognized")
                time.sleep(1)
                continue
    else:
        print('\nCommand not recognized. Try "-h" for the Help Menu\n')
        time.sleep(1)

# ranking_finder takes the argument of the good word list and finds the highest possible score for the round

def ranking_finder(good_words):
    highest_possible_score = 0
    for word in good_words:
        int_points = int(points_system(word)[0])
        highest_possible_score += int_points
    return highest_possible_score

# ranking_assessor factors in the current user score with the highest possible score for the round to find consistent ranks. Rank based on current points as a percent of the total

def ranking_assessor(highest_possible_score, current_score):
    percents = [1.5, 4.5, 7.5, 14, 24, 38, 48, 68]
    rank_marker_list = ["0"]
    for number in percents:
        rank_marker = round((number / 100) * highest_possible_score)
        rank_marker_list.append(rank_marker)
    
    rankings = ["Born Yesterday", "Pre-K Reading Level", "Somebody knows their ABCs", "Hooked on Phonics", "Mediocrity ain't half bad (jk)", "High School Reading Level", "I May be in Debt, but I am College Educated", "Congrats on your Master's Thesis, Dweeb", "How long have you been playing this game??", "JACK OF ALL TRADES, MASTER OF ONE. No More Words Left. What'd You Expect? A Cookie? Go Touch Grass."]

    if current_score == 0:
        ranking = "Born Yesterday"
    else:
        if current_score == highest_possible_score:
            ranking = rankings[9]
        elif current_score >= rank_marker_list[8]:
            ranking = rankings[8]
        elif current_score >= rank_marker_list[7]:
            ranking = rankings[7]
        elif current_score >= rank_marker_list[6]:
            ranking = rankings[6]
        elif current_score >= rank_marker_list[5]:
            ranking = rankings[5]
        elif current_score >= rank_marker_list[4]:
            ranking = rankings[4]
        elif current_score >= rank_marker_list[3]:
            ranking = rankings[3]
        elif current_score >= rank_marker_list[2]:
            ranking = rankings[2]
        elif current_score >= rank_marker_list[1]:
            ranking = rankings[1]
        else:
            ranking = rankings[0]
        
        
        
        
        
        
        
        

    return [ranking, rank_marker_list, rankings]

# loading_prompt picks a random print statement for the opening sequence to improve overall user experience

def loading_prompt():
    possible_statements = ['(Not) Picking my Nose...', 'Thinking About the Meaning of Life...', 'Am I Getting Hungry?...', 'Watching Paint Dry...', "What's That Smell?...", 'Downloading Malware (jk)...', 'Converting Meters to Inches...', 'Descaling the Keurig...', 'Fetching the Newspaper...']
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

# quitting_prompt takes user through options for quitting the game, allowing for mistaken quits to be avoided and for all answers to be revealed

def quitting_prompt(variables, words_found, score, highest_possible_score, good_words, ranking, user_choice):
    while True:
        quitting_input = input("\nAre You Sure You Want to Quit? (Y/N)\n\n")
        if quitting_input.lower() == "y" or quitting_input.lower() == "yes":
            while True:
                second_quitting_input = input("\nWould you like to save and return later? (Y/N)\n\n")
                if (second_quitting_input.lower() == "y") or (second_quitting_input.lower() == "yes"):
                    while True:
                        if user_choice == None:
                            create_new_save(variables, words_found, score)
                            print("\nSaving...\n")
                            time.sleep(1)
                            print("Saved! Looking forward to next time\n")
                            return "quit"
                        third_quitting_input = input("\nWould you like to Overwrite Save File or Save a New File?\n\nO: Overwrite File\nN: New File\n\n")
                        if (third_quitting_input.lower() == "o") or (third_quitting_input.lower() == "overwrite") or (third_quitting_input.lower() == "overwrite file"):
                            overwrite_save(variables, words_found, score, user_choice)
                        elif (third_quitting_input.lower() == "n") or (third_quitting_input.lower() == "new") or (third_quitting_input.lower() == "new file"):
                            create_new_save(variables, words_found, score)
                            print("\nSaving...\n")
                            time.sleep(1)
                            print("Saved! Looking forward to next time\n")
                            return "quit"
                        else:
                            print('\nChoice not recognized. Input "c" to cancel quitting.')
                            time.sleep(1)
                elif (second_quitting_input.lower() == "n") or (second_quitting_input.lower() == "no"):
                    return closing_printout(words_found, score, highest_possible_score, good_words, ranking)
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

# closing_printout takes users inputs for the quitting_prompt and delivers a custom closing message based on users' decision to save or not save

def closing_printout(words_found, score, highest_possible_score, good_words, ranking):
    print("\nWords Found:\n\n" + str(words_found))
    time.sleep(2)
    print("\nPoints Scored: " + str(score) + " out of " + str(highest_possible_score) + " potential points")
    time.sleep(2)
    print("\nWords Remaining:\n\n" + str(good_words))
    time.sleep(2)
    print("\nFinal rank: " + ranking)
    time.sleep(2)
    print("\nGoodbye! See you soon\n")
    return "quit"

# help_rules prints the rules of how to play the game

def help_rules():
    print("\nGameplay:\n\nThe user is provided 7 different letters, one of which is a [mandatory letter].\nThe user tries to find as many unique words as possible with the letters given\nso long as they all contain the one mandatory letter. Points are assessed based\non word length, and the user tries to obtain as many points as possible,\nachieving different acolades depending on how many points have been acquired.\nEvery game has at least one 'panagram', or word that contains all 7 letters.\n")
    time.sleep(1)
    print("Spelling Bee Rules\n\n1. There is at least 1 panagram per game\n2. Words must be at least 4 letters in length\n3. Words cannot be counted more than once\n4. Words must contain mandatory letter\n5. Point System:\n\t4-letters = 1pt\n\t5-letters = 5pt\n\t6-letters = 6pt\n\t...etc.\n\tPanagram = 7 additional points\n6. Player ranking determined by points gained vs. total points possible\n")
    time.sleep(1)

# help_tiers prints the tier rankings and their run-specific values

def help_tiers(rank_marker_list, rankings):
    print("\nScore Tiers\n")
    time.sleep(1)
    count = 0
    print("Score:  Ranking:\n")
    for number in rank_marker_list:
        print("  " + str(number) + "\t" + rankings[count])
        count += 1
    print('\n')

# help_words_list prints words_found in alphabetical order

def help_words_list(words_found):
    print("\nWords List\n")
    time.sleep(1)
    if words_found == []:
        print("You haven't entered any successful words yet\n")
        time.sleep(1)
    else:
        sorted_list = sorted(words_found)
        print(str(sorted_list) + "\n")
        time.sleep(1)

# help_shuffle shuffles letters around

def help_shuffle(unique_letters):
    shuffle(unique_letters)
    print("\nShuffling Letters\n")
    time.sleep(1)

# help_clean_savefile allows user to choose previous save states to erase from the savefile

def help_clean_savefile():
    print("\nClean Save File\n")
    time.sleep(1)
    with open("savefile.json") as savefile:
        save_dicts = json.load(savefile)
    if save_dicts == [{}]:
        print("There are no Save Files to erase at this time")
        return None
    count = 1
    for save in save_dicts:
        if save == {}:
            continue
        else:
            print("\nSave Slot #" + str(count) + "\n")
            for keys, values in save.items():
                print(keys + ":", values)
            count += 1
            time.sleep(0.5)
    while True:
        user_input = input('\nPlease select a savefile to delete, or input "e" to return\n\n')
        try:
            deletion_choice = int(user_input)
            if (deletion_choice > 0) and (deletion_choice <= len(save_dicts)):
                print(f"\nSave Slot #{deletion_choice} has been selected\n\n" + str(save_dicts[deletion_choice]))
                time.sleep(1)
                while True:
                    new_input = input("\nAre you sure you want to delete? (Y/N)\n\n")
                    if (new_input.lower() == "y") or (new_input.lower() == "yes"):
                        choice = save_dicts[deletion_choice]
                        save_dicts.remove(choice)
                        with open("savefile.json", "w") as f:
                            json.dump(save_dicts, f)
                        f.close()
                        print(f"\nSave Slot #{deletion_choice} has been deleted. \n")
                        time.sleep(1)
                        break
                    elif (new_input.lower() == "n") or (new_input.lower() == "no"):
                        print(f"\nNot deleting Save Slot #{deletion_choice}\n")
                        break
                    else:
                        print("\nPlease choose to delete (Y), or not to delete (N)\n")
                        time.sleep(0.5)
        except:
            ValueError
            if user_input.lower() == "e":
                print("\nReturning\n")
                time.sleep(1)
                break
            else:
                print('\nPlease a savefile to delete, or input "e" to return\n')
                time.sleep(0.5)
        
# create_new_save stores letters, words found, and score from your current game in an outfile that can be accessed at the beginning of the program

def create_new_save(variables, words_found, score):
    with open("savefile.json") as f:
        data = json.load(f)
    new_save_dict = {'letters': variables, 'words_found': words_found, 'score': score, 'last updated': time.strftime("%m/%d/%Y %H:%M")}
    data.append(new_save_dict)
    with open("savefile.json", "w") as f:
        json.dump(data, f)
    f.close()

# overwrite_save unlike create_new_save, takes the additional variable of user_choice given when the save state was selected to remove that file as it saves the new file

def overwrite_save(variables, words_found, score, user_choice):
    with open("savefile.json") as f:
        data = json.load(f)
    new_save_dict = {'letters': variables, 'words_found': words_found, 'score': score, 'last updated': time.strftime("%m/%d/%Y %H:%M")}
    data.remove(user_choice)
    data.append(new_save_dict)
    with open("savefile.json", "w") as f:
        json.dump(data, f)
    f.close()