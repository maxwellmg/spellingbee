from random import choice, shuffle

list = ["aabbccddeeffgg", "hhiijjkkllmmnn", "ooppqqrrssttuu"]

def generate_game():
    chosen_panagram = choice(list)
    chosen_mandatory_letter = choice(chosen_panagram)
    print("The chosen word is " + chosen_panagram)
    print("The chosen letter is " + chosen_mandatory_letter)
    return chosen_panagram, chosen_mandatory_letter
#variables = generate_game()

def randomize_letters():
    chosen_panagram = "aabbccddeeffgg"
    chosen_mandatory_letter = choice(chosen_panagram)
    unique_letters = []
    all_but = chosen_panagram.replace(chosen_mandatory_letter, "")
    #chosen_panagram(0)
    for letter in all_but:
        if letter in unique_letters:
            pass
        else:
            unique_letters.append(letter)
    print(unique_letters)
    shuffle(unique_letters)
    print(unique_letters)

randomize_letters()

#print(generate_game())
#def print_letters_in_terminal(chosen_panagram, chosen_mandatory_letter):
'''def print_letters_in_terminal(variables):
    chosen_panagram = variables[0]
    chosen_mandatory_letter = variables[1]
    unique_letters = []
    all_but = chosen_panagram.replace(chosen_mandatory_letter, "")
    #chosen_panagram(0)
    for letter in all_but:
        if letter in unique_letters:
            pass
        else:
            unique_letters.append(letter)
        print(unique_letters)
    letter1 = unique_letters[0]
    letter2 = unique_letters[1]
    letter3 = unique_letters[2]
    letter5 = unique_letters[3]
    letter6 = unique_letters[4]
    letter7 = unique_letters[5]
    print("    " + letter1 + "     " + letter2 + "\n" + letter3 + "     [" + chosen_mandatory_letter + "]     " + letter5 + "\n    " + letter6 + "     " + letter7)'''

#generate_game()
#print_letters_in_terminal(generate_game())
#print_letters_in_terminal()
