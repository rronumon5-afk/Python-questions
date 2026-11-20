result=["pass","fail","pass","fail"]
binary=[]

for i in range(len(result)):
    if result[i]=="pass":
        binary.append(1)
    else:
        binary.append(0)
print(binary)           