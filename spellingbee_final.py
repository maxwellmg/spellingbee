import time
from function_library import check_save_file, generate_game, find_all_internal_words, loading_prompt, print_letters, guess_checker, ranking_finder, ranking_assessor, print_recent_inputted_words

print("\n + ~~~~~~~~~~~~~~~~~~~~~ + \n |  Python Spelling Bee  | \n + ~~~~~~~~~~~~~~~~~~~~~ + \n ")
time.sleep(1)

previous_save = check_save_file()
if previous_save == None:
    words_found = []
    count_words_found = 0
    score = 0

    variables = generate_game()
    print("Picking a Panagram...\n")
    time.sleep(0.7)

    good_words = find_all_internal_words(variables)
    print("Finding All Viable Words...\n")
    time.sleep(0.7)

    print(loading_prompt())
    time.sleep(0.7)

    highest_possible_score = ranking_finder(good_words)
    print("Generating Scoring System...\n\n")
    time.sleep(0.7)
else:
    variables = previous_save[0][0]
    good_words = find_all_internal_words(variables)
    words_found = previous_save[0][1]
    highest_possible_score = ranking_finder(good_words)
    for word in words_found:
        good_words.remove(word)
    score = previous_save[0][2]
    count_words_found = len(words_found)
    print("\nWelcome Back! We missed you\n")
    time.sleep(1)

chosen_mandatory_letter = variables[0]
unique_letters = variables[1]

print('Input "-h" to See the Help Menu\n\n')
time.sleep(1.4)

'''
variables = generate_game()

good_words = find_all_internal_words(variables)

#highest_possible_score = ranking_finder(good_words)'''

while True:
    ranking_variables = ranking_assessor(highest_possible_score, score)
    current_rank = ranking_variables[0]
    recent_word_list = print_recent_inputted_words(words_found)
    print("Words Found: " + str(count_words_found) + "\t Score: " + str(score) + "\t Ranking: " + current_rank + "\n\n" + recent_word_list + "\n")
    '''chosen_mandatory_letter = variables[0]
    unique_letters = variables[1]'''
    print_letters(chosen_mandatory_letter, unique_letters)
    new_word = input("Your guess: ")
    current_guess = guess_checker(new_word, variables, words_found, good_words, score, highest_possible_score, ranking_variables, user_choice = None)
    if current_guess == None:
        continue
    elif current_guess == "quit":
        break
    else:
        words_found.append(new_word.upper())
        good_words.remove(new_word.upper())
        new_points = current_guess[0]
        score += int(new_points)
        print(current_guess[1])
        count_words_found += 1
        
        

