#from refining_panagrams.checked_panagrams_main import mwd_checked_panagrams
#from all_words_beta_list import all_words_beta_list as dictionary
from function_library import generate_game, find_all_internal_words, randomize_letters, print_letters_in_terminal
#from random import choice, shuffle

print("Welcome to the Spelling Bee! Hope you enjoy.")
#"Press (H) if you need help"

#chosen_panagram = choice(mwd_checked_panagrams)
#chosen_mandatory_letter = choice(chosen_panagram)
variables = generate_game()
#variables = [chosen_panagram, chosen_mandatory_letter]
find_all_internal_words(variables)
print_letters_in_terminal(variables)
if input
