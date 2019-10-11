cables_to_avoid = int(input("How many cables should I avoid? "))

cables_avoided = 0

while (cables_avoided < cables_to_avoid):
    cables_avoided = cables_avoided + 1
    print("Avoiding... ...Done! ", cables_avoided, " Live cables avoided!")

print("All live cables have been avoided.")