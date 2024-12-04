number=int(input("Enter the number:"))

total=0

while(number!=0):   #145!=0                14!=0              1!=0

    digit=number%10    #145%10=5            14%10=4            1%10=1

    digit_square=digit**2  #5*5              #4*4               #1*1
 
    total=total+digit_square #total=0+5*5     total=25+4*4      total=41+181

    number=number//10      #145//10=14        #14//10=1        #1//10=0

print(total) 