str = input("Enter a string: ")
def string_reverse(str):
    reversed_string = ""
    for i in str:
        reversed_string = i + reversed_string
    return reversed_string
print("The reversed string is :",string_reverse(str))    