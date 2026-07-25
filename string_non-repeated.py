str = input("Enter a string: ")
def non_repeated_characters(str):
    non_repeated = ""
    for i in str:
        if str.count(i) == 1:
            non_repeated += i
    return non_repeated
print("The non-repeated characters in the string are :", non_repeated_characters(str))        