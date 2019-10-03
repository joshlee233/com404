cover_type = input("Is the book cover hard or soft?: ")
binding = input("Is the book perfect bound? (yes/no): ")

#if (cover_type == "soft" and binding == "yes"):
#    print("Soft cover, perfect bound books are very popular!")
#elif (cover_type == "soft" and binding == "no"):
#    print("Soft covers with coils or stitches are great for short books")
#else:
#    print("Books with hard covers can be more expensive!")

if (cover_type == "soft" and binding == "yes"):
    print("Soft cover, perfect bound books are very popular!")
    if (cover_type == "soft" and binding == "no"):
        print("Soft covers with coils or stitches are great for short books")
        if (cover_type == "hard"):
            print("Books with hard covers can be more expensive!")
else:
    print("Oh dear, not a good book choice!")