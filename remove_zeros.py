#*Today's Question*:Move all zeros to the end of the list without changing the order of other elements.
#Input lis = [0, 5, 0, 8, 3, 0, 7]
#Output lis [5, 8, 3, 7, 0, 0, 0]
nums=[0,5,0,8,3,0,7]
count=0
lis=[]
for i in range(len(nums)):
    if nums[i]==0:
        count+=1
    else:
        lis.append(nums[i])
for j in range(count):
    lis.append(0)
print(lis)            
            
           