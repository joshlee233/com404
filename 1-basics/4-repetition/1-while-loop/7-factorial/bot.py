number_to_factorise = int(input("Please enter a number to Factorise: "))

count = 0
answer = 1

while (count < number_to_factorise):
    count = count + 1
    answer = answer * count

print(answer)