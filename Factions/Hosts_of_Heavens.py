from CoreRules import Unit
from CoreRules import Weapon
from CoreRules import Ability
from CoreRules import InflictWounds
from CoreRules import InflictMortalWounds
import random as r

# Hosts of Heavens faction data.

# Battleline

# Liberator - Core battleline of the faction, the basic warrior wielding one handed weapon such as swords and hammers and shield to smite the forces of darkness.
# They fight with vigor that assaults their enemies relentlessly.
class Liberator(Unit):
    def __init__(self):
        super().__init__("Lightborn Liberators",4,4,4,4,2,4,8,4,5,["HoH"])
        self.weapon_list.append(Weapon("Heavencrafted Weapon", 2, 0, 4, -1, 1,["-"],))
    
        # Initializes the ability of the unit.
        class Heavencrafted_Shield(Ability):
            def OnInit(parent):
                parent.ward = 6
                return parent
            
            def __init__(self):
                super().__init__("Heavencrafted Shield", "This Unit has a 6+ ward save", "Passive")
        
        class LLTT(Ability):
            def __init__(self):
                super().__init__("Lay Low The Tyrant", "At the end of each combat, this unit does D3 mortal wounds to a random unit it is in combat with", "CombatEnd")
            
            def CombatEnd(self,F,A,E):
                target = r.choice(E)
                damage = r.randint(1,3)
                print(f"The [Lightborn Liberators] continues their zealous onslaught!, inflicting {damage} mortal wounds to [{target}]")
                target = InflictMortalWounds(target, damage)
                return target
        
        self = Heavencrafted_Shield.OnInit(self)
        self.abilities_list.append(Heavencrafted_Shield())
        self.abilities_list.append(LLTT())
