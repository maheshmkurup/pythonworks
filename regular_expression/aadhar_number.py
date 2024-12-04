from re import fullmatch

aadhar_number=input("Enter the aadhar number:")

pattern="[1-9]{1}[0-9]{3} [0-9]{4} [0-9]{4}"

matcher=fullmatch(pattern,aadhar_number)

if matcher==None:

    print("Invalid")

else:

    print("Valid")