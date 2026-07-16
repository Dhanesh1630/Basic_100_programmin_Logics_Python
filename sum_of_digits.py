num = int(input("enter a number: "))
def sum_of_digits(num):
    sum = 0 
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10
    print(f"sum of digits is {sum}")
sum_of_digits(num)        