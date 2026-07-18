num = input("Enter a number: ")

result = ""

for digit in num:
    if digit == '0':
        result += '1'
    else:
        result += digit

print(result)