str = input("Enter a string of words: ")
words = str.split()
for word in words:
    if len(word) == 1:
        print(word.upper(), end = " ")
    else:
        print(word[0].upper() + word[1:-1] + word[-1].upper(), end = " ")
            
    