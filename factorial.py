num = int(input("Enter a number: "))
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"The factorial of {num} is : {factorial(num)}")
