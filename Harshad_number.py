num = int(input("Enter a number: "))
def harshad_number(num):
    original_num = num
    sum_of_digits = 0
    while num > 0 :
        digit = num % 10
        sum_of_digits += digit
        num = num // 10
    if original_num % sum_of_digits == 0:
        print(f"{original_num} is a Harshad number")
    else:
        print(f"{original_num} is not a Harshad number")
harshad_number(num)                