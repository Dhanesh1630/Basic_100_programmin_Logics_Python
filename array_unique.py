arr = list(map(int, input("Enter Array of lements seperated by space: ").split()))
distinct = []
for i in arr:
    if i not in distinct:
        distinct.append(i)
print("The unique elements in the array are: ", " ".join(map(str, distinct)))
print("The nunber of unique elements are: ",len(distinct))
