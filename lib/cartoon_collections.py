def roll_call_dwarves(names):
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")

def summon_captain_planet(planteers):
    planteers = [planteer.capitalize() + "!" for planteer in planteers]
    return planteers

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(foods):
    cheese = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheese:
            return food
        
    return None
    
