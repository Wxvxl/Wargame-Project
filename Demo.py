# Demo Sheet for Wargame Project
# Import the core rules.
from CombatRound import CombatRound
from CoreRules import Unit
from CoreRules import Weapon
from CoreRules import Ability

# Import factions used.
from Factions.Hosts_of_Heavens import Liberator

class DummyEnemy(Unit):
    def __init__(self):
        super().__init__("Wooden Dummy", 0, 3, 0, 3, 1, 0, 100, 5, 10, "Dummies")
        self.weapon_list.append(Weapon("Spinning Hammer", 3, -2, 5, -2, 1, "-"))
    
Johns = Liberator()
Dummys = DummyEnemy()

CombatRound([Johns], [Dummys])
