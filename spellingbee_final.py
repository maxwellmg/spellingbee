import time
from function_library import generate_game, find_all_internal_words, loading_menu_prompt, print_letters, guess_checker, ranking_finder, ranking_assessor

print("\n + ~~~~~~~~~~~~~~~~~~~~~ + \n |  Python Spelling Bee  | \n + ~~~~~~~~~~~~~~~~~~~~~ + \n ")
time.sleep(1)

#print("Input -h to see the help menu")

words_found = []
count_words_found = 0
score = 0

variables = generate_game()
print("Picking a Panagram...\n")
time.sleep(1)

good_words = find_all_internal_words(variables)
print("Finding all viable words...\n")
time.sleep(1)

print(loading_menu_prompt())
time.sleep(1)

highest_possible_score = ranking_finder(good_words)
print("Generating scoring system...\n")
time.sleep(1)

while True:
    ranking = ranking_assessor(highest_possible_score, score)
    print("Words Found: " + str(count_words_found) + "\t Score: " + str(score) + "\t Ranking: " + ranking + "\n")
    #print_letters(variables, unique_letters)
    print_letters(variables)
    new_word = input("Your guess: ")
    #guess_checker(new_word, variables, words_found, good_words)
    if guess_checker(new_word, variables, words_found, good_words) == None:
        continue
    else:
        changes = guess_checker(new_word, variables, words_found, good_words)
        words_found.append(new_word.upper())
        good_words.remove(new_word.upper())
        new_points = changes[0]
        score += int(new_points)
        print(changes[1])
        count_words_found += 1
        
        

