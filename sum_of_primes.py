def is_prime(num):
    if num < 2:
        return False
    for i in range(2 , int(num**0.5) +1):
        if num % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
found = False
for i in range(2,num):
    if is_prime(i) and is_prime(num-i):
        print(f"{num} can be expressed as the sum of two prime numbers: {i} + {num-i}")
        found = True
        break
if not found:
    print(f"{num} cannot be expressed as the sum of two prime numbers")
