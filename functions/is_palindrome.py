def is_palindrome_number(num):

    r=0

    temp=num

    while(temp>0):

        r=r*10+(temp%10)

        temp=temp//10

    if r==num:

        print(f"{num} is palindrome number")

    else:

        print(f"{num} is not a palindrome number")

is_palindrome_number(121)
    