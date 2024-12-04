for row in range(1,4):

    for sp in range(1,4-row):

        print(" ",end="")

    for col in range(1,row+1):

        print("* ",end="")

    print()

for row in range(4,0,-1):

    for sp in range(4,row-4,-1):

        print(" ",end="")

    for col in range(1,row):

        print("* ",end="")

    
    print()