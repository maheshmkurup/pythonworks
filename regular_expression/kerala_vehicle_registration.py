#starting with KL
#2 digit
#alphabets minimum1 maximum2
#4 digit

from re import fullmatch

user_input=input("Enter the registration number:")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("valid")

    









