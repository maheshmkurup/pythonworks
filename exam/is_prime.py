number=int(input("Enter the number:"))

is_prime="is prime number"

for i in range(2,number):

    if number%i==0:

        is_prime="is not a prime number"

print(is_prime)