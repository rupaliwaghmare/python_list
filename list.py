# list=[]
# i=0
# while i<10:
#     list.append(i)
#     i=i+1
# print(list)


# a=[1,2,3,4,5,6]
# b=[]
# b.append(a)
# print(b)

n=[[1,2,3,4,],[5,6,7,8,]]
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        print(n[i][j])
        j=j+1
    i=i+1