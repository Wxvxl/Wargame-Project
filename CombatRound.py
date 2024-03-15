import random as r

# Initialize and process combat between units.
def CombatRound(A, B): # A and B represents two sides.
    # Fighters are grouped into one list with all of the fighter.
    Fighters = []
    Fighters.extend(A)
    Fighters.extend(B)

    # Sort the fighter by the initiative, then print the combat order. 
    Combat_Order = sorted(Fighters, key=lambda x: x.I, reverse=True)
    print("Combat Begins!")
    for i,fighter in enumerate(Combat_Order):
        print(f"{i+1}. {fighter} at initiative {fighter.I}")
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
            hit_rolls = []
            
            # start rolling to hit
            for i in range(rolls_count):
                hit_rolls.append(r.randint(1,6))
            
            # set the number you need to score a successful hit.
            # Compare the attacker's WS and the defender's WS.
            hitTarget = 4 # The default target needed to score a hit.
            if (fighter.WS + weapon.HM) > 2 * (target.WS + target.weapon_list[0].HM):
                hitTarget = 2 # if attacker WS is more than double of defender WS, hitting on 2+
            
            elif (fighter.WS + weapon.HM) > (target.WS + target.weapon_list[0].HM):
                hitTarget = 3 # if attacker WS is more than defender WS, hitting on 3+

            elif (target.WS + target.weapon_list[0].HM) * 2 > (fighter.WS + weapon.HM):
                hitTarget = 5 # if defender WS is more than double of attacker WS, hitting on 5+

            elif ((target.WS + target.weapon_list[0].HM) * 2) + 3 > (fighter.WS + weapon.HM):
                hitTarget = 6 # if defender WS is more than double that of the attacker + 3, then hit on 6+

            print(f"{fighter} attacking using {weapon} at {fighter.WS + weapon.HM}WS!")
            print(f"{target} defending using {target.weapon_list[0]} at {target.WS + target.weapon_list[0].HM}")
            print(f"Roll needed to hit: {hitTarget}+")
            
            # Remove all of the hit roll that does does not meet the hit criteria.
            hit_rolls = [roll for roll in hit_rolls if roll >= hitTarget] 
            print(f"Successful hit for {fighter} against {target}: {hit_rolls}")
            print()
        
            # rolling to wound, works the same way as rolling to hit except successful wound is dictated by Strength and Toughness.
            wound_rolls = []
            print(f"{fighter} rolling to wound against {target} using {weapon} with {weapon.S} strength against {target} with {target.T} toughness")
            hitTarget = 4 # Default value for wounding.

            if (weapon.S) >= 2 * (target.T):
                hitTarget = 2 # if Strength more than or equal to double of target Toughness wounding on 2+
            
            elif (weapon.S) > (target.T):
                hitTarget = 3 # if Strength higher than toughness, then wounding on 3+
            
            elif (weapon.S) < (target.T):
                hitTarget = 5 # If strength lower than toughness, wounding on 5+
            
            elif (weapon.S) <= (target.T) * 2:
                hitTarget = 6 # If strength lower than double of toughness, wounding on 6+!
            
            # Rolls the wound roll, works the same way as hit roll.
            print(f"roll needed to successfully wound: {hitTarget}+")
            for i in range(len(hit_rolls)):
                wound_rolls.append(r.randint(1,6))
            wound_rolls = [roll for roll in wound_rolls if roll >= hitTarget]
            print(f"Successful wounds for {fighter} against {target}: {wound_rolls}")
            print()

            # Units now make their saving throws.
            print(f"{target} rolling for saving throws")
            print(f"{target} has a {target.Sv}+ save, reduced by {fighter}'s {weapon} with AP{weapon.AP}")

            # Modifies the save by the weapon AP value.
            SvTarget = target.Sv - weapon.AP
            
            # Roll the saving throws and remove all of the saved wounds.
            print(f"{target} needs {SvTarget}+ to successfully save a wound!")
            Sv_rolls = []
            for i in range(len(wound_rolls)):
                Sv_rolls.append(r.randint(1,6))
            Sv_rolls = [roll for roll in Sv_rolls if roll <= SvTarget]

            # count the total damage dealt.
            damage = (len(Sv_rolls)) * weapon.D
            print(f"{target} has {len(Sv_rolls)} unsaved wounds, receiving {damage} damage!")

            # process ward saves
            # extra saves that is made.
            if target.ward != 0:
                ward_rolls = []
                for i in range(damage * weapon.D):
                    ward_rolls.append(r.randint(1,6))
                ward_rolls = [roll for roll in ward_rolls if roll >= target.ward]

                if len(ward_rolls) != 0:
                    print(f"{target} saved {len(ward_rolls)} damage from Ward")
                    damage -= len(ward_rolls)
                else: print(f"{target} did not save any wounds through ward.")

            # counts the amount of casualties that the target unit suffers!
            casualties = damage // target.W
            if casualties != 0:
                print(f"{target} suffers {casualties} casualties")
            
            # Wounds unit that took damage, but did not die.
            unallocated_damage = damage - (casualties * target.W)
            if unallocated_damage != 0:
                print(f"A {str(target)[:-1]} is wounded but not slain after suffering {unallocated_damage} damage")
                target.CW = unallocated_damage
            print()



                
            

            
            
        