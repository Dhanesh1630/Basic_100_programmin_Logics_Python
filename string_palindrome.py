str = input("Enter a string: ")
def string_palindrome(str):
    str = str.lower()
    if str == str[::-1]:
        print("The string is a palindrome")
    else :
        print("The string is not a palindrome")    

string_palindrome(str)        