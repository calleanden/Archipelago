from BaseClasses import ItemClassification, Item
from typing import TypedDict, Dict, List, Set

class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification

base_id = 1



#{"name": "", "count": 0, "classification":ItemClassification},
item_table: List[ItemDict] = [
    {"name": "Brewer's License", "count":1, "classification":ItemClassification.progression}, #Unlocks tavern
    {"name": "Sanctified Ground", "count": 1, "classification":ItemClassification.progression}, #Unlocks abbey
    {"name": "Guild Representative", "count": 1, "classification":ItemClassification.progression}, #Unlocks guild
    {"name": "Good Will of the Nomads", "count": 1, "classification":ItemClassification.progression}, #Unlocks nomad wagon
    {"name": "Doctor's License", "count": 1, "classification":ItemClassification.progression}, #Unlocks sanitarium
    {"name": "Clear Roads", "count": 1, "classification":ItemClassification.progression}, #Unlocks stagecoach
    {"name": "Friend of the Wilderfolk", "count": 0, "classification":ItemClassification.progression}, #Unlocks survivalist
    {"name": "The Forge's Flames", "count": 1, "classification":ItemClassification.progression}, #Unlocks blacksmith
    {"name": "Warrens Key", "count": 1, "classification":ItemClassification.progression}, #Unlocks Warrens
    {"name": "Weald Key", "count": 1, "classification":ItemClassification.progression}, #Unlocks the Weald
    {"name": "Cove Key", "count": 1, "classification":ItemClassification.progression}, #Unlocks the Cove
    {"name": "Ruins Key", "count": 1, "classification":ItemClassification.progression}, #Unlocks the Ruins
    {"name": "Darkest Dungeon Key", "count":1, "classification":ItemClassification.progression} #Unlocks the Darkest Dungeon

]