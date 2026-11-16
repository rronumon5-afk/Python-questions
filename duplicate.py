nums=[1,2,2,2,3,5,6,7,9]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            print(nums[i])
            break
            