
with open('./books/frankenstein.txt') as f:
    file_contents = f.read()
    
    words = file_contents.split()
    
    print('This book has ' + str(len(words)) + ' words.')