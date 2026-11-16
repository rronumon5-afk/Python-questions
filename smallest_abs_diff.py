#Today's Question: Find two numbers that have the smallest absolute difference.
#inp: [4,9,6,1]
#out: [4,6]

num=[4,9,6,1]
output=abs(num[0]-num[1])
for i in range(len(num)):
    for j in range(i+1,len(num)):
        a=abs(num[i]-num[j])
        if output>a:
            output=a
            result=[num[i],num[j]]
print(result)            
                
        
        
        
        

    