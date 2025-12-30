from BaseClasses import ItemClassification, Item
from typing import TypedDict, Dict, List, Set, ClassVar
from typing import TYPE_CHECKING
from .Types import ItemNames, ItemCategories

if TYPE_CHECKING:
    from World import DarkestDungeonWorld


ITEM_NAME_TO_ID = {
    
    #0: Keys
    ItemNames.TAVERN_KEY.value : 1,
    ItemNames.ABBEY_KEY.value : 2,
    ItemNames.BLACKSMITH_KEY.value : 3,
    ItemNames.GUILD_KEY.value : 4,
    ItemNames.NOMAD_WAGON_KEY.value : 5,
    ItemNames.SANITARIUM_KEY.value : 6,
    ItemNames.STAGECOACH_KEY.value : 7,
    ItemNames.SURVIVALIST_KEY.value : 8,
    ItemNames.RUINS_KEY.value : 9,
    ItemNames.WARRENS_KEY.value : 10,
    ItemNames.WEALD_KEY.value : 11,
    ItemNames.COVE_KEY.value : 12,
    ItemNames.FARMSTEAD_KEY.value : 13,
    ItemNames.COURT_KEY.value : 14,
    ItemNames.DARKEST_KEY.value : 15,
    #100: Progressive upgrade items
    ItemNames.ABBEY_CLOISTER_PROG.value : 101,
    ItemNames.ABBEY_TRANSEPT_PROG.value : 102,
    ItemNames.ABBEY_PENANCE_PROG.value: 103,
    ItemNames.BLACKSMITH_WEAPONSMITHING_PROG.value : 104,
    ItemNames.BLACKSMITH_ARMORSMITHING_PROG.value : 105,
    ItemNames.BLACKSMITH_FURNACE_PROG.value : 106,
    ItemNames.GUILD_INSTRUCTOR_PROG.value : 107,
    ItemNames.GUILD_REGIMEN_PROG.value : 108,
    ItemNames.NOMAD_WAGON_SIZE_PROG.value : 109,
    ItemNames.NOMAD_WAGON_MERCHANT_PROG.value : 110,
    ItemNames.SANITARIUM_LIBRARY_PROG.value : 111,
    ItemNames.SANITARIUM_MEDICAL_PROG.value : 112,
    ItemNames.SANITARIUM_CELLS_PROG.value : 113,
    ItemNames.STAGECOACH_NETWORK_PROG.value : 114,
    ItemNames.STAGECOACH_BARRACKS_PROG.value : 115,
    ItemNames.STAGECOACH_RECRUITS_PROG.value : 116,
    ItemNames.SURVIVALIST_BONFIRE_PROG.value : 117,
    ItemNames.TAVERN_BAR_PROG.value : 118,
    ItemNames.TAVERN_GAMBLING_PROG.value : 119,
    ItemNames.TAVERN_BROTHEL_PROG.value : 120,
    #200: Goal unlock items
    ItemNames.DD_MARK.value : 201,
    ItemNames.RUINS_BOSS1_KEY_PROG.value : 202,
    ItemNames.RUINS_BOSS1_TROPHY_PROG.value : 203,
    ItemNames.RUINS_BOSS2_KEY_PROG.value : 204,
    ItemNames.RUINS_BOSS2_TROPHY_PROG.value : 205,
    ItemNames.WARRENS_BOSS1_KEY_PROG.value : 206,
    ItemNames.WARRENS_BOSS1_TROPHY_PROG.value : 207,
    ItemNames.WARRENS_BOSS2_KEY_PROG.value : 208,
    ItemNames.WARRENS_BOSS2_TROPHY_PROG.value : 209,
    ItemNames.WEALD_BOSS1_KEY_PROG.value : 210,
    ItemNames.WEALD_BOSS1_TROPHY_PROG.value : 211,
    ItemNames.WEALD_BOSS2_KEY_PROG.value : 212,
    ItemNames.WEALD_BOSS2_TROPHY_PROG.value : 213,
    ItemNames.COVE_BOSS1_KEY_PROG.value : 214,
    ItemNames.COVE_BOSS1_TROPHY_PROG.value : 215,
    ItemNames.COVE_BOSS2_KEY_PROG.value : 216,
    ItemNames.COVE_BOSS2_TROPHY_PROG.value : 217,
    #300: Endgame items
    ItemNames.DD_FINAL_QUEST_ITEM_1.value : 301,
    ItemNames.DD_FINAL_QUEST_ITEM_2.value : 302,
    ItemNames.DD_FINAL_QUEST_ITEM_3.value : 303,
    ItemNames.DD_FINAL_QUEST_ITEM_4.value : 304,
    #400: Filler items
    ItemNames.FILLER_ITEM_1.value : 401,
    ItemNames.FILLER_ITEM_2.value : 402
    }

def get_default_classification(item_name : str):
    if ITEM_NAME_TO_ID[item_name] < 100:
        return ItemClassification.progression;
    elif ITEM_NAME_TO_ID[item_name] < 200: 
        return ItemClassification.useful;
    elif ITEM_NAME_TO_ID[item_name] < 300:
        return ItemClassification.progression;
    elif ITEM_NAME_TO_ID[item_name] < 400:
        return ItemClassification.progression;
    else:
        return ItemClassification.filler;

def get_random_filler_name(world: "DarkestDungeonWorld"):
    f = {key:value for key, value in ITEM_NAME_TO_ID.items() if value > 400}
    return world.random.choice(list(f.keys()))

class DarkestDungeonItem(Item):
    game = "Darkest Dungeon"

def create_item_with_correct_classification(world : "DarkestDungeonWorld", name : str):
    classification = get_default_classification(name)
    return DarkestDungeonItem(name,classification, ITEM_NAME_TO_ID[name], world.player);

def create_all_items(world : "DarkestDungeonWorld"):

    #Key items (13)
    itempool : List[Item] = [
        world.create_item(ItemNames.TAVERN_KEY.value),
        world.create_item(ItemNames.ABBEY_KEY.value),
        world.create_item(ItemNames.BLACKSMITH_KEY.value),
        world.create_item(ItemNames.GUILD_KEY.value),
        world.create_item(ItemNames.NOMAD_WAGON_KEY.value),
        world.create_item(ItemNames.SANITARIUM_KEY.value),
        world.create_item(ItemNames.STAGECOACH_KEY.value),
        world.create_item(ItemNames.SURVIVALIST_KEY.value),
        world.create_item(ItemNames.RUINS_KEY.value),
        world.create_item(ItemNames.WARRENS_KEY.value),
        world.create_item(ItemNames.WEALD_KEY.value),
        world.create_item(ItemNames.COVE_KEY.value),
        world.create_item(ItemNames.DARKEST_KEY.value)
        ]
    #Upgrade items (100)
    for i in range(4):
        itempool.append(world.create_item(ItemNames.STAGECOACH_RECRUITS_PROG.value));
        itempool.append(world.create_item(ItemNames.NOMAD_WAGON_SIZE_PROG.value))
        itempool.append(world.create_item(ItemNames.BLACKSMITH_WEAPONSMITHING_PROG.value))
        itempool.append(world.create_item(ItemNames.BLACKSMITH_ARMORSMITHING_PROG.value))
        itempool.append(world.create_item(ItemNames.SANITARIUM_CELLS_PROG.value))
        itempool.append(world.create_item(ItemNames.GUILD_INSTRUCTOR_PROG.value))
    for i in range(5):
        itempool.append(world.create_item(ItemNames.GUILD_REGIMEN_PROG.value))
        itempool.append(world.create_item(ItemNames.BLACKSMITH_FURNACE_PROG.value))
        itempool.append(world.create_item(ItemNames.NOMAD_WAGON_MERCHANT_PROG.value))
        itempool.append(world.create_item(ItemNames.SANITARIUM_LIBRARY_PROG.value))
        itempool.append(world.create_item(ItemNames.SANITARIUM_MEDICAL_PROG.value))
        itempool.append(world.create_item(ItemNames.SURVIVALIST_BONFIRE_PROG.value))
        itempool.append(world.create_item(ItemNames.STAGECOACH_NETWORK_PROG.value))
        itempool.append(world.create_item(ItemNames.STAGECOACH_BARRACKS_PROG.value))
    for i in range(6):
        itempool.append(world.create_item(ItemNames.ABBEY_CLOISTER_PROG.value))
        itempool.append(world.create_item(ItemNames.ABBEY_TRANSEPT_PROG.value))
        itempool.append(world.create_item(ItemNames.ABBEY_PENANCE_PROG.value))
        itempool.append(world.create_item(ItemNames.TAVERN_BAR_PROG.value))
        itempool.append(world.create_item(ItemNames.TAVERN_GAMBLING_PROG.value))
        itempool.append(world.create_item(ItemNames.TAVERN_BROTHEL_PROG.value))
    #Boss progression items
    for i in range(3):
        itempool.append(world.create_item(ItemNames.RUINS_BOSS1_KEY_PROG))
        itempool.append(world.create_item(ItemNames.RUINS_BOSS2_KEY_PROG))
        itempool.append(world.create_item(ItemNames.WARRENS_BOSS1_KEY_PROG))
        itempool.append(world.create_item(ItemNames.WARRENS_BOSS2_KEY_PROG))
        itempool.append(world.create_item(ItemNames.WEALD_BOSS1_KEY_PROG))
        itempool.append(world.create_item(ItemNames.WEALD_BOSS2_KEY_PROG))
        itempool.append(world.create_item(ItemNames.COVE_BOSS1_KEY_PROG))
        itempool.append(world.create_item(ItemNames.COVE_BOSS2_KEY_PROG))
    #DLC items 
    if world.options.enable_CC_DLC:
        itempool.append(world.create_item(ItemNames.COURT_KEY.value))
    if world.options.enable_CoM_DLC:
        itempool.append(world.create_item(ItemNames.FARMSTEAD_KEY.value))
    if world.options.open_dungeon:
        itempool.append(world.create_item(ItemNames.DD_FINAL_QUEST_ITEM_1.value))
        itempool.append(world.create_item(ItemNames.DD_FINAL_QUEST_ITEM_2.value))
        itempool.append(world.create_item(ItemNames.DD_FINAL_QUEST_ITEM_3.value))
    for _ in range(18):
        itempool.append(world.create_item(ItemNames.DD_MARK.value))
    item_count = len(itempool)
    unfilled_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    filler_item_count = unfilled_location_count - item_count;
    itempool += [world.create_filler() for _ in range(filler_item_count)]
    world.multiworld.itempool += itempool