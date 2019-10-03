first = int(input("Please enter the first whole number: "))
second = int(input("Please enter the second whole number: "))
third = int(input("Please enter the third whole number: "))

even = 0
odd = 0

if (first % 2 == 0):
    even = even + 1
else:
    odd = odd + 1

if (second % 2 == 0):
    even = even + 1
else:
    odd = odd + 1

if (third % 2 == 0):
    even = even + 1
else:
    odd = odd + 1


print("There was " + str(even) + " even and " + str(odd) + " odd")