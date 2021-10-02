elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
b=[]
c=[]
i=0
sum=0
s=0
count=0
count1=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        b.append(elements[i])
        count=count+1
        

    else:
        c.append(elements[i])
        s=s+elements[i]
        
    # i=i+1
        count1=count1+1
    i=i+1
print(b,"even number",sum,count)
print(c,"odd number",s,count1)