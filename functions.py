def hello_world():
    print("Hai How r u!!!")

# print(hello_world)
hello_world()
hello_world()
hello_world()
hello_world()


def hello_world(name,age=24):
    return(f'{name}, How r u!!, my age is {age}')

print(hello_world('Prem',25))


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

inform = ('rpporep','informaioein')
req = {'course_0':'maths', 'course_1':'business'}

# print(student_info('premchand','24','234',name='prem',age = '25'))
student_info(*inform,**req)




def is_leap_year(year):
    return (year%4==0 and ((year%400!=0) or (year%400==0)))

def days_in_month(year, month):
    if not ((month >= 0) and (month <=12)):
        return 'Input month is invalid'
    if (month==2) and is_leap_year(year):
        days_in_feb = 29
    else:
        days_in_feb = 28
        # return days_in_feb
    month_days= [0,31,days_in_feb,31,30,31,30,31,31,30,31,30,31]
    print (month_days[month], (sum(month_days)))
print(is_leap_year(2019))
print(days_in_month(2019,2))

