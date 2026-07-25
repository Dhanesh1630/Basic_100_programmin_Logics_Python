str = input("Enter a string: ")
list1 = list(str)
def sorted_string(str):
    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if list1[j] > list1[j+1]:
                list1[j] , list1[j+1] = list1[j+1] , list1[j]

    result =""
    for ch in list1:
       result += ch
    return result

print("The sorted string is : ", sorted_string(str))       
    
                