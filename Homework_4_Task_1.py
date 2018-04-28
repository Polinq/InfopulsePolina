def songLaLaLa(str_quantity = 3, la_quantity = 3, end_symbol = 0):

    c = " "
    if end_symbol is 0:
        c = "."
    if end_symbol is 1:
        c = "!"

    a = "la"

    i = 0
    j = 1
    while i < str_quantity:
        while j < la_quantity:
            a = a + '-la'
            j = j + 1
        if i == (str_quantity - 1):
            print(a + c)
        else:
            print(a)
        i = i + 1

songLaLaLa()

