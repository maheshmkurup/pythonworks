previous=0

current=1

next=0

for row in range(1,8):

    for col in range(1,row+1):

        print(row,end="\t")

        next=previous+current
        
        previous=current

        current=next

    print()

    