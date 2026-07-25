arr = list(map(int, input("Enther array of integers seperated by space: ").split()))
def sort_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

result = sort_array(arr)
print("The sorted array is: "," ".join(map(str, result)))

