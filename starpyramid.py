while True:
    try:
        a = int(input("Enter 1 for Star Pyramid or Enter 2 for Upside Down Half Pyramid : "))


        if a == 2:
            while True:
                try:
                    n = int(input("\nSelect your number for the shape: "))
                    if n > 1 and n <= 100:
                        for i in range(n, -1, -1):
                            for j in range(0, i + 1):
                                print("*", end=" ")
                            print()
                        break
                    else:
                        print("\nEnter number greater than 1 and less than 100, so that my PC wont crash, Im poor")
                        print("--------------------------------------Try again---------------------------------\n")
                        continue
                except ValueError:
                    print("\nPlease enter a whole number between 1 - 100 only")
                    print("------------------Try again---------------------\n")
            break
    #-----------------------------------------------------------------------------------------------------------
        elif a == 1:
            while True:
                try:
                    rows1 = int(input("\nSelect your number for the shape: "))
                    if rows1 > 1 and rows1 <= 100:
                        for i in range(0, rows1):
                            for j in range(0, rows1 - i - 1):
                                print(end=" ")
                            for j in range(0, i + 1):
                                print("*", end=" ")
                            print()
                        break
                    else:
                        print("\nEnter number greater than 1 and less than 100, so that my PC wont crash, Im poor")
                        print("--------------------------------------Try again---------------------------------\n")
                        continue
                except ValueError:
                    print("\nPlease enter a whole number between 1 - 100 only")
                    print("------------------Try again---------------------\n")
            break
        else:
            print("\n!!Enter 1 or 2 only!!\n")
            continue
    except ValueError:
        print("\nPlease enter 1 or 2 only")
        print("--------Try again-------\n")
