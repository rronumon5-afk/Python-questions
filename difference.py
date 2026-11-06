#Find the difference between the largest and smallest elements.
#inp : [5,8,3,9,2,10]
#out : 8
num=[5,8,3,9,2,10]
maximum=0
for i in num:
    if i>maximum :
        maximum=i
print(maximum)        
minimum=maximum
for i in num:
    if i<maximum: 
        minimum=i
print(minimum)                

print("The difference:",maximum-minimum)
