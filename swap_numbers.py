a = int(input("enter first number:"))
b = int(input("enter second number:"))
def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a = a+b
    b = a-b
    a = a-b
    print(f"After swapping: a = {a}, b = {b}")
swap_numbers(a , b)    