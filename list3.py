# Code likho jo iss list mein se maximum dhund kar ke print kare.

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
a=numbers[i]

while i<len(numbers):
    if numbers[i]>a:
        a=numbers[i]
        print(a)
    i=i+1