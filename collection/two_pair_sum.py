arr=[2,3,4,5]

sum=int(input("enter the sum:"))

for i in range(0,len(arr)-1):

    for j in range(i+1,len(arr)):

        curr_sum=arr[i]+arr[j]

        if sum==curr_sum:

            print(arr[i],arr[j])

            break
        
         





         



