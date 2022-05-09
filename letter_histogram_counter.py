#word_list = ["butt", "tushie", "behind", "backside"]
#word_list = ["acdf"]
word_list = ["abcdefg", "aabbccddeeffgg", "aabccdeefgg", "abcd"]
#letter_histogram = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def letter_histogram_counter():
    seven_unique_letter_words = []
    for word in word_list:
        letter_histogram = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        unique_letter_counter = 0
        for letter in word:
            for key in letter_histogram:
                if key == letter:
                    letter_histogram[key] = letter_histogram[key] + 1
                else:
                    pass
            else:
                pass
        for key in letter_histogram:
            #print("Key = " + str(key) + ", Value = " + str(letter_histogram[key]))
            if letter_histogram[key] == 0:
                pass
            else:
                unique_letter_counter +=1
        if unique_letter_counter == 7:
            #only issue is that the list resets each time I try to append a new word, otherwise we're there
            seven_unique_letter_words.append(word)
        else:
            pass
    print(seven_unique_letter_words)

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