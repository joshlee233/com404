health = 100
print("Your health is 100%. Escape is in progress...")

count = 0

while (count < 5):
    count = count + 1
    who_is_that = input("...Oh dear, who is that?")
    if who_is_that == "Slimer's Bot":
        print("Time to jam out of here!")
        health = health - 20
    elif who_is_that == "Hacker":
        print("Yay! Better follow this one!")
        health = health + 20
    else:
        print("Phew, just another emoji")

print("Escaped! Health is", str(health))

