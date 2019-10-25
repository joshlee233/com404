days_remaining = int(input("How many days remain until the next full moon?: "))
print("We must count the days...")

count = days_remaining

while (count > 0):
    print("The full moon is upon us in " + str(count) + " days.")
    count = count - 1

print("It's a full moon. The beast has been unleashed!")
print("May it have mercy on our souls.")