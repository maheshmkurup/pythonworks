from re import fullmatch

driving_licence_no=input("Enter the driving licence number:")

pattern="[A-Z][0-9]{2} [0-9]{11}"

matcher=fullmatch(pattern,driving_licence_no)

if matcher==None:

    print("Invalid")

else:

    print("Valid")
    