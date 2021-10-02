elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
b=[]
c=[]
i=0
sum=0
s=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        b.append(elements[i])
        

    else:
        c.append(elements[i])
        s=s+elements[i]
    i=i+1
print(b,"even number sum =",sum)
print(c,"odd number sum =",s)