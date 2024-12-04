number=int(input("Enter a number:"))

is_prime=True

for i in range(2,number):     #exclude 1 and number

    if number%i==0:

        is_prime=False

        break

print(is_prime)