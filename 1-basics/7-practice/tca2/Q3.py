number_of_zones = int(input("How many zones must I cross?\n"))
print("Crossing zones...")

count = number_of_zones

while (count > 0):

    print("... Crossed zone ", str(count))
    count = count - 1

print("Crossed all zones. Jumanji!")