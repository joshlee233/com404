max_numbers_to_add = int(input("How many numbers Should I sumup: "))

numbers_added_so_far = 0
user_input = 0
answer = 0


while (numbers_added_so_far < max_numbers_to_add):
    numbers_added_so_far = numbers_added_so_far + 1
    user_input = int(input("Please enter number " + str(numbers_added_so_far) + " of " + str(max_numbers_to_add) + ": " ))
    answer = answer + user_input
    print(answer)
    
print(answer)