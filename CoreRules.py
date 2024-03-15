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
    def __init__(self, name, description, type):
        self.name = name 
        self.description = description
        self.type = type # The ability type, this is used to check when the ability would fire off.
        # Current list of types: "Passive", "CombatStart", "CombatEnd", "OnKill", "OnCasualty", "OnDeath"
    
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
            