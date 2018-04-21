def while_a_number():
    '''The function asks the user to enter a number. Until he enters it correctly, ask him to enter. The function returns the entered number.'''
while True:
    print("Enter a number to stop")
    p = input("Please enter a number: ")
    print(p)
    if type(p) is int:
        break