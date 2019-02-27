# 1 number to check wheter even or odd
num = int(input("Enter the input number to check whether it is odd or even:"))
if num % 2 == 0:
    print("Input given number is even")
else:
    print("Input given is odd")

# 2 Get two input number and

num1 = int(input("Enter the first number to check it is divisible by 4:"))
num2 = int(input("Enter the second number to check it is odd or even number:"))

if num1%4 == 0:
    print("Given number is divisible by 4")
elif num1%2 == 0:
    print("Given number is even")
else:
    print("Given number is odd")

if num1%num2 == 0:
    print("Input numbers are divisible so it is even")
else:
    print("Input numbers are not divisible it is odd")




from datetime import datetime
start_time = datetime.now()
a='Premchand'
# print(a[::-1])
ix=len(a)
prt_val =''
while ix:
    ix -=1
    prt_val += a[ix]
print (prt_val)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# min(timeit.repeat(lambda: reverse_string_readable_answer(a_string)))



# Read in 5 book titles and values. After each title and value is read in display the values and produce a
# running total of the cost. Input the data in variables and then display the results. For example:

Running_Total = 0
num = int(input('Size of elements : '))
Book_Title = []
Book_cost = []
Running_Total_sum = []
for i in range(num):
    Book_Title.append(input("Enter Book Title: "))
    Book_cost.append(float(input("Enter the book cost: ")))

cnt = 0
print(f"{'Book Title':<30s} {'Cost':14s} {'Running Total':>10s}")
while cnt <= (num-1):
    Running_Total += Book_cost[cnt]
    Running_Total_sum.append(Running_Total)
    print(f"{Book_Title[cnt]:<30s} {Book_cost[cnt]:f} {Running_Total_sum[cnt]:>10.4f}")
    cnt += 1

print(Book_Title)
print(Book_cost)
print(len(Book_Title))
print(len(Book_cost))



