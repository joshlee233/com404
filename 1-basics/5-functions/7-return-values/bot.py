def sum_weights(weight1, weight2):
    total_weight = weight1 + weight2
    return total_weight

def calc_avg_weight(weight1, weight2):
    average_weight = sum_weights(weight1, weight2) / 2
    return average_weight

def run():
    weight1 = float(input("Please enter the weight for bot1: "))
    weight2 = float(input("Please enter the weight for bot2: "))
    which_sum = input("Please enter either sum or average: ")
    if (which_sum == "sum"):
        answer = sum_weights(weight1, weight2)
        print(answer)
    else:
        answer = calc_avg_weight(weight1, weight2)
        print(answer)

run()