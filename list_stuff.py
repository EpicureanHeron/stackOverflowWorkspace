a=[1,2,3,4,5,6]
b=[2,34,5,67,5,6]
c=[]
for i in range(len(a)):
    if a[i] == b[i]:
        c.append(0)
    else:
        c.append(1)
print(c)