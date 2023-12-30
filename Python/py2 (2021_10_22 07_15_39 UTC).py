import time
x1 = bool()
v2 = 0
def a():
    v1 = int(input('What is 1+1?\n'))
    if v1 != 2:
        x1 == False
        while x1 == False:
            v2 = str(input('Wanna try again?\n'))
            if v2 == 'yes' or 'y': # need to rerun a()
                a()
            if v2 == 'no' or 'n':
                x1 == True #need to break x1 while loop if v2 != 'yes' not fixed yet
                exit(print('Okie!'))

    else:
        v1 = 2
        x1 == True
        print('Yee')
        time.sleep(1.5)
        exit(print('peace!'))
a()
        