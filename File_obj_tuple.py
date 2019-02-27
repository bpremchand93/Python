with open('text.txt','r') as rf:
    with open('text_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)


courses = ['science','maths','computer science','english']
courses_2 = ['Tamil','German','Tamil']
number = [1,3,3,4,5,6,7]

tuple_1 = ('science','maths','computer science','english')
tuple_2 = ('Tamil','German','Tamil')
number_tup = (1,3,3,4,5,6,7)

number_tup[0] = 5
print(tuple_1.extend(tuple_2))
print(courses[0:3])
print(courses[:-1])

print(len(courses))
# print(courses[4])

courses.append(courses_2)
print(courses)

courses.insert(0,courses_2)
courses.extend(courses_2)

courses_merge = courses.append(courses_2)
print(courses.index('science'))
courses.sort(reverse=True)
number.sort(reverse=True)

sorted_courses = sorted(courses)
print(sorted_courses)

print('science' not in courses)
print(sum(number))

courses.extend(courses_2)
course_str = '-'.join(courses)

print(course_str)

