def review(rating):

    if rating<0:

        raise Exception("Too low")
    
    elif rating>10:

        raise Exception("Too High")
    
    

    
    else:

        print("Done")

try:

    review(12)

except Exception as e:

    print(e)

print("Hello")

print("Hai") 