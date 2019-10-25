def is_league_united(hero1, hero2):
    if (hero1 == "Superman" and hero2 == "Wonder Woman"):
        return True
    else:
        return False

def decide_plan(hero1, hero2):
    if (is_league_united(hero1, hero2) == True):
        return "Time to save the world"
    else:
        return "We must unite the league!"

def run():
    hero1 = input("Input first hero name:\n")
    hero2 = input("Input second hero name:\n")
    league_or_plan = input("Input either league or plan:\n")
    if (league_or_plan == "league"):
        print(is_league_united(hero1, hero2))
    elif (league_or_plan == "plan"):
        print(decide_plan(hero1, hero2))
    else:
        print("Invalid command. Please try again")

run()