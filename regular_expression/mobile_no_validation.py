from re import fullmatch

user_input=input("Enter the mobile number:")

pattern="(91)?[0-9]{10}"

# * => zero or any number of times
# ? => optional
# + => need atleast once

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("Valid")

