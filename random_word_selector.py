from random import choice

list = ["abc", "def", "ghi"]
chosen_panagram = choice(list)
chosen_mandatory_letter = choice(chosen_panagram)
print("The chosen word is " + chosen_panagram)
print("The chosen letter is " + chosen_mandatory_letter)