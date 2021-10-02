# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# print len(students)
# print len(marks)
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']

marks = [10, 20, 56, 45, 36, 20]
list3=[]
i=0
while i<len(students):
    list3.append (str(students[i])+ str(marks[i]))
    i=i+1
print(list3)