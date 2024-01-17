# spellingbee
replicating NYTs spelling bee game just for fun

Game will be capable of being run in Terminal

Utilizing Read Me as a dev log to track tasks needing to be completed, as well as progress

Spelling Bee Description
    NYT offers this app to subscribers. This version will initially try to replicate functionality before toying with the premise
    The game is simple. The user is provided 7 different letters, one of which is a mandatory letter. The user tries to find as many unique words as possible with the letters given so long as they all contain the one mandatory letter. Points are assessed based on word length, and the user tries to get as many points as possible, achieving different acolades depending on how many points have been acquired. Every day there is at least one "panagram", or word that contains all 7 letters. Panagrams also get a large point bump.

Spelling Bee Rules
1. There is at least 1 panagram per day
2. Words must be at least 4 letters in length
3. Words cannot be counted more than once
4. Words must contain mandatory letter
5. Figure out the Point System
    4-letters = 1pt
    5-letters = 5pt
    6-letters = 6pt
    Panagram = x additional points
    Solve algebracally eventually
6. Accolades achieved based on points gained are proportional based on how many points are possible in a day.

Tasks to accomplish
1. Create a list of eligible panagrams
  a. Find a free online dictionary (COMPLETE)
  b. Discern a discreet list of words that contain exactly 7 unique letters
    - create a program that makes histogram for each word (COMPLETE)
    - run program on dictionary to create list of just panagrams, save as new file (COMPLETE)
    - In completing this, we see a new problem: most of these words are rubbish. Need to find a frequency measurer to disclude ridiculous words
        -Possible solution: find a large text or several large texts. Create find threshhold of frequency for words that would include/disclude word from final list
2. For each panagram, find a list of words that can only be made from its letters
3. Create Print Statements for a Terminal Run-through
    -Potential print statements:
        "Randomly selecting a Word"
        "Randomly picking a letter in that Word"
        "Curating custom word list"
        Perhaps a randomly selected loading phrase ["crossing ts, dotting is", "filtering out curse words", etc]
4. Create a Terminal Help Menu
    -Potential Menu items
        -(R): Print rules of the game
        -(S): See current score
        -(Q): Quit out of game, lose progress
        -(H): Exit help menu
        -(W): See words successfully submitted thus far
        -Make a toggle for print statements?