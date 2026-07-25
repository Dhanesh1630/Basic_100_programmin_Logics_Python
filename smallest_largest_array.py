arr = list(map(int,input("Enter the elements of the array seperated by space: ").split()))
def smallest_largest_array(arr):
    smallest = arr[0]
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
        elif arr[i] > largest:
            largest = arr[i]
    return smallest , largest
smallest , largest = smallest_largest_array(arr)
print(f"The smallest element in the array is: {smallest}")
print(f"The largest element in the array is: {largest}")
