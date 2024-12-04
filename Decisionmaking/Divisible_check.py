number=int(input("Enter the Number:"))

if number%15==0:

    print("fizzbuzz")

elif number%5==0:

    print("buzz")

elif number%3==0:

    print("Fizz")

else:

    print("Invalid Number")