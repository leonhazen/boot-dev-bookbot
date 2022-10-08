import string

def countLetters(text):
    letterCount = {}
    for letter in list(string.ascii_lowercase):
        letterCount[letter] = text.lower().count(letter)

    return letterCount

with open('./books/frankenstein.txt') as f:
    file_contents = f.read()
    
    words = file_contents.split()
    
    print('This book has ' + str(len(words)) + ' words.')

    letterDict = countLetters(file_contents)
    print(letterDict)
