def variable():
    variable2 = input('What is 1+1?\n')
    if variable2 != '2':
        print('wuh?')
    else:
        print('Noice!')
    while variable2 != '2':
        variable3 = input('Do you want to try again?\n')
        if variable3 == 'yes' or 'y':
            variable()
        else:
            exit(print('Peace!'))
variable()