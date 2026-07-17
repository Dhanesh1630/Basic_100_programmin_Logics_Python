num = int(input("Enter a number: "))
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10)+ digit
        num = num // 10
    if original_num == reversed_num:
        print(f"{original_num} is palindrome")
    else:
        print(f"{original_num} is not palindrome")
is_palindrome(num)                