
courses   = {'science','maths','computer science','english'}
courses_2 = {'Tamil','German','Tamil','computer science'}
number = {1,3,3,4,5,6,7}

# print ('maths' in courses)

print(courses_2.intersection(courses))
print(courses_2.difference(courses))
print(courses_2.union(courses))
print(courses)
print(courses.add('test'))

empty = set()
empty_li = list()
empty_tu = tuple()


student ={'name':'Prem','age':25,'courses':['BI','Computer Science']}
print(student.items())
print(student.keys())
print(student.values())
# student.update{'name':'Premchand','age':25,'phone':89940376}
print(student.get('age','Not found'))
student['phone']=89940390
del student['age']
name = student.pop('name')
print(student)
print(name)
print(len(student))

for values in student.values():
     print(values)


my_list = [0,1,2,3,4,5,6,7,8,9]

print(my_list[::-1])


sample_url = 'http://coreyms.com'
print(sample_url[:-4])
print(sample_url[7:])
print(sample_url[7:-4])
print(sample_url[::-1])


language='Java'
if (len(language) is 4):
    print('Condition was true')
elif(language == 'Java'):
    print('Language is Java')
else:
    print("Condition was false")

user = 'Admin'
logged_in = False

# if user == 'Admin':
if not logged_in:
    print ('Enter into the site')
else:
    print ('Do not enter into the site')


a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
print (id(a))
print (id(b))
print (a is b)


condition = True

if condition:
    print('Enter into the condition')
else:
    print('Not enter into the condition')

num = [1,3,3,4,5]
letter = 'abc'
for i in num:
    if i == 3:
        print('3 found')
        break
    print (i)


for a in num,letter:
    print (a)


for i in range(10):
    print(i)

x=0
while True:
    print (x)
    x+=1
