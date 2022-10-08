import string

def countLetters(text):
    letterCount = {}
    for letter in list(string.ascii_lowercase):
        letterCount[letter] = text.lower().count(letter)

    return letterCount

with open('./books/frankenstein.txt') as f:
    # Read in book file
    file_contents = f.read()
    
    # Split into list of words
    words = file_contents.split()
    
    # Print the count of words
    print('This book has ' + str(len(words)) + ' words.')

    # Run the countLetters function to create dictionary of letters and their counts
    letterDict = countLetters(file_contents)

    # Sort the letters into an ordered list based on the count of that letter
    sortedLetters = sorted(letterDict, key=letterDict.get, reverse=True)

    # Loop through the ordered list of letters and print the count for each of them
    for letter in sortedLetters:
        print("The '" + letter + "' character was found " + str(letterDict[letter]) + " times")
