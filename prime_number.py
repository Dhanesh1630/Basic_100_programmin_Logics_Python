num = int(input("enter number:"))
def prime_number(num):
    if num > 1 :
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(f"{num} is not a prime number")
                break
        else :
            print(f"{num} is a prime number")
            
    else:
        print(f"{num} is not a prime number")
prime_number(num)
        
