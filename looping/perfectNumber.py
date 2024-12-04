num=int(input("Enter the number:"))

total=0

for i in range(1,num):

    if num%i==0:

        total=total+i       #num + sum of its divisors=perfect Number   (6,28,496,8128)

print("perfect Number" if total==num else "not perfect Number")