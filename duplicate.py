n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
k=[]
i=0
while i<len(n):
    j=n[i]
    if j not in k:
         k.append(j)
    i=i+1
print(k)