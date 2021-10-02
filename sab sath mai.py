elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c=0
i=0
c1=0
sum=0
sum1=0
count=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        # print(elements[i],"it is even")
        count=count+elements[i]
        c=c+1
    else:
        sum1=sum1+elements[i]   
        c1=c1+1
        # print(elements[i],"it is odd")  
    i=i+1
avreg1=sum/4
avreg=sum/5
print("even number,count:",c,"  ","sum of even:",sum,"   ","avrg odd:",avreg)
print("odd number.count:",c1,   "","sum of odd:",sum1,"    ","avreg even:",avreg1)

