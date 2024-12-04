def product_except_self(nums):
    
    n = len(nums)
    
    answer = [1] * n

    prefix = 1
    
    for i in range(n):
        
        answer[i] = prefix
        
        prefix *= nums[i]

    
    suffix = 1
    
    for i in range(n - 1, -1, -1):
        
        answer[i] *= suffix
        
        suffix *= nums[i]

    return answer

nums1 = [1, 2, 3, 4]

nums2 = [-1, 1, 0, -3, 3]

print(product_except_self(nums1)) # Output: [24, 12, 8, 6]
   
print(product_except_self(nums2))  # Output: [0, 0, 9, 0, 0]