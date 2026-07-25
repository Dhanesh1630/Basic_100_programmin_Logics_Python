num = list(map(int, input("Enter Array of integrs seperated by space: ").split()))
def reverse_array(num):
    start = 0
    end = len(num) -1
    while start < end:
        num[start], num[end] = num[end], num[start]
        start += 1
        end -= 1
    return num
print("The reversed array is: ", " ".join(map(str, reverse_array(num))))
    