Spelling Bee Rules

1. Create a list of eligible words
  a. Find a dictionary of just words
    To speed it up, find a list of 7 or more letter words
  b. Create a list where each letter is one item
  c. create a histogram program that counts the number of instances for each letter in each word. If a word hits >= 8 different items from the letter list, its ineligible.
2. Figure out the Point System
    4-letters = 1pt
    5-letters = 5pt
    6-letters = 6pt
    assuming word is good:
        if len(word) < 4
            pass
        if len(word)
3. Rules for User interactions
  a. <=3 letters = Too short
  b. Doesnt contain main letter = error
  c. if both requirements are hit, it then cross references word with dictionary. If match, assess points. If not match = Word not in dictionary
  d. if the word provided has already been provided, no additional points will be assessed
4. Create a list each day based on the word/s chosen so it doesnt have to cycle through all 500k words
