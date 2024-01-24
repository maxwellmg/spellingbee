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
    print("Words Found: " + str(count_words_found) + "\t Score: " + str(score) + "\t Ranking: N/A" + "\n")
    print_letters(variables, unique_letters)
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
        
        

