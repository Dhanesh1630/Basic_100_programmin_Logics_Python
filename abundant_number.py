num = int(input("enter number: "))
def abundant_number(num):
    original_num = num
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors > original_num:
        print(f"{original_num} is an abundant number")
    else:
        print(f"{original_num} is not an abundant number")
abundant_number(num)                    