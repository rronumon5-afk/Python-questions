#Ques: Find the first element that appears more than once.
a=[1,1,2,2,3,4,5]
for i in range(len(a)):
    if a[i] in a[i+1:]:
        print(a[i])
        break


 
