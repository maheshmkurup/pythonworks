lst1=["apple","mango","onion","pottatto"]

lst2=[100,200]

result={}

for i in range(0,len(lst2)):

    lst_one_index_element=lst1[i]

    lst_two_index_element=lst2[i]

    result[lst_one_index_element]=lst_two_index_element

balance_elements=lst1[len(lst2):]

for index,element in enumerate(balance_elements):

    result[element]=index+1

print(result)

