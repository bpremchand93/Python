
# 3 prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in a:
    if i <= 5:
        b.append(i)
    else:
        pass

print (b)

print("\t"*2+"Title")
print("Hello")
print("Hello World")
a=5
b=12.3456789
c=a+b
d="A number "+str(b)
e=a+ \
 b+ \
 c
f=2
g=a/f
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


a= '^'*50
print (a)
b='<'+' '*48+'>'
print (b)
print (b)
print (b)
# print("<{:^48s}>".format('Title')
print(f"<{'Title':^48s}>")
print (b)
print (b)
print(f"<{' A Option a':<48s}>")
print(f"<{' B Option b':<48s}>")
print(f"<{' C Option c':<48s}>")
print (b)
print (b)
d= 'V'*50
print (d)


print (f'{6 + 8 / 2-1}')
print (f'{1 + 1 - 1 + 2 / 2}')
print (f'{1.1 + 5 / 2}')
print (f'{9.2 / 3}')
print (f'{9.2 % 3}')
print (f'{1 * 2 + 3 * 5 % 4}')
print (f'{1 + 8 % 3 * 2- 9}')
print (f'{6 + ( 24 % (16- 11))}')



# List:

empty_list = []
empty_list.append(10) #using an index won’t work until the items are added.
ages = [19, 21, 20]
student1_details = [20, "Michael Brennan", 77.5]
student2_details = [33, "Mairead Gallagher", 65]
class_of_students = [student1_details, student2_details, "module title", [2, 3, 4] ]

print(empty_list)
print(ages)
print(student1_details)
print(student2_details)
print(class_of_students)

empty_list =[]
empty_list.append(10)
ages=[19,21,20]
student1_details = [20, "Michael Brennan", 77.5]
student2_details = [33, "Mairead Gallagher", 65]
class_of_students = [student1_details, student2_details, "module title", [2, 3, 4] ]
print('{0}'.format(ages[1]))
print('{0} \t\t{1} \t{2}'.format(ages[1],student1_details[1],student2_details[2]))
print('\n{}'.format(class_of_students))
print('{}'.format(class_of_students[0][1]))
print('{}'.format(class_of_students[3][2]))
ages[1] = 33
group_of_students = class_of_students[0:2]
print(group_of_students)
print("1st student, 2nd datum is: {0}".format(group_of_students[0][1]))
second_group_of_students=student1_details+student2_details #joining two lists
third_group_of_students=[] # create an empty list
third_group_of_students+=second_group_of_students
print(second_group_of_students)
print(third_group_of_students)
print("Is Michael in list? {}".format(("Michael" in group_of_students[0][1])))
print("Is Michael in list? {}".format((group_of_students[0] in group_of_students[0])))


books=[]
num=int(input('Enter the number of element:'))
for i in range(num):
    books.append(input(f"Enter the book title {i}: "))

for i in range(len(books)):
    print('{0} has the value of {1}'.format(i,books[i]))



grades=[1,2,3]
nu_grades=[grades]*2 #note the square brackets around the list name
print("{}".format(nu_grades))
nu_grades[0][1]=6
print("Repeated list after change {}".format(nu_grades))

grades=[1,2,3,4,5,6,7,7,8,9,0,10231,12,3,4]
my_range = list(range(0,5))
print (my_range)
stu_grade = [['L12345',45,61],['L54321',40,80]]
print("Lnum : {}".format(stu_grade[0][0]))
print("Grade: {}".format(stu_grade[0][1]))

print(len(grades))
print(grades.sort())
print(grades.pop(['6']))
print(grades.clear())
print(grades.reverse())
print(grades)
print(grades.remove(3))
print(grades.count(2))
print(grades.pop(-1))
print(grades)


student1_details = [20, "Michael Brennan", 77.5]
student2_details = [33, "Mairead Gallagher", 65]
student3_details = student2_details
student3_details [0] = 34
print(student2_details,id(student2_details))
print(student3_details,id(student3_details))

import copy
student1_details = [20, "Michael Brennan", 77.5]
student2_details = [33, "Mairead Gallagher", 65]
student3_details = copy.deepcopy(student2_details)
student2_details[0] = 35
print(f"student2_details --> {id(student2_details)},{student2_details}")
print(f"student3_details --> {id(student3_details)},{student3_details}")



names=["ab","cd","aa", "db", "cd"]
b=set(names) #this will remove the repeating items in the new collection
print(b) # {'db', 'aa', 'cd', 'ab}

empty_tuple = ()
grades = (40,50,60)
student_python_exam = ("L00144391","prem",78.9)
student_python_exam1 = ("L00144392","premc",99.9)
python_class_of_student = (student_python_exam,student_python_exam1,'python',[10,11,12])
grades[1]=30
print(python_class_of_student)
grade_tuple_chg = list(grades)
grade_tuple_chg[0]=49
grade_tuple_chg = 50
print(grade_tuple_chg)
