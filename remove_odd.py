nums=[0,1,1,3,3,4,5,6,7]
lis={}
for i in nums:
    if i not in lis:
       lis[i]=1
    elif i in lis:
        lis[i]+=1
for i in lis:
    if lis[i]%2!=0:
        while i in nums:
            nums.remove(i)
print(nums)              
                
  
           
        
    
            
         
        
        

