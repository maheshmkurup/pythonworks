def review(rating):

    assert rating>0,"Too low"  #==> if condition become false (-1,-2 etc) print too low

    assert rating in range(1,11),"Too high"  #==> if condition become false if (11,12,etc) then print too high

    print("rated")

try:

 review(13)

except Exception as e:
   
   print(e)

       