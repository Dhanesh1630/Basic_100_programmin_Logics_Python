a = int(input("enter first value: "))
b = int(input("enter second value: "))
c = int(input("enter third value: "))
def largest_of_numbers(a, b ,c):
    if a > b and a > c:
        print(f"{a} is largest number")
    elif b >a and b > c:
        print(f"{b} is largest number")
    elif c > a and c >  b:
        print(f"[c] is largest number")
largest_of_numbers(a , b ,c)                