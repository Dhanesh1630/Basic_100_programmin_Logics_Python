str = input("Enter a string: ")
def string_swapcase(str):
    result = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= "Z":
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result
print("The swapcase string is : ", string_swapcase(str))
                