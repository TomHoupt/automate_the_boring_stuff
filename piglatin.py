# piglatin.py

#English to Pig Latin

print('Enter the English message to translate into Pig Latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = [] #a list of the words in Pig Latin
for word in message.split():
    #Seperate the non-letters at the start of this word:
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue


    #seperate the non-letters at the end of this word:
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word [-1] + suffix_non_letters
        word = word[:-1]

    #Remember if the wrod was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() #Make the word lowercase for translation

    #Seperate the consonants at the start of this word:
    prefix_consonants = ''
    while len(word) > 0 and not [0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    #Add the Pig Latin ending to the word:
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else: word += 'yay'

    #set the word back to uppercase or title case:
    if wasUpper:
        word = word.supper()
    if wasTitle:
        word = word.title()

    #add the non-letters back to the start of end of the word.
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

#join all the words back to the start or end of the word
print(' '.join(pig_latin))


