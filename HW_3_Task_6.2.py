def is_a_triangle(a, b, c):
    ''' Shows if the triangle exsists or not. If it exsisrs, it will show "yes" and if it does not exsit it will show "no". (num, num, num) -> yes or (num, num, num) -> no.'''
    if (a + c < b or a + b < c or b + c < a):
        print('NO')
    else:
        print('YES')

# пример использования функции:
is_a_triangle(7, 9, 4)