num = int(input("enter range: "))
def primes_in_range(num):
    print(f"prime numbers in range 1 to {num} are: ")
    for i in range(1, num+1):
        if i > 1:
            for j in range(2, int(i/2)+1):
                if(i%j) == 0:
                    break
            else:
                print(i , end=" ")
primes_in_range(num)                    
