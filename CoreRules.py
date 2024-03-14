class Weapon: 
    def __init__(self, name, A, HM, S, AP, D, abilities):
        self.name = name
        self.A = A
        self.HM = HM
        self.S = S
        self.AP = AP
        self.D = D
        self.abilities = abilities
    
    def __str__(self) -> str:
        return self.name

class Ability:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type
    
class Unit:
    def __init__(self, name, M, WS, BS, T, W, I, LD, Sv, Count):
        # Initializes all of the basic stats of the unit
        self.name = name
        self.M = M
        self.WS = WS
        self.BS = BS
        self.T = T
        self.W = W
        self.CW = W
        self.I = I
        self.LD = LD
        self.Sv = Sv
        self.Count = Count
        self.weapon_list = []
        self.abilities_list = []
    
    def __str__(self) -> str:
        return self.name
    
    def display_stats(self):
        print(f"Unit name        : {self.name}")
        print(f"Movement         : {self.M}")
        print(f"Weapon Skill     : {self.WS}")
        print(f"Ballistic Skill  : {self.BS}")
        print(f"Toughness        : {self.T}")
        print(f"Wounds Per Model : {self.W}")
        print(f"Initiative       : {self.I}")
        print(f"Leadership       : {self.LD}")
        print(f"Armour Save      : {self.Sv}+")
        print(f"Squad Count      : {self.Count}")
        print()

        print(f'{"Weapon Name":<20}| {"HM":^2} | {"S":^2} | {"AP":^2} | {"D":^1} | {"Abilities":<16}')
        for weapon in self.weapon_list:
            print(f'{weapon.name:<20}| {weapon.A:^2} | {weapon.S:^2} | {weapon.AP:^2} | {weapon.D:^1} | {", ".join(weapon.abilities):^8}')

        if self.abilities_list != []:
            print()
            print(f"{'Ability Name':<20} | {'Description':<30}")
            for ability in self.abilities_list:
                print(f"{ability.name:<20} | {ability.description:<30}")
        print()
            