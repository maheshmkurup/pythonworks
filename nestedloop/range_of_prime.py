start=int(input("Enter start:"))

stop=int(input("Enter the limit:"))

for num in range(start,stop+1):

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False

            break

    if is_prime==True:

        print(num)

        