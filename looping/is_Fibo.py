number=int(input("Enter the number:"))

previous=0

current=1

is_fib=False

for i in range(1,number+1):

    next=previous+current

    previous=current

    current=next

    if next==number:

        is_fib=True

        break

print(is_fib)