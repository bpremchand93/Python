import os
Mydir = os.chdir('C:\\Users\\PremChand\\Desktop')

def read_ssh_file():
    lines=open("sshd_logon_attempt.txt").readlines()
    failed_count=0
    illegal_user_count=0
    error_count=0
    count=0

    for line in lines:
        comments=line[36:]
        meta=line[0:35]
        print("Comments {0}".format(comments[0:40]))
        if(comments[0] == 'F'):
            failed_count += 1
        elif(comments[0] == 'I'):
            illegal_user_count += 1
        else:
            error_count += 1
        # count+=1
    print("There were {0} failed login attempts".format(failed_count))
    print("There were {0} Illegal login attempts".format(illegal_user_count))
    print("There were {0} Errors".format(error_count))

read_ssh_file()





