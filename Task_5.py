a = 4000
b = 1890
c = 18
if a > b:
    a, b = b,a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)
