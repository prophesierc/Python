import time
x1 = bool()
def a():
    v1 = int(input('What is 1+1?\n'))
    if v1 != 2:
        x1 == False
        while x1 == False:
            v2 = str(input('Wanna try again?\n'))
            if v2 == 'yes' or 'y': # need to rerun a()
                print('bleh')
    if v1 == 2:
        x1 == True
        while x1 == True:
            print('Yee')
            time.sleep(2.3)
            exit(print('peace!'))
a()                