def type_of_triangle(a, b, c):
    ''' Shows the type of triangle.'''

    if(a == b == c):
        print('Equilateral triangle')
    if(a + c < b or a + b < c or b + c < a):
        print('Not a triangle')
    else:
        print('Isosceles triangle')

# пример использования функции:
type_of_triangle(9, -10, 0)

