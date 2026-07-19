while True:
    print("\n===== Number System Conversion =====")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Octal")
    print("4. Octal to Decimal")
    print("5. Decimal to Hexadecimal")
    print("6. Hexadecimal to Decimal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a decimal number: "))
        print("Binary =", bin(num)[2:])

    elif choice == 2:
        binary = input("Enter a binary number: ")
        print("Decimal =", int(binary, 2))

    elif choice == 3:
        num = int(input("Enter a decimal number: "))
        print("Octal =", oct(num)[2:])

    elif choice == 4:
        octal = input("Enter an octal number: ")
        print("Decimal =", int(octal, 8))

    elif choice == 5:
        num = int(input("Enter a decimal number: "))
        print("Hexadecimal =", hex(num)[2:].upper())

    elif choice == 6:
        hexa = input("Enter a hexadecimal number: ")
        print("Decimal =", int(hexa, 16))

    elif choice == 7:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please enter a number between 1 and 7.")