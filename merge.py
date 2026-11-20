#merge to arrays in a single sorted array
a=list(map(int,input("enter list:").split()))
b=list(map(int,input("enter list:").split()))
for i in a:
    b.append(i)
    
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            b[j],b[i]=b[i],b[j]
print(b)            
                  
            
    
