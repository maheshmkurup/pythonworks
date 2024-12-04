for row in range(7,0,-1):

    for sp in range(7,row-7,-1):

        print(" ",end="")

    for col in range(1,row):

        print("* ",end="")

    print()