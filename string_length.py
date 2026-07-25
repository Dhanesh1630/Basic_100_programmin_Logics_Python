str = input("Enter a string: ")
def string_length(str):
    string_length = 0
    for i in str:
        string_length += 1
    return string_length    
print("Then length of the string is :",string_length(str))