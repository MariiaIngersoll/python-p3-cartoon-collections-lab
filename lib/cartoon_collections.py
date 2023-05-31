
def roll_call_dwarves(dwarvs):
    for idx, dwarv in enumerate(dwarvs, start=1):
        print(f"{idx}. {dwarv}")

def summon_captain_planet(planeteer_calls):
    newPlant = []
    for n in planeteer_calls:
        newValue = n.capitalize() + "!"
        newPlant.append(newValue)
    return newPlant

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(string):
    cheeses = ["cheddar", "gouda", "camembert"]
    for str in string:
        if str in cheeses:
            return str
    return None
