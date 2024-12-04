#pancard number

#3 random alphabets uppercase'
#4th place alphabet PCAFHT
#1 alphabet
#4 digits
#1 alphabet

from re import fullmatch

pan_card_number=input("Enter the pancard number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pan_card_number)

if matcher==None:

    print("Invalid")

else:

    print("Valid")