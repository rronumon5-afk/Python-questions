nums=[10,8,9,7,7,10,1,1]#output=4
count=[]
for i in range(len(nums)):
    if nums[i] in nums[i+1:]:
        count.append(nums[i])
        
count=set(count)
print(len(count))        