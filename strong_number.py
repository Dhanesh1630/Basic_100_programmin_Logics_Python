num = int(input("Enter a number: "))
def strong_number(num):
    original_num = num
    sum_of_digits_factorial = 0
    while num > 0:
        digit = num % 10
        factorial = 1
        for i in range(1, digit +1):
            factorial *= i
        sum_of_digits_factorial += factorial
        num = num // 10
    if original_num == sum_of_digits_factorial:
        print(f"{original_num} is a strong number")
    else :
        print(f"{original_num} is not a strong number")
strong_number(num)                

