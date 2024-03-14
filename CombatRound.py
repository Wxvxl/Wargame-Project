import random as r

def CombatRound(A, B):
    Fighters = []
    Fighters.extend(A)
    Fighters.extend(B)
    Combat_Order = sorted(Fighters, key=lambda x: x.I, reverse=True)
    print("Combat Begins!")
    for i,fighter in enumerate(Combat_Order):
        print(f"{i+1}. {fighter} at initiative {fighter.I}")
    print()

    for fighter in Combat_Order:
        if fighter in A:
            target = r.choice(B)
        else:
            target = r.choice(A)
        
        # rolling to hit
        for weapon in fighter.weapon_list:
            rolls_count = fighter.Count * weapon.A
            hit_rolls = []
            
            # start rolling to hit
            for i in range(rolls_count):
                hit_rolls.append(r.randint(1,6))
            
            # set the number you need to score a successful hit.
            hitTarget = 4
            if (fighter.WS + weapon.HM) > 2 * (target.WS + target.weapon_list[0].HM):
                hitTarget = 2
            
            elif (fighter.WS + weapon.HM) > (target.WS + target.weapon_list[0].HM):
                hitTarget = 3

            elif (target.WS + target.weapon_list[0].HM) * 2 > (fighter.WS + weapon.HM):
                hitTarget = 5

            elif ((target.WS + target.weapon_list[0].HM) * 2) + 3 > (fighter.WS + weapon.HM):
                hitTarget = 6

            
            print(f"{fighter} attacking {target} using {weapon}")
            print(f"{fighter} WS: {fighter.WS + weapon.HM}")
            print(f"{target} WS: {target.WS + target.weapon_list[0].HM}")
            print(f"Roll needed to hit: {hitTarget}+")
            hit_rolls = [roll for roll in hit_rolls if roll >= hitTarget] 
            
            print(f"Successful hit for {fighter} against {target}: {hit_rolls}")
            print()
        
            # rolling to wound
            wound_rolls = []
            print(f"{fighter} rolling to wound against {target} using {weapon} with {weapon.S} strength against {target} with {target.T} toughness")
            hitTarget = 4

            if (weapon.S) >= 2 * (target.T):
                hitTarget = 2
            
            elif (weapon.S) >= (target.T):
                hitTarget = 3
            
            elif (weapon.S) < (target.T):
                hitTarget = 5
            
            elif (weapon.S) < (target.T) * 2:
                hitTarget = 6
            
            print(f"roll needed to successfully wound: {hitTarget}+")
            for i in range(len(hit_rolls)):
                wound_rolls.append(r.randint(1,6))
            wound_rolls = [roll for roll in wound_rolls if roll >= hitTarget]
            print(f"Successful wounds for {fighter} against {target}: {wound_rolls}")
            print()

            # Saving throws
            print(f"{target} rolling for saving throws")
            print(f"{target} has a {target.Sv}+ save, reduced by {fighter}'s {weapon} with AP{weapon.AP}")

            if target.Sv - weapon.AP <= 1:
                SvTarget = 2
            else:
                SvTarget = target.Sv - weapon.AP
            
            print(f"{target} needs {SvTarget}+ to successfully save a wound!")
            wound_rolls = [roll for roll in wound_rolls if roll < SvTarget]
            damage = (len(wound_rolls)) * weapon.D
            print(f"{target} has {len(wound_rolls)} unsaved wounds, receiving {damage} damage!")

            casualties = damage // target.W
            print(f"{target} suffers {casualties} casualties")
            
            unallocated_damage = damage - (casualties * target.W)
            if unallocated_damage != 0:
                print(f"A {target} is wounded but not slain after suffering {unallocated_damage} damage")
                target.CW = unallocated_damage
            print()



                
            

            
            
        