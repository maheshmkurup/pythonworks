user_input=input("Enter the bracket pairs:")

symbol_dictionary={
    
    "{":"}",

    "(":")",

    "[":"]",

    "<":">"

}

symbol_stack=[]

top=-1

is_valid=True

for symbol in user_input:
    
    if symbol in symbol_dictionary: #symbol is an opening

      
        
        top=top+1

        symbol_stack.append(symbol) #pushing or inserting the symbol to stack

    elif top==-1:
        
        is_valid=False

    elif symbol==symbol_dictionary.get(symbol_stack[top]):  #check symbol is valid closing
        
        top=top-1

        symbol_stack.pop()

    else:
        
        is_valid=False

if len(symbol_stack)==0 and is_valid==True:
    
    print("valid")

else:
    
    print("invalid")








    
     
    

    


    



     



   















