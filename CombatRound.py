import random as r
from CoreRules import InflictWounds
from CoreRules import RollToHit
from CoreRules import RollToWound
from CoreRules import InflictCasualties
# Initialize and process combat between units.

def CombatRound(A, B): # A and B represents two sides.
    # Fighters are grouped into one list with all of the fighter.
    Fighters = []
    Fighters.extend(A)
    Fighters.extend(B)

    # Sort the fighter by the initiative, then print the combat order. 
    Combat_Order = sorted(Fighters, key=lambda x: x.I, reverse=True)
    print("Combat Begins!")
    print("Order of Battle:")
    for i,fighter in enumerate(Combat_Order):
        print(f"{i+1}. [{fighter}] at initiative {fighter.I}")
    input("Press enter to continue")
    print()

    # Attacking fighter selects a random enemy target to fight.
    for fighter in Combat_Order:
        if fighter in A:
            target = r.choice(B)
        else:
            target = r.choice(A)
        
        # Count the amount rolls that needs to be made.
        for weapon in fighter.weapon_list:
            rolls_count = fighter.curcount * weapon.A
            hit_rolls = RollToHit(rolls_count, fighter, weapon, target)
            wound_rolls = RollToWound(fighter,target,weapon,hit_rolls)

            damage = InflictWounds(fighter, weapon, target, len(wound_rolls))
            target = InflictCasualties(target, damage)
    
    for fighter in Combat_Order:
        for ability in fighter.abilities_list:
            if ability.type == "CombatEnd":
                if fighter in A:
                    ability.CombatEnd(fighter, A, B)
                else:
                    ability.CombatEnd(fighter, B, A)
                input("Press enter to continue")
                print()
            
        


                
            

            
            
        