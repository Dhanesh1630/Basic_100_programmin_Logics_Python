rows = int(input("Enter the number of rows for Fibonacci Pattern: "))
def fibonacci_pattern(num):
    a = 0
    b =1
    for i in range(num):
        print(a,end=" ")
        c = a + b
        a = b
        b = c
for i in range(rows):
    fibonacci_pattern(i+1)
    print()
            