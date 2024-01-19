import requests
import time
from panagram_list import panagram_list1

def url_creator_checker():
    url_list = []
    good_words_list = []
    bad_words_list = []
    unknown_result_words_list = []
    good_count = 0
    bad_count = 0

    for word in panagram_list1:
        #url = "https://en.wiktionary.org/wiki/" + str(word)
        url = "https://www.merriam-webster.com/dictionary/" + str(word)
        url_list.append(url)
    for url in url_list:
        response = requests.get(url)
        status_code = response.status_code
        word_prep = url.split("/")
        word = word_prep[4].strip("\n")
        if status_code == 200:
            good_count +=1
            good_words_list.append(word)
            print("Good count: " + str(good_count))
        elif status_code == 404:
            bad_count +=1
            #print("This URL was rejected: " + url)
            print("Bad Count: " + str(bad_count))
            bad_words_list.append(word)
        else:
            unknown_result_words_list.append(word)
        #time.sleep(1)
    
    print("The total number of 200 responses is: " + str(good_count) + "\n")
    print("The total number of 404 responses is: " + str(bad_count) + "\n")

#Outfile creation of word lists
    
    with open("checked_panagrams.txt", "a") as f:
        for word in good_words_list:
            g.write('"' + word + '", ')
    f.close()

url_creator_checker()
