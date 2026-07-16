char = input("enter a character: ")
def checkChar(char):
    if char in 'aeiouAEIOU':
        print(f"{char} is a vowel")
    else :
        print(f"{char} is a consonanat")
checkChar(char)            