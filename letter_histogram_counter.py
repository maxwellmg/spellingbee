#word_list = ["butt", "tushie", "behind", "backside"]
word_list = ["abcdefg", "aabbccddeeffgg", "aabccdeefgg"]
#letter_histogram = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def letter_histogram_counter():
    #word_histogram = {}
    for word in word_list:
        letter_histogram = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        for letter in word:
            for key in letter_histogram:
                if key == letter:
                    letter_histogram[key] = letter_histogram[key] + 1
                else:
                    pass
                #print(letter_histogram.value(letter))
            else:
                pass
        print(letter_histogram)
letter_histogram_counter()

'''capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
for key in capitals:
    print("Key = " + key + ", Value = " + capitals[key])'''




'''Program capable of taking a list of words, crossreferences letters of word with dict with empty values, and temporarily makes histogram of letters contained within that word. Used to determine exact number of unique letters per word

Next step is to find len of letters with value >1 to see if theyre exactly 7 (for panagram)
def letter_histogram_counter():
    #word_histogram = {}
    for word in word_list:
        letter_histogram = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        for letter in word:
            for key in letter_histogram:
                if key == letter:
                    letter_histogram[key] = letter_histogram[key] + 1
                else:
                    pass
                #print(letter_histogram.value(letter))
            else:
                pass
        print(letter_histogram)
letter_histogram_counter()'''