#Prints the string
print("Please enter the activity to be preformed.")
#Stores the input in a variable
activity = input()

#Checks whether the string entered is equal to calculate, if true then it prints the next line
if (activity == "calculate"):
    print("Preforming calculations...")
#Anything else that is input brings up this message insted
else:
    print("Preforming activity...")
#prints the string
print("Activity completed!")