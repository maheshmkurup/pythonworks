#validate gmailid

#lowercase
#starts with an alphabet
#numbers optional
#@gmail.com
#before at 64 characters


from re import fullmatch

email_id=input("Enter the email id:")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

matcher=fullmatch(pattern,email_id)

if matcher==None:

    print("Invalid")

else:

    print("valid")

 
