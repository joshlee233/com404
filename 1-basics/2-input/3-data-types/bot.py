#Code to gather information about a person and then return it along with their bmi calculation
name = input("What is your name? : ")
age = int(input("How old are you? (years) : "))
height = float(input("How tall are you? (meters) : "))
weight = int(input("What is your weight? (Kilograms) : "))
bmi = weight / (height * 2)
print(name + " you are " + str(age) + " years old and your bmi is " + str(round(bmi, 2)) )