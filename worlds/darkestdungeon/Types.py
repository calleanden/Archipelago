from enum import StrEnum

class DLCNames(StrEnum):
    NONE = "Base Game"
    CC = "Crimson Court"
    COM = "Color of Madness"
    SB = "The Shieldbreaker"

class RegionNames(StrEnum):
    MENU = "Main Menu"
    HAMLET = "The Hamlet"
    RUINS = "The Ruins"
    WEALD = "The Weald"
    WARRENS = "The Warrens"
    COVE = "The Cove"
    DARKEST = "The Darkest Dungeon"
    ABBEY = "The Abbey"
    BLACKSMITH = "The Blacksmith"
    GUILD = "The Guild"
    NOMAD_WAGON = "The Nomad Wagon"
    SANITARIUM = "The Sanitarium"
    STAGECOACH = "The Stagecoach"
    SURVIVALIST = "The Survivalist"
    TAVERN = "The Tavern"
    COURT = "The Crimson Court"
    FARM = "The Farmstead"
    QUEST_GOALS = "Quest Goals"

class ItemCategories(StrEnum):
    MISC = "Miscallenous"
    KEY = "Key"
    UPGRADE = "Upgrade Item"
    TROPHY = "Trophy Item"

class ItemNames(StrEnum):
    TAVERN_KEY = "Brewer's License"
    ABBEY_KEY = "Sanctified Ground"
    GUILD_KEY = "Guild Representative"
    NOMAD_WAGON_KEY = "Good Will of the Nomads"
    SANITARIUM_KEY = "Doctor's License"
    STAGECOACH_KEY = "Clear Roads"
    SURVIVALIST_KEY = "Friend of the Wilderfolk"
    BLACKSMITH_KEY = "Sturdy Anvil"
    WARRENS_KEY = "Footpath to the Warrens"
    WEALD_KEY = "Footpath to the Weald"
    COVE_KEY = "Footpath to the Cove"
    RUINS_KEY = "Footpath to the Ruins"
    DARKEST_KEY = "Footpath to the Darkest Dungeon"
    FARMSTEAD_KEY = "Footpath to the Farmstead"
    COURT_KEY = "Footpath to the Crimson Court"
    ABBEY_CLOISTER_1 = "AP Cloister 1"
    ABBEY_CLOISTER_2 = "AP Cloister 2"
    ABBEY_CLOISTER_3 = "AP Cloister 3"
    ABBEY_CLOISTER_4 = "AP Cloister 4"
    ABBEY_CLOISTER_5 = "AP Cloister 5"
    ABBEY_CLOISTER_6 = "AP Cloister 6"
    ABBEY_TRANSEPT_1 = "AP Transept 1"
    ABBEY_TRANSEPT_2 = "AP Transept 2"
    ABBEY_TRANSEPT_3 = "AP Transept 3"
    ABBEY_TRANSEPT_4 = "AP Transept 4"
    ABBEY_TRANSEPT_5 = "AP Transept 5"
    ABBEY_TRANSEPT_6 = "AP Transept 6"
    ABBEY_PENANCE_1 = "AP Penance Hall 1"
    ABBEY_PENANCE_2 = "AP Penance Hall 2"
    ABBEY_PENANCE_3 = "AP Penance Hall 3"
    ABBEY_PENANCE_4 = "AP Penance Hall 4"
    ABBEY_PENANCE_5 = "AP Penance Hall 5"
    ABBEY_PENANCE_6 = "AP Penance Hall 6"
    BLACKSMITH_WEAPONSMITHING = "AP Weaponsmithing"
    RUINS_NECRO_KEY_1 = "Apprentice Necromancer Key"
    RUINS_NECRO_TROPHY_1 = "Introduction to Necromancy"
    FILLER_ITEM_1 = "Trinkets and Baubles"


class LocationNames(StrEnum):
    Quests_0_ST = "Tutorial Quest Stagecoach Unlock",
    Quests_0_NW = "Tutorial Quest Nomad Wagon Unlock",
    Quests_0_RU = "Tutorial Quest Ruins Unlock",
    Quests_0_DD = "Tutorial Quest Darkest Dungeon Unlock",
    Quests_1_AB = "Quest 1 Abbey Unlock",
    Quests_1_TA = "Quest 1 Tavern Unlock",
    Quests_1_FS = "Quest 1 Farmstead Unlock",
    Quests_2_BS = "Quest 2 Blacksmith Unlock",
    Quests_2_GU = "Quest 2 Guild Unlock",
    Quests_2_WE = "Quest 2 Weald Unlock",
    Quests_3_SA = "Quest 3 Sanitarium Unlock",
    Quests_3_CO = "Quest 3 Cove",
    Quests_3_WA = "Quest 3 Warrens Unlock",
    Quests_RUINS_1 = "Finish 1 Ruins Quest",
    Abbey_Cloister_1 = "Abbey Cloister Level 1 Upgrade",
    Abbey_Cloister_2 = "Abbey Cloister Level 2 Upgrade",
    Abbey_Cloister_3 = "Abbey Cloister Level 3 Upgrade",
    Abbey_Cloister_4 = "Abbey Cloister Level 4 Upgrade",
    Abbey_Cloister_5 = "Abbey Cloister Level 5 Upgrade",
    Abbey_Cloister_6 = "Abbey Cloister Level 6 Upgrade",
    Abbey_Transept_1 = "Abbey Transept Level 1 Upgrade",
    Abbey_Transept_2 = "Abbey Transept Level 2 Upgrade",
    Abbey_Transept_3 = "Abbey Transept Level 3 Upgrade",
    Abbey_Transept_4 = "Abbey Transept Level 4 Upgrade",
    Abbey_Transept_5 = "Abbey Transept Level 5 Upgrade",
    Abbey_Transept_6 = "Abbey Transept Level 6 Upgrade",
    Abbey_Penance_Hall_1 = "Abbey Penance Hall Level 1 Upgrade",
    Abbey_Penance_Hall_2 = "Abbey Penance Hall Level 2 Upgrade",
    Abbey_Penance_Hall_3 = "Abbey Penance Hall Level 3 Upgrade",
    Abbey_Penance_Hall_4 = "Abbey Penance Hall Level 4 Upgrade",
    Abbey_Penance_Hall_5 = "Abbey Penance Hall Level 5 Upgrade",
    Abbey_Penance_Hall_6 = "Abbey Penance Hall Level 6 Upgrade",
    Blacksmith_Weaponsmithing_1 = "Blacksmith Weaponsmithing Level 1 Upgrade",
    Blacksmith_Weaponsmithing_2 = "Blacksmith Weaponsmithing Level 2 Upgrade",
    Blacksmith_Weaponsmithing_3 = "Blacksmith Weaponsmithing Level 3 Upgrade",
    Blacksmith_Weaponsmithing_4 = "Blacksmith Weaponsmithing Level 4 Upgrade",
    Blacksmith_Armorsmithing_1 = "Blacksmith Armorsmithing Level 1 Upgrade",
    Blacksmith_Armorsmithing_2 = "Blacksmith Armorsmithing Level 2 Upgrade",
    Blacksmith_Armorsmithing_3 = "Blacksmith Armorsmithing Level 3 Upgrade",
    Blacksmith_Armorsmithing_4 = "Blacksmith Armorsmithing Level 4 Upgrade",
    Blacksmith_Furnace_1 = "Blacksmith Furnace Level 1 Upgrade",
    Blacksmith_Furnace_2 = "Blacksmith Furnace Level 2 Upgrade",
    Blacksmith_Furnace_3 = "Blacksmith Furnace Level 3 Upgrade",
    Blacksmith_Furnace_4 = "Blacksmith Furnace Level 4 Upgrade",
    Blacksmith_Furnace_5 = "Blacksmith Furnace Level 5 Upgrade",
    Ruins_Level_1 = "Ruins Level 1"
    Ruins_Necromancer_1 = "The Necromancer Apprentice"