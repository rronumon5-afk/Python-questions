nums=[10,7,4,8,9,4,7,7,10,1,7,1]#output=4
a={}
for i in nums:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
count=0
for i in a:
    if a[i]>1:
        count+=1
                
print(count)               
        
        
