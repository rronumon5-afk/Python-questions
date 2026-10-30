num=[5,8,3,9,2,10]
largest=0
second_largest=0
for i in num:
    if i>largest:
        largest=i
print(largest)        


for i in num:
    if i<largest and i>second_largest:
        second_largest=i
print(second_largest)        
 
        