while True:
    try:
        rows1 = int(input("Enter a number: "))
        if rows1 > 1 and rows1 <= 100:
            for i in range(0, rows1):
                for j in range(0, rows1-i-1):
                    print(end=" ")
                for j in range(0, i+1):
                    print("*", end=" ")
                print()
            break
        else:
            print("Enter number greater than 1 and less than 100, so that my PC wont crash, Im poor")
            continue
    except ValueError:
        print("Please enter a whole number between 1 - 100 only")
