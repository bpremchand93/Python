import os
dir='C:\\Users\\PremChand\\Desktop'
mydir = os.chdir(dir)
read_file = open('text.txt','r+')

for line in read_file:
    print(line.rstrip)

read_file.write('Prem5, L00144391, M.scvv\n')
read_file.seek(20,0)
prt_read_file = read_file.read()
print('After Writing \n')
print(prt_read_file)
read_file.close()
line = line.split('\n')
print(f'{line} line in the file')


import os
a=os.path.abspath('C:/Users/PremChand/Desktop')
b= r'C:\Users\PremChand\Desktop'
# print(b.replace("\", "/",3))
print(a,b)



import random
import os
import math
import sys

for i in range(10):
    print(f'{i} byte is {random.randint(1,10)}')
    print(f'{i} byte is {random.randrange(1,10)}')
    print(f'{i} byte is {random.random()}')

for i in range(10):
    print(f'{i} byte is {random.uniform(10,15)}')


env_tup = tuple(os.environ)
print(env_tup)
for i in range(10):
    sys.stdout.write("{} ".format(env_tup[i]))


print('\n\nThe factorial of 4 is : {}'.format(math.factorial(5)))
print('\nPi value {}'.format(math.pi))


import platform as pl
print(pl.machine())
print(pl.node())
print(pl.processor())
print(pl.python_version())
print(pl.python_version())
print(pl.platform())
print(pl.system())
print(pl.system())
print(pl.release())
print(pl.version())

import sys
print(sys.platform)


values = [2,3,4,5,6,7]

def double(x):
  return x * 2

a=[]
for value in values:
  a.append(double(value))
print(a)

results = list(map(double, values))
print(results)


str = input("Enter your input: ")
print ("Received input is : ", str)

import os
for folder_name1, sub_folder, file_name in os.walk("E:\\Desktop\\ML dataset\\ML Assignment L00142823"):
  print("\n Folder {0} \n".format(folder_name1))

  for sub_folders in sub_folder:
      print("Folder Name: {0} is the sub folder of {1}".format(sub_folders,folder_name1))
  for file_names in file_name:
      print("{0} is a file inside {1}".format(file_names,folder_name1))


import zipfile, os
os.chdir(os.path.normpath("E://ziptest"))
newzip = zipfile.ZipFile('test.zip','a')
newzip.write('os_zip.txt')

print("{}".format(newzip.printdir()))
newzip.write(('os_zip1.txt'))
print("\n file in zip are: {0} \n")
newzip.extractall()
newzip.close()

