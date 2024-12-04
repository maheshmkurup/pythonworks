def is_amstrong_number(num):

    real=num

    digit_count=len(str(num))

    total=0

    while(num!=0):

        digit=num%10

        exponent=digit**digit_count

        total=total+exponent

        num=num//10

    print(total)

    if total==real:

        print(f"{total} is an armstrong number")

    else:

        print(f"{total} is not an armstrong number")

is_amstrong_number(1634)