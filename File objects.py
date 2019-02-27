# File Objects

with open('text.txt','w') as f:
    # for line in f:
    #     print(line,end='')
    f.write("test")
    f.seek(2)
    f.write('tt')

    read_size = 10
    f_content = f.read(read_size)
    print(f_content,end='')

    f.seek(10)

    f_content = f.read(read_size)
    print(f_content,end='')


    print(f.tell())
    while len(f_content) > 0:
        print(f_content,end='*')
        f_content = f.read(read_size)
print(f.closed)
print(f.read())
f = open('text.txt','r')
print(f.close())
print(f.mode)


