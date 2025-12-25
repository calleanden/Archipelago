from BaseClasses import ItemClassification, Item
from typing import TypedDict, Dict, List, Set, ClassVar
from .Types import ItemNames, ItemCategories
from .CustomDataClasses import DDItemData

class DarkestDungeonItem(Item):
    
    def __init__(self, name, data : DDItemData, player):
        self.data = data
        super().__init__(name, data.classification, data.address, player)

item_list = [
    DDItemData(ItemNames.TAVERN_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.ABBEY_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.GUILD_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.NOMAD_WAGON_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.SANITARIUM_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.STAGECOACH_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.SURVIVALIST_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.BLACKSMITH_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.WARRENS_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.WEALD_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.COVE_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.RUINS_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.DARKEST_KEY.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.ABBEY_CLOISTER_PROG.value, classification=ItemClassification.useful, category=ItemCategories.UPGRADE),
    DDItemData(ItemNames.ABBEY_TRANSEPT_PROG.value, classification=ItemClassification.useful, category=ItemCategories.UPGRADE),
    DDItemData(ItemNames.ABBEY_PENANCE_PROG.value, classification=ItemClassification.useful, category=ItemCategories.UPGRADE),
    DDItemData(ItemNames.BLACKSMITH_WEAPONSMITHING_PROG.value, classification=ItemClassification.useful, category=ItemCategories.UPGRADE),
    DDItemData(ItemNames.RUINS_NECRO_KEY_1.value, classification=ItemClassification.progression, category=ItemCategories.KEY),
    DDItemData(ItemNames.RUINS_NECRO_TROPHY_1.value, classification=ItemClassification.progression, category=ItemCategories.TROPHY),
    DDItemData(ItemNames.DD_MARK.value, classification=ItemClassification.progression,category=ItemCategories.KEY),
    DDItemData(ItemNames.FILLER_ITEM_1.value)
]

item_dictionary = {item_data.name : item_data for item_data in item_list}
