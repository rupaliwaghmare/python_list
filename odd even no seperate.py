

L = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
b=[]
c=[]
i=0
sum=0
s=0
count=0
count1=0
while i<len(L):
    if L[i]%2==0:
        sum=sum+L[i]
        b.append(L[i])
        count=count+1
        

    else:
        c.append(L[i])
        s=s+L[i]
        
    # i=i+1
        count1=count1+1
    i=i+1
print(b,"even number",sum,count)
print(c,"odd number",s,count1)



