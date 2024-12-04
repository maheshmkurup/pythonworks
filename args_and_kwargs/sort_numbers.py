def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)
    
    if kwargs.get("reverse")=="False":

        return sorted(args)
    
print(sort_numbers(10,20,30,40,reverse="True"))

print(sort_numbers(20,50,60,40,reverse="False"))



