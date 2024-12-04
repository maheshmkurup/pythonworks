arr=[100,200,300,400,500,600,700,800]

left=1

right=len(arr)-1

if right%2==0:

    right=right-1

while(left<right):

    arr[left],arr[right]=arr[right],arr[left]

    left=left+2

    right=right-2

print(arr)
 




