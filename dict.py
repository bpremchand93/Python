campus ={}
contacts = {"prem":98909090211, "ram":901902901391, "Raj":92931111111111111111902931}
contacts['tamil'] = 901293010920391029390
# print(contacts)
# print(contacts.values())

print(98909090211 in contacts)
print(len(contacts))
for k,v in contacts.items():
    print(f"key is {k} and value is {v}")

print(contacts.get('rama'))

eng_staff_contact = {'paul':19203100923}
all_staff=eng_staff_contact
eng_staff_contact['thomas'] = 120930100239
print (f'\n{all_staff} \n{eng_staff_contact}')
upd_staff = {'thomas':12312312312}
eng_staff_contact.update(upd_staff)
print(eng_staff_contact)

student_lnum = ('L00133422','L001334234','L001332223')
module_sub = ['maths','science']
merge = list(zip(student_lnum,module_sub))
print(merge)
grades = [90.2,99.3]
merge_upd = list(zip(student_lnum,module_sub,grades))
print(merge_upd)

import random as rd
a=['Joe', 'John', 'Jane', 'Mick', 'Mary', 'Ann', 'Rick', 'John', 'Aine','Brenda']
b=['Jack', 'Mary', 'Phil', 'John', 'Pat', 'Joe', 'Luke', 'Bill', 'Ben', 'Nathan']
c=[]
d=[]
for i in range(len(a)):
    e=rd.randint(1,20)
    c.append(e)
for i in range(len(b)):
    e=rd.randint(1,20)
    d.append(e)

dict_a = dict(zip(a,c))
dict_b = dict(zip(b,d))
inters_itm = dict(dict_a.items() & dict_b.items())
diff_itm = dict(dict_a.items() | dict_b.items())
not_itm = dict(dict_a.items() ^ dict_b.items())
print(dict_a)
print(dict_b)
print(f'Key value pair intersect ---> {inters_itm} ')
print(f'Key value pair difference ---> {diff_itm} ')
print(f'Key value pair not present ---> {not_itm} ')
