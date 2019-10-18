def display_ladder(steps):
    for step in range(steps):
        print("| |\n***")

def create_ladder(steps):
  print("How many steps remain?: ")
  steps = int(input())
  display_ladder(steps)

create_ladder(0)
