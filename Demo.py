# Demo Sheet for Wargame Project
from CombatRound import CombatRound
from CoreRules import Unit
from CoreRules import Weapon
from CoreRules import Ability

class Liberator(Unit):
    def __init__(self):
        super().__init__("Liberators",4,4,4,4,2,4,8,3,5)
        self.weapon_list.append(Weapon("Sigmarite Hammer", 2, 0, 4, -1, 1,["-"]))
        Sigmarite_Shield = Ability("Sigmarite Shield", "This Unit has a 5+ Invulnerable Save", "Passive")
        LayLowTheTyrant = Ability("Lay Low The Tyrant", "At the end of each combat, this unit does D3 mortal wounds to the unit it is in combat with", "EndOfCombat")
        self.abilities_list.append(Sigmarite_Shield)
        self.abilities_list.append(LayLowTheTyrant)

class DummyEnemy(Unit):
    def __init__(self):
        super().__init__("Wooden Dummy", 0, 3, 0, 3, 1, 0, 100, 4, 5)
        self.weapon_list.append(Weapon("Spinning Hammer", 4, -1, 5, -2, 1, "-"))
    
Johns = Liberator()
Bobs = Liberator()
Johns.display_stats()

Dummys = DummyEnemy()
Dummys.display_stats()

CombatRound([Johns, Bobs], [Dummys])
    