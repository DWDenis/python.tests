   
def get_grade(score:int) -> str:
    if score >= 90:
        return "A"
    elif score > 79:
        return "B"
    elif score > 69:
        return "C"
    elif score > 59:
        return "D"
    return "F"



'''    
Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
Spaces and punctuation are counted as engraved units.
'''
def cost_of_project(engraving:str, solid_gold:bool):
    if solid_gold == True:
        cost = 100 + (10 * len(engraving))
        return cost
    else:
        cost = 50 + (7 * len(engraving))
    return cost



def get_water_bill(num_gallons:int) -> float:
    bill = 1000
    if num_gallons >= 30001:
        return (num_gallons/bill) * 10
    elif num_gallons > 22000:
        return (num_gallons/bill) * 7
    elif num_gallons > 8000:
        return (num_gallons/bill) * 6
    return (num_gallons/bill) * 5



def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = 100 + ((gb-15)*100)
    return bill



