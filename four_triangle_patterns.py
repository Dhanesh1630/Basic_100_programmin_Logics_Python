rows = int(input("Enter the number of rows for Tiangle patterns: "))
# pattern 1
for i in range(1 , rows +1):
    for i in range ( 1 , i+1):
        print("*", end = " ")
    print()
print()

# pattern 2
for i in range( rows , 0 , -1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()
print()

# pattern 3
for i in range(rows):
    for j in range(i):
        print(" ", end = " ")
    for k in range(rows - i):
        print("*", end =" ")
    print()
print()

# pattern 4
for i in range(1,rows):
    for j in range(rows - i):
        print(" ",end = " ")
    for k in range(i):
        print("*", end = " ")
    print()                             