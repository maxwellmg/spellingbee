To Run Program:
 - Open any Terminal
 - (optional) input <python -V> (this program was written in 3.6.5. Consider creating an .env in 3.6.5 if troubles arise)
 - Make sure you are in the ../SPELLINGBEE subdirectory
 - Input <python spellingbee_final.py>
 - Enjoy!

To Exit, either:
- Input -q to begin the quitting procedure (RECOMMENDED) or
- Input CTRL + C to force quit the program

Spelling Bee Description
    NYT offers this app to subscribers and offers one unique set of letters per day. This version replicates the core functionality with the added ability to play unlimited run-throughs.
    
Gameplay:
    The user is provided 7 different letters, one of which is a [mandatory letter]. The user tries to find as many unique words as possible with the letters given so long as they all contain the one mandatory letter. Points are assessed based on word length, and the user tries to obtain as many points as possible, achieving different acolades depending on how many points have been acquired. Every game has at least one "panagram", or word that contains all 7 letters. 

Spelling Bee Rules
1. There is at least 1 panagram per game
2. Words must be at least 4 letters in length
3. Words cannot be counted more than once
4. Words must contain mandatory letter
5. Point System:
    4-letters = 1pt
    5-letters = 5pt
    6-letters = 6pt
    ...etc.
    Panagram = 7 additional points
6. Accolades achieved based on points gained are proportional based on how many points are possible in a game.

Scoring Tiers (calculated as a percentage from Points Obtained / Total Points Available)
Tier 0: 0 >= Score < 1.5%
Tier 1: 1.5 >= Score < 4.5%
Tier 2: 4.5 >= Score < 7.5%
Tier 3: 7.5 >= Score < 14%
Tier 4: 14 >= Score < 24%
Tier 5: 24 >= Score < 38%
Tier 6: 38 >= Score < 48%
Tier 7: 48 >= Score < 68%
