
while True:
    try:
        a = int(input(" Enter 1 for Half Pyramid \n Enter 2 for Star Pyramid \n Enter 3 for Diamond Star \n Enter 4 for All Patterns \n Choose Your Pattern : "))

        if a == 1:
            while True:
                try:
                    n = int(input("\nSelect the size for your pattern: "))
                    if n > 1 and n <= 100:
                        for i in range(n, -1, -1):
                            for j in range(0, i + 1):
                                print("@", end=" ")
                            print()
                        break
                    else:
                        print("\nEnter number greater than 1 and less than 100, so that my PC wont crash, Im poor")
                        print("--------------------------------------Try again---------------------------------\n")
                        continue
                except ValueError:
                    print("\nPlease enter a whole number between 1 - 100 only")
                    print("------------------Try again---------------------\n")
    #-----------------------------------------------------------------------------------------------------------
        elif a == 2:
            while True:
                try:
                    rows1 = int(input("\nSelect the size for your pattern: "))
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
    #-----------------------------------------------------------------------------------------------------------
        elif a == 3:
            while True:
                try:
                    rows1 = int(input("\nSelect the size for your pattern: "))
                    if rows1 > 1 and rows1 <= 100:
                        for i in range(0, rows1):
                            print(' ' * (rows1 - i - 1) + '$ ' * (i + 1))
                        for j in range(rows1 - 1, 0, -1):
                            print(' ' * (rows1 - j) + '$ ' * j)
                        break
                    else:
                        print("\nEnter number greater than 1 and less than 100, so that my PC wont crash, Im poor")
                        print("--------------------------------------Try again---------------------------------\n")
                        continue
                except ValueError:
                    print("\nPlease enter a whole number between 1 - 100 only")
                    print("------------------Try again---------------------\n")
    #-----------------------------------------------------------------------------------------------------------
        elif a == 4:
            while True:
                try:
                    rows1 = int(input("\nSelect the size for your pattern: "))
                    if rows1 > 1 and rows1 <= 100:
                        for i in range(rows1, -1, -1):
                            for j in range(0, i + 1):
                                print("@", end=" ")
                            print()
                        for i in range(0, rows1):
                            for j in range(0, rows1 - i - 1):
                                print(end=" ")
                            for j in range(0, i + 1):
                                print("*", end=" ")
                            print()
                        for i in range(0, rows1):
                            print(' ' * (rows1 - i - 1) + '$ ' * (i + 1))
                        for j in range(rows1 - 1, 0, -1):
                            print(' ' * (rows1 - j) + '$ ' * j)
                        break
                    else:
                        print("\nEnter number greater than 1 and less than 100, so that my PC wont crash, Im poor")
                        print("--------------------------------------Try again---------------------------------\n")
                        continue
                except ValueError:
                    print("\nPlease enter a whole number between 1 - 100 only")
                    print("------------------Try again---------------------\n")
        else:
            print("\n!!Enter 1, 2, 3 or 4 only!!\n")
            continue
    except ValueError:
        print("\nPlease enter 1, 2, 3 or 4 only")
        print("----------Try again-----------\n")
    p = input("\nWanna try again? Yes or No? : ")
    if p == "Yes" or p == "yes":
        continue
    else:
        print("\nThanks, See you next time 😁")
        break
        
