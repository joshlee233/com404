def options():
    word = input("Please enter a word: ")
    option_select = int(input("""1) Display in a Box – display the word in an ascii art box
    2) Display Lower-case – display the word in lower-case e.g. hello
    3) Display Upper-case – display the word in upper-case e.g. HELLO
    4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
    5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.
    Please select an option: """))

    if (option_select == 1):
        ascii_box(word)
    elif (option_select == 2):
        lower_case(word)
    elif (option_select == 3):
        upper_case(word)
    elif (option_select == 4):
        reverse(word)
    elif (option_select == 5):
        repeat(word)
    else:
        print()


def ascii_box(word):
    print("*" * (len(word) + 10))
    print("* Hello", word, "*")
    print("*" * (len(word) + 10))

def lower_case(word):
    print(word.lower())

def upper_case(word):
    print(word.upper())

def reverse(word):
    reverse = ""
    for letter in word:
        reverse = letter + reverse
    print(reverse)

def repeat(word):
    number_of_times = int(input("How many times to display the word?: "))
    for number in range(number_of_times):
        if (number % 2 == 0):
            upper_case(word)
        else:
            lower_case(word)

options()