from math import sqrt
def distance(x1, y1, x2, y2):
    '''The function counts the distance between two '''
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Enter 4 coordinates to count the distance: ")
print("X1 = ")
x1 = float(input())
print("X2 = ")
x2 = float(input())
print("Y1 = ")
y1 = float(input())
print("Y2 = ")
y2 = float(input())
print(distance(x1, x2, y1, y2))

