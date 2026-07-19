while True :
    print("\n===== Rectangle Patterns =====")
    print("1. Solid Reactangle")
    print("2. Hallow Rectangle")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        for i in range(rows):
            for j in range(cols):
                print("*",end=" ")
            print()
    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of coulums: "))
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    print("*", end =" ")
                else:
                    print(" ", end =" ")
            print()
    elif choice == 3:
        print("Exiting program...")
        break
