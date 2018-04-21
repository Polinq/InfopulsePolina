def is_year_leap(a):
    '''The function works with one argument (num) and shows if the year is leap. If the year is leap it shows "True", if the year is not leap it shows "False"'''
    if ((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)):
        print('True')
    else:
        print('False')

is_year_leap(4)
