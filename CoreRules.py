import random as r

# This initializes the core rules of the game. Such as unit stats, weapon stats, etc.
# Necessary to import this: "from CoreRules Import X" where X is Weapon, Ability, Unit etc.
class Weapon: 
    def __init__(self, name, A, HM, S, AP, D, abilities):
        self.name = name
        self.A = A # The attack value of the weapon.
        self.HM = HM # The "Hit Modifier" of the weapon, modifies the unit WS by this much when attacking.
        self.S = S # Strength of the weapon, it is compared to the target's toughness when attacking.
        self.AP = AP # "Armor Piercing" reduce the enemy armor save by this much.
        self.D = D # Damage, when the weapon successfuly wounds a target it does this much damage.
        self.abilities = abilities # The list of abilities, this is a list value that contains the "Ability" class.
    
    def __str__(self) -> str:
        return self.name

class Ability:
    def __init__(self, name, description, ability_type):
        self.name = name 
        self.description = description
        self.type = ability_type # The ability type, this is used to check when the ability would fire off.
        # Current list of types: "Passive", "CombatStart", "CombatEnd", "OnKill", "OnCasualty", "OnDeath", "OnInit"
    
class Unit:
    def __init__(self, name, M, WS, BS, T, W, I, LD, Sv, Count, Tags):
        # TODO: Refactor the unit class to be able to have mixed-model units.
        # Initializes all of the basic stats of the unit
        self.name = name
        self.M = M # Movement value, unit will move by this much. 
        self.WS = WS # Weapon Skill, decides how good the unit is at melee combat, helps with hitting more often and getting hit less.
        self.BS = BS # Ballistic Skill, decides how accurate the unit is when shooting.
        self.T = T # Toughness, how tough the unit is, compared with the weapon strength to see if the unit will be wounded.
        self.W = W # Wounds per model.
        self.CW = W # The current wound of the unit, only used if some unit is partially wounded. 
        self.I = I # Initiative, decides the order that the unit would strike in, higher initiative is faster.
        self.LD = LD # Leadership value, decides the morale 
        self.Sv = Sv # Armor Save, when this unit is successfully wounded they must roll equal or higher to the armor save value to "save" that wound.
        # Armor save is modified by the attacker's armor piercing.
        self.caxcount = Count # How many model the unit can have at max 
        self.curcount = Count # The current count of model in the unit.
        self.weapon_list = [] # List of weapons that the unit carries. Usually contains only one weapon.
        self.abilities_list = [] # List of the abilities that the unit has. See ability class.
        self.tags = [] # Tags associated with the unit, keywords, whether its reinforced,
        self.statuseffects = [] # Status effects applied to the unit. 
        # TODO: Create status effects class.

        # EXTRA STATLINES 
        # Statlines that are not available to each unit.
        self.ward = 0 # An additional save that is made for every point of damage that is dealt.
        self.invuln = 0 # A save that is made if armor piercing exceeds this value instead of normal save. This value cannot be modified by AP.
    
    def __str__(self) -> str:
        return self.name
    
def display_stats(self):
    # Displays all of the stats that the unit has.
    print(f"Unit name        : {self.name}") 
    print(f"Movement         : {self.M}")
    print(f"Weapon Skill     : {self.WS}")
    print(f"Ballistic Skill  : {self.BS}")
    print(f"Toughness        : {self.T}")
    print(f"Wounds Per Model : {self.W}")
    print(f"Initiative       : {self.I}")
    print(f"Leadership       : {self.LD}")
    print(f"Armour Save      : {self.Sv}+")
    print(f"Squad Count      : {self.curcount}")
    print()
    # Displays all of the weapon the unit is equipped with. 
    # Some units may carry multiple weapons.
    print(f'{"Weapon Name":<20}| {"HM":^2} | {"S":^2} | {"AP":^2} | {"D":^1} | {"Abilities":<16}')
    for weapon in self.weapon_list:
        print(f'{weapon.name:<20}| {weapon.A:^2} | {weapon.S:^2} | {weapon.AP:^2} | {weapon.D:^1} | {", ".join(weapon.abilities):^8}')

    # Prints all of the abilities that the unit has and their description.
    if self.abilities_list != []:
        print()
        print(f"{'Ability Name':<20} | {'Description':<30}")
        for ability in self.abilities_list:
            print(f"{ability.name:<20} | {ability.description:<30}")
    print()

def InflictCasualties(target, damage):
    # counts the amount of casualties that the target unit suffers!
    casualties = 0
    pre_casualties = 0
    
    if damage == 0:
        print()
        return target
    
    if target.CW != target.W:
        damage -= target.CW
        if damage <= 0:
            damage = 0
        pre_casualties += 1
    
    casualties += damage // target.W
    if casualties != 0 or pre_casualties != 0:
        target.curcount -= casualties + pre_casualties
        if target.curcount <= 0: target.curcount = 0 
        print(f"[{target}] suffers {casualties + pre_casualties} casualties")
        print(f"[{target}] only has {target.curcount} model(s) left!")
            
     # Wounds unit that took damage, but did not die.
    unallocated_damage = damage - (casualties * target.W)
    if unallocated_damage != 0:
        print(f"A [{str(target)[:-1]}] is wounded but not slain after suffering {unallocated_damage} damage")
        target.CW = unallocated_damage
    print()
    return target

def InflictWounds(fighter, weapon, target, wounds):
      # Units now make their saving throws.
    print(f"[{target}] rolling for saving throws")
    print(f"[{target}] has a {target.Sv}+ save, reduced by [{fighter}]'s [{weapon}] with AP{weapon.AP}")     
    
    # Modifies the save by the weapon AP value.
    SvTarget = target.Sv - weapon.AP
    
    # Roll the saving throws and remove all of the saved wounds.
    print(f"[{target}] needs {SvTarget}+ to successfully save a wound!")
    input("Press enter to continue")
    print()
    Sv_rolls = []
    for i in range(wounds):
        Sv_rolls.append(r.randint(1,6))
    Sv_rolls = [roll for roll in Sv_rolls if roll <= SvTarget]
    # count the total damage dealt.
    damage = (len(Sv_rolls)) * weapon.D
    if len(Sv_rolls) != 0:
        print(f"[{target}] has {len(Sv_rolls)} unsaved wounds, receiving {damage} damage!")
    else:
        print(f"[{target}] has successfuly saved all wounds receiving no damage!")
    print()
    # process ward saves
    # extra saves that is made.
    if target.ward != 0:
        print(f"[{target}] has a Ward save of {target.ward}+!")
        input("Press enter to continue")
        print()
        ward_rolls = []
        for i in range(damage * weapon.D):
            ward_rolls.append(r.randint(1,6))
        ward_rolls = [roll for roll in ward_rolls if roll >= target.ward]
        if len(ward_rolls) != 0:
            print(f"[{target}] saved {len(ward_rolls)} damage from Ward")
            damage -= len(ward_rolls)
        else: print(f"[{target}] did not save any wounds through Ward.")
        print()
    return damage

def InflictMortalWounds(target, MW):
    if target.ward != 0:
        print(f"[{target}] has a Ward save of {target.ward}+!")
        ward_rolls = []
        for i in range(MW):
            ward_rolls.append(r.randint(1,6))

        ward_rolls = [roll for roll in ward_rolls if roll >= target.ward]
    
        if len(ward_rolls) != 0:
            print(f"[{target}] saved {len(ward_rolls)} damage from Ward")
            MW -= len(ward_rolls)
            if MW <= 0:
                MW = 0
        else: print(f"[{target}] did not save any wounds through ward.")
    target = InflictCasualties(target, MW)
    return target
  
def RollToHit(rolls_count, fighter, weapon, target):
    hit_rolls = []
    for i in range(rolls_count):
        hit_rolls.append(r.randint(1,6))

    # set the number you need to score a successful hit.
    # Compare the attacker's WS and the defender's WS.
    if (fighter.WS + weapon.HM) > 2 * (target.WS + target.weapon_list[0].HM):
        hitTarget = 2 # if attacker WS is more than double of defender WS, hitting on 2+
    elif (fighter.WS + weapon.HM) > (target.WS + target.weapon_list[0].HM):
        hitTarget = 3 # if attacker WS is more than defender WS, hitting on 3+  
    elif (target.WS + target.weapon_list[0].HM) * 2 > (fighter.WS + weapon.HM):
        hitTarget = 5 # if defender WS is more than double of attacker WS, hitting on 5+    
    elif ((target.WS + target.weapon_list[0].HM) * 2) + 3 > (fighter.WS + weapon.HM):
        hitTarget = 6 # if defender WS is more than double that of the attacker + 3, then hit on 6+
    if (fighter.WS + weapon.HM) == (target.WS + target.weapon_list[0].HM): hitTarget = 4
    
    print(f"[{fighter}] attacking using [{weapon}] with WS {fighter.WS + weapon.HM}")
    print(f"[{target}] defending using [{target.weapon_list[0]}] with WS {target.WS + target.weapon_list[0].HM}")
    print(f"Roll needed to hit: {hitTarget}+")
    input("Press enter to continue")
    print()
    # Remove all of the hit roll that does does not meet the hit criteria.
    hit_rolls = [roll for roll in hit_rolls if roll >= hitTarget]
    if len(hit_rolls) != 0:
        print(f"Successful hit for [{fighter}] against [{target}]: {hit_rolls}")
    else: print(f"[{fighter}] fails to hit [{target}]!")
    print()

    return hit_rolls

def RollToWound(fighter, target, weapon, hit_rolls):
     # rolling to wound, works the same way as rolling to hit except successful wound is dictated by Strength and Toughness.
    wound_rolls = []
    print(f"[{fighter}] rolling to wound against [{target}] using [{weapon}] with Strength {weapon.S}")
    print(f"[{target}] has Toughness {target.T}")
    if (weapon.S) >= 2 * (target.T):
        hitTarget = 2 # if Strength more than or equal to double of target Toughness wounding on 2+
    elif (weapon.S) > (target.T):
        hitTarget = 3 # if Strength higher than toughness, then wounding on 3
    elif (weapon.S) < (target.T):
        hitTarget = 5 # If strength lower than toughness, wounding on 5+
    elif (weapon.S) <= (target.T) * 2:
        hitTarget = 6 # If strength lower than double of toughness, wounding on 6+!
    if (weapon.S) == (target.T): hitTarget = 4

    # Rolls the wound roll, works the same way as hit roll.
    print(f"roll needed to successfully wound: {hitTarget}+")
    input("Press enter to continue")
    print()
    for i in range(len(hit_rolls)):
        wound_rolls.append(r.randint(1,6))
    wound_rolls = [roll for roll in wound_rolls if roll >= hitTarget]
    if len(wound_rolls) != 0:
        print(f"Successful wounds for [{fighter}] against [{target}]: {wound_rolls}")
    else: print(f"[{fighter}] fails to wound [{target}]!")
    print()
    return wound_rolls