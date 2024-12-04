arr=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
     ]

#print maximum of list objects

list_objects=[item for item in arr if isinstance(item,list)]

print(max(list_objects,key=len)) #==> taking the largest items using len key