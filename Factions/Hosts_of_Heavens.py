from CoreRules import Unit
from CoreRules import Weapon
from CoreRules import Ability

# Hosts of Heavens faction data.

# Battleline

# Liberator - Core battleline faction, the basic warrior wielding hammers and shield to smite the forces of darkness.
class Liberator(Unit):
    def __init__(self):
        super().__init__("Liberators",4,4,4,4,2,4,8,4,5, ["HoH"])
        self.weapon_list.append(Weapon("Heavencrafted Hammer", 2, 0, 4, -1, 1,["-"],))
        Heavencrafted_Shield = Ability("Heavencrafted Shield", "This Unit has a 6+ ward save", "Passive")
        LayLowTheTyrant = Ability("Lay Low The Tyrant", "At the end of each combat, this unit does D3 mortal wounds to a random unit it is in combat with", "CombatEnd")
        self.abilities_list.append(Heavencrafted_Shield)
        self.ward = 6
        self.abilities_list.append(LayLowTheTyrant)