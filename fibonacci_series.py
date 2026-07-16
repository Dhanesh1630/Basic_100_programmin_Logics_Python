num = int(input("enter number: "))
def fibonacci_series(num):
    a = 0
    b = 1
    print("Fibonacci series: ")
    for i in range(num):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
fibonacci_series(num)