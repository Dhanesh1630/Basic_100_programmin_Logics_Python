num = int(input("Enter the number of rows for Floyd's Triangle: "))
n = 1
for i in range(1, num + 1):
    for j in range(i):
        print(n, end=" ")
        n += 1
    print()    