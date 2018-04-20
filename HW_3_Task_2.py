p = input("Введите фразу: ")
l = len(p)//2+len(p)%2
a = p[l:]
b = p[:l]
print(a+b)