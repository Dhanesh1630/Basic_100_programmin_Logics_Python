num = int(input("Enter a number: "))
def is_armstrong(num):
    original_num = num
    sum_of_cubes = 0
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num = num // 10
    if original_num == sum_of_cubes:
        print(f"{original_num} is an Armstrong number")
    else:
        print(f"{original_num} is not an Armstrong number")
is_armstrong(num)                