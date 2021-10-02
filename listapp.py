# a=[1,2,3,4,5,6]
# b=[]
# b.append(a)
# print(b)

# # n=[[1,2,3,4,],[5,6,7,8,]]
# # i=0
# # while i<len(n):
# #     j=0
# #     while j<len(n[i]):
# #         print(n[i][j])
# #         j=j+1
# #     i=i+1

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
a=numbers[i]

while i<len(numbers):
    if numbers[i]>a:
        a=numbers[i]
        print(a)
    i=i+1