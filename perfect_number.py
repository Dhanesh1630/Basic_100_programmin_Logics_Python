num = int(input("Enter a number: "))
def perfect_number(num):
    original_num = num
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == original_num:
        print(f"{original_num} is a perfect number")
    else :
        print(f"{original_num} is not a perfect number")
perfect_number(num)                    