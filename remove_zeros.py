#*Today's Question*:Move all zeros to the end of the list without changing the order of other elements.
#Input lis = [0, 5, 0, 8, 3, 0, 7]
#Output lis [5, 8, 3, 7, 0, 0, 0]
nums=[0,5,0,8,3,0,7]
for i in range(len(nums)):
    if nums[i]==0:
     nums.pop(i)
     nums.append(0)
print(nums)     