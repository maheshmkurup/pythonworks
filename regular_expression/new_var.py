#starting with an alphabet from p-t
#in second place must be a number that is divisible by 3
#followed by any alphabets,numbers,@

from re import fullmatch

user_input=input("Enter the variable name:")

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("Valid")
    