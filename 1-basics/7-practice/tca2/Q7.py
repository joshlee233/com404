word = input("Please input a word:\n")

def what_to_do(word):

    print("""1) Under - display the word with a line under it.
    2) Over - display the word with a line over it.
    3) Both - display the word in an underline and overline.
    4) Grid - display the word in a grid that is n x n in size.""")
    choice = input("What would you like to do with this word?\n")

    if choice == "1":
       print(under(word))
    else:
        print("")

def under(word):
    count = 0
    for i in word:
        count = len(word)
    print(word)
    print("*" * count)



what_to_do(word)