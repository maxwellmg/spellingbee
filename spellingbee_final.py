from .../refining_panagrams/checked_panagrams_main import mwd_checked_panagrams
from all_words_beta_list import all_words_beta_list as dictionary
import function_library
from random import choice, shuffle

print("Welcome to the Spelling Bee! Hope you enjoy.")
#"Press (H) if you need help"
variables = generate_game()
find_all_internal_words(variables)
print_letters_in_terminal(variables)
