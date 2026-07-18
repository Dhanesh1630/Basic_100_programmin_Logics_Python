def gcd(a ,b):
    while b:
        a ,b = b, a%b
    return a
num1 =int(input("Enter the numerator of the first fraction: "))
den1 = int(input("Enter the denominator of the first fraction: "))
num2 = int(input("Enter the numerator of the second fraction: "))
den2 = int(input("Enter the denominator of the second fraction: "))
num = num1 * den2 + num2 * den1
den = den1 * den2
g = gcd(num ,den)
print(f"The sume of the fractions is: {num //g} / {den//g}")
