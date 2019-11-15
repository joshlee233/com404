def options(option):
    print("""
    1) Under - display the word with a line under it.
    2) Over - display the word with a line over it.
    3) Both - display the word in an underline and overline.
    4) Grid - display the word in a grid that is n x n in size.
    """)
    option = int(input("Please input the option you would like to select:\n"))

    if option == "1":
        return under()
    else:
        print("")



def under():
    print("hello")

return options()