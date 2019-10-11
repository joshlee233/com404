bars_to_be_charged = int(input("How many bars should be charged? "))

number_charged = 0

while (number_charged < bars_to_be_charged):
    number_charged = number_charged + 1
    print("Charging: ", number_charged * "█")
print("The battery is fully charged.")