numbers = input("Enter numbers with single space seperated: ").split()
def lcm_gcd(numbers):
    numbers = list(map(int, numbers))
    gcd = numbers[0]
    for i in numbers[1:]:
        while i:
            gcd , i = i, gcd%i
    print(f"The GCD of {numbers} is: {gcd}")        
    lcm = 1
    for i in numbers :
        lcm *= i//gcd  
    print(f"The LCM of {numbers} is: {lcm}")
lcm_gcd(numbers)              