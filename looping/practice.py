arr=[3,6,9,5,7,8]

search_element=int(input("Enter the number:"))

is_present=False

for i in range(0,len(arr)):

    if search_element==arr[i]:

        is_present=True

        break

print(is_present)
    