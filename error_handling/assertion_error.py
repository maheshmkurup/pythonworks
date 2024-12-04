def poll(age):

    assert age>18,"invalid age"  #==> if condition become false then print as invalid age

    print("voted")

try:

 poll(16)

except Exception as e:
   
   print(e)

    

