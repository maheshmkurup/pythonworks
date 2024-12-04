from re import fullmatch

passport_number=input("Enter the passport number:")

pattern="[A-Z][1-9][0-9]{6}"

matcher=fullmatch(pattern,passport_number)

if matcher==None:

    print("Invalid")

else:

    print("Valid")
    



