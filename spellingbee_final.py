import time
from function_library import generate_game, find_all_internal_words, randomize_letters, find_game_letters, print_letters, guess_checker

print("\n + ~~~~~~~~~~~~~~~~~~~~~ + \n |  Python Spelling Bee  | \n + ~~~~~~~~~~~~~~~~~~~~~ + \n ")
time.sleep(1)
print("Input -h to see the help menu")

words_found = []
count_words_found = 0
score = 0

variables = generate_game()
good_words = find_all_internal_words(variables)

#print("Words Found: " + str(count_words_found) + "\t Score: " + str(score))
unique_letters = find_game_letters(variables)

while True:
    print("Words Found: " + str(count_words_found) + "\t Score: " + str(score))
    print_letters(variables, unique_letters)
    new_word = input("Your guess: ")
    guess_checker(new_word, variables, words_found, good_words)
    if guess_checker(new_word, variables, words_found, good_words) == None:
        continue
    else:
        words_found.append(new_word)
        score += new_points
        count_words_found += 1

#randomize_letters(variables, unique_letters)
#if input
