f = open("panagram_dictionary.txt", "a")
f.write(seven_letter_words)
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())