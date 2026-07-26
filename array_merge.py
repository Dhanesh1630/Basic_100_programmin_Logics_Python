arr1 = list(map(int , input("Enter first array of integers seperated by space: ").split()))
arr2 = list(map(int, input("Enter second array of integers sepearted by space: ").split()))
i , j = 0 , 0
merged = []
while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1
while i < len(arr1):
    merged.append(arr1[i])
    i += 1
while j < len(arr2):
    merged.append(arr2[j])
    j += 1
print("The merged array is: ", " ".join(map(str, merged)))                    