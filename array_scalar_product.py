n = int(input("Enter size of array: "))
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
arr1.sort()
arr2.sort(reverse = True)
result = 0
for i in range(n):
    result += arr1[i] * arr2[i]
print("The scalar product is: ",result)
