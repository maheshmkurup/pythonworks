from re import fullmatch

user_input=input("Enter the variable name:")

#rules for a variable

#1.)start with an alphabet (lowercase or uppercase)
#2.)any number of alphabets,digits,_

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input) #None

if matcher==None:

    print("Invalid")

else:

    print("Valid")



