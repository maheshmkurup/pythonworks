number=int(input("Enter the number:"))

real=number

digit_count=len(str(number))

total=0

while(number!=0):

    digit=number%10

    exponent=digit**digit_count

    total=total+exponent

    number=number//10


print(total)


if total==real:

    print(f"{total} is an armstrong number")

else:

    print(f"{total} is not an armstrong number")