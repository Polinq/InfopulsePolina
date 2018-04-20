phrase = input("Type a phrase: ")
if len(phrase) > 10:
        print(phrase[3], phrase[-1], phrase[:5], phrase[:-2], phrase[::2], phrase[1::2], phrase[::-1], phrase[::-2], phrase[1::-1], phrase[::], sep='\n')
if len(phrase) < 10:
        print("Too short phrase")