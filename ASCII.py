num = input("Enter a charatcter: ")     
def ascii_value(num):
    print(f"The ASCII value of {num} is: {ord(num)}")
if len(num) !=1:
    print("Please enter a single character")
else:
    ascii_value(num)    
   