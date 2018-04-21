def while_a_word(a):
    '''The function asks the user to enter a word (a line with no spaces in the middle, and at the beginning and at the end, spaces can be). Until he enters it correctly, ask him to enter. The function returns the entered word'''
while True:
    print("Type a phrasse without spaces")
    phrase = input("Your message: ")
    phrase.strip()
    print(phrase)
    if ' ' in phrase:
        break 

