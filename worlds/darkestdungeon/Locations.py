from typing import Dict, ClassVar, TYPE_CHECKING
from dataclasses import dataclass
from BaseClasses import Location
from .Items import DarkestDungeonItem
from .Types import ItemNames, LocationNames, RegionNames
if TYPE_CHECKING:
    from .World import DarkestDungeonWorld

LOCATION_NAME_TO_ID = {
    #0: Tutorial quest locations
    LocationNames.Quests_0_ST.value : 1,
    LocationNames.Quests_0_NW.value : 2,
    LocationNames.Quests_0_RU.value : 3,
    LocationNames.Quests_0_DD.value : 4,
    #100: Initial quest locations
    LocationNames.Quests_1_AB.value : 101,
    LocationNames.Quests_1_FS.value : 102,
    LocationNames.Quests_1_TA.value : 103,
    LocationNames.Quests_2_BS.value : 104,
    LocationNames.Quests_2_GU.value : 105,
    LocationNames.Quests_2_WE.value : 106,
    LocationNames.Quests_2_CC.value : 107,
    LocationNames.Quests_3_CO.value : 108,
    LocationNames.Quests_3_SA.value : 109,
    LocationNames.Quests_3_WA.value : 110,
    LocationNames.Quests_4_SU.value : 111,
    #200: Abbey locations
    LocationNames.Abbey_Cloister_1.value : 201,
    LocationNames.Abbey_Cloister_2.value : 202,
    LocationNames.Abbey_Cloister_3.value : 203,
    LocationNames.Abbey_Cloister_4.value : 204,
    LocationNames.Abbey_Cloister_5.value : 205,
    LocationNames.Abbey_Cloister_6.value : 206,
    LocationNames.Abbey_Transept_1.value : 207,
    LocationNames.Abbey_Transept_2.value : 208,
    LocationNames.Abbey_Transept_3.value : 209,
    LocationNames.Abbey_Transept_4.value : 210,
    LocationNames.Abbey_Transept_5.value : 211,
    LocationNames.Abbey_Transept_6.value : 212,
    LocationNames.Abbey_Penance_Hall_1.value : 213,
    LocationNames.Abbey_Penance_Hall_2.value : 214,
    LocationNames.Abbey_Penance_Hall_3.value : 215,
    LocationNames.Abbey_Penance_Hall_4.value : 216,
    LocationNames.Abbey_Penance_Hall_5.value : 217,
    LocationNames.Abbey_Penance_Hall_6.value : 218,
    #300: Blacksmith locations
    LocationNames.Blacksmith_Weaponsmithing_1.value : 301,
    LocationNames.Blacksmith_Weaponsmithing_2.value : 302,
    LocationNames.Blacksmith_Weaponsmithing_3.value : 303,
    LocationNames.Blacksmith_Weaponsmithing_4.value : 304,
    LocationNames.Blacksmith_Armorsmithing_1.value : 305,
    LocationNames.Blacksmith_Armorsmithing_2.value : 306,
    LocationNames.Blacksmith_Armorsmithing_3.value : 307,
    LocationNames.Blacksmith_Armorsmithing_4.value : 308,
    LocationNames.Blacksmith_Furnace_1.value : 309,
    LocationNames.Blacksmith_Furnace_2.value : 310,
    LocationNames.Blacksmith_Furnace_3.value : 311,
    LocationNames.Blacksmith_Furnace_4.value : 312,
    LocationNames.Blacksmith_Furnace_5.value : 313,
    #400: Guild locations
    LocationNames.Guild_InstructorMastery_1.value : 401,
    LocationNames.Guild_InstructorMastery_2.value : 402,
    LocationNames.Guild_InstructorMastery_3.value : 403,
    LocationNames.Guild_InstructorMastery_4.value : 404,
    LocationNames.Guild_TrainingRegimen_1.value : 405,
    LocationNames.Guild_TrainingRegimen_2.value : 406,
    LocationNames.Guild_TrainingRegimen_3.value : 407,
    LocationNames.Guild_TrainingRegimen_4.value : 408,
    LocationNames.Guild_TrainingRegimen_5.value : 409,
    #500: Nomad wagon locations
    LocationNames.NomadWagon_Size_1.value : 501,
    LocationNames.NomadWagon_Size_2.value : 502,
    LocationNames.NomadWagon_Size_3.value : 503,
    LocationNames.NomadWagon_Size_4.value : 504,
    LocationNames.NomadWagon_MerchantNetwork_1.value : 505,
    LocationNames.NomadWagon_MerchantNetwork_2.value : 506,
    LocationNames.NomadWagon_MerchantNetwork_3.value : 507,
    LocationNames.NomadWagon_MerchantNetwork_4.value : 508,
    LocationNames.NomadWagon_MerchantNetwork_5.value  : 509,
    #600: Sanitarium locations
    LocationNames.Sanitarium_MedicalDevices_1.value  : 601,
    LocationNames.Sanitarium_MedicalDevices_2.value  : 602,
    LocationNames.Sanitarium_MedicalDevices_3.value  : 603,
    LocationNames.Sanitarium_MedicalDevices_4.value  : 604,
    LocationNames.Sanitarium_MedicalDevices_5.value  : 605,
    LocationNames.Sanitarium_PatientCells_1.value : 606,
    LocationNames.Sanitarium_PatientCells_2.value : 607,
    LocationNames.Sanitarium_PatientCells_3.value : 608,
    LocationNames.Sanitarium_PatientCells_4.value : 609,
    LocationNames.Sanitarium_TreatmentLibrary_1.value : 610,
    LocationNames.Sanitarium_TreatmentLibrary_2.value : 611,
    LocationNames.Sanitarium_TreatmentLibrary_3.value : 612,
    LocationNames.Sanitarium_TreatmentLibrary_4.value : 613,
    LocationNames.Sanitarium_TreatmentLibrary_5.value : 614,
    #700: Stagecoach locations
    LocationNames.Stagecoach_ExpRecruits_1.value : 701,
    LocationNames.Stagecoach_ExpRecruits_2.value : 702,
    LocationNames.Stagecoach_ExpRecruits_3.value : 703,
    LocationNames.Stagecoach_ExpRecruits_4.value : 704,
    LocationNames.Stagecoach_HeroBarracks_1.value : 705,
    LocationNames.Stagecoach_HeroBarracks_2.value : 706,
    LocationNames.Stagecoach_HeroBarracks_3.value : 707,
    LocationNames.Stagecoach_HeroBarracks_4.value : 708,
    LocationNames.Stagecoach_HeroBarracks_5.value : 709,
    LocationNames.Stagecoach_Network_1.value : 710,
    LocationNames.Stagecoach_Network_2.value : 711,
    LocationNames.Stagecoach_Network_3.value : 712,
    LocationNames.Stagecoach_Network_4.value : 713,
    LocationNames.Stagecoach_Network_5.value : 714,
    #800: Survivalist locations
    LocationNames.Survivalist_Bonfire_1.value : 801,
    LocationNames.Survivalist_Bonfire_2.value : 802,
    LocationNames.Survivalist_Bonfire_3.value : 803,
    LocationNames.Survivalist_Bonfire_4.value : 804,
    #900: Tavern locations
    LocationNames.Tavern_Bar_1.value : 901,
    LocationNames.Tavern_Bar_2.value : 902,
    LocationNames.Tavern_Bar_3.value : 903,
    LocationNames.Tavern_Bar_4.value : 904,
    LocationNames.Tavern_Bar_5.value : 905,
    LocationNames.Tavern_Bar_6.value : 906,
    LocationNames.Tavern_GamblingHall_1.value : 907,
    LocationNames.Tavern_GamblingHall_2.value : 908,
    LocationNames.Tavern_GamblingHall_3.value : 909,
    LocationNames.Tavern_GamblingHall_4.value : 910,
    LocationNames.Tavern_GamblingHall_5.value : 911,
    LocationNames.Tavern_GamblingHall_6.value : 912,
    LocationNames.Tavern_Brothel_1.value : 913,
    LocationNames.Tavern_Brothel_2.value : 914,
    LocationNames.Tavern_Brothel_3.value : 915,
    LocationNames.Tavern_Brothel_4.value : 916,
    LocationNames.Tavern_Brothel_5.value : 917,
    LocationNames.Tavern_Brothel_6.value : 918,
    #1000: RUINS locations
    LocationNames.RUINS_Boss1_1_mark.value : 1001,
    LocationNames.RUINS_Boss1_2_mark.value : 1002,
    LocationNames.RUINS_Boss1_3_mark.value : 1003,
    LocationNames.RUINS_Boss2_1_mark.value : 1004,
    LocationNames.RUINS_Boss2_2_mark.value : 1005,
    LocationNames.RUINS_Boss2_3_mark.value : 1006,
    LocationNames.RUINS_Level_1.value : 1007,
    LocationNames.RUINS_Level_2.value : 1008,
    LocationNames.RUINS_Level_3.value : 1009,
    LocationNames.RUINS_Level_4.value : 1010,
    LocationNames.RUINS_Level_5.value : 1011,
    LocationNames.RUINS_Level_6.value : 1012,
    LocationNames.RUINS_Level_7.value : 1013,
    #1100: WARRENS locations
    LocationNames.WARRENS_Boss1_1_mark.value : 1101,
    LocationNames.WARRENS_Boss1_2_mark.value : 1102,
    LocationNames.WARRENS_Boss1_3_mark.value : 1103,
    LocationNames.WARRENS_Boss2_1_mark.value : 1104,
    LocationNames.WARRENS_Boss2_2_mark.value : 1105,
    LocationNames.WARRENS_Boss2_3_mark.value : 1106,
    LocationNames.WARRENS_Level_1.value : 1107,
    LocationNames.WARRENS_Level_2.value : 1108,
    LocationNames.WARRENS_Level_3.value : 1109,
    LocationNames.WARRENS_Level_4.value : 1110,
    LocationNames.WARRENS_Level_5.value : 1111,
    LocationNames.WARRENS_Level_6.value : 1112,
    LocationNames.WARRENS_Level_7.value : 1113,
    #1200: WEALD locations
    LocationNames.WEALD_Boss1_1_mark.value : 1201,
    LocationNames.WEALD_Boss1_2_mark.value : 1202,
    LocationNames.WEALD_Boss1_3_mark.value : 1203,
    LocationNames.WEALD_Boss2_1_mark.value : 1204,
    LocationNames.WEALD_Boss2_2_mark.value : 1205,
    LocationNames.WEALD_Boss2_3_mark.value : 1206,
    LocationNames.WEALD_Level_1.value : 1207,
    LocationNames.WEALD_Level_2.value : 1208,
    LocationNames.WEALD_Level_3.value : 1209,
    LocationNames.WEALD_Level_4.value : 1210,
    LocationNames.WEALD_Level_5.value : 1211,
    LocationNames.WEALD_Level_6.value : 1212,
    LocationNames.WEALD_Level_7.value : 1213,
    #1300: COVE locations
    LocationNames.COVE_Boss1_1_mark.value : 1301,
    LocationNames.COVE_Boss1_2_mark.value : 1302,
    LocationNames.COVE_Boss1_3_mark.value : 1303,
    LocationNames.COVE_Boss2_1_mark.value : 1304,
    LocationNames.COVE_Boss2_2_mark.value : 1305,
    LocationNames.COVE_Boss2_3_mark.value : 1306,
    LocationNames.COVE_Level_1.value : 1307,
    LocationNames.COVE_Level_2.value : 1308,
    LocationNames.COVE_Level_3.value : 1309,
    LocationNames.COVE_Level_4.value : 1310,
    LocationNames.COVE_Level_5.value : 1311,
    LocationNames.COVE_Level_6.value : 1312,
    LocationNames.COVE_Level_7.value : 1313,
    #1400: Farm locations
    #1500: Court locations
    #1600: Shieldbreaker locations
    #1700: Darkest Dungeon locations
    LocationNames.DD_FinalQuest_1.value : 1701,
    LocationNames.DD_FinalQuest_2.value : 1702,
    LocationNames.DD_FinalQuest_3.value : 1703,
    #LocationNames.DD_FinalQuest_4.value : 1704,
    #1800: Event locations
    LocationNames.RUINS_Boss1_1.value : 1801,
    LocationNames.RUINS_Boss1_2.value : 1802,
    LocationNames.RUINS_Boss1_3.value : 1803,
    LocationNames.RUINS_Boss2_1.value : 1804,
    LocationNames.RUINS_Boss2_2.value : 1805,
    LocationNames.RUINS_Boss2_3.value : 1806,
    LocationNames.WARRENS_Boss1_1.value : 1807,
    LocationNames.WARRENS_Boss1_2.value : 1808,
    LocationNames.WARRENS_Boss1_3.value : 1809,
    LocationNames.WARRENS_Boss2_1.value : 1810,
    LocationNames.WARRENS_Boss2_2.value : 1811,
    LocationNames.WARRENS_Boss2_3.value : 1812,
    LocationNames.WEALD_Boss1_1.value : 1813,
    LocationNames.WEALD_Boss1_2.value : 1814,
    LocationNames.WEALD_Boss1_3.value : 1815,
    LocationNames.WEALD_Boss2_1.value : 1816,
    LocationNames.WEALD_Boss2_2.value : 1817,
    LocationNames.WEALD_Boss2_3.value : 1818,
    LocationNames.COVE_Boss1_1.value : 1819,
    LocationNames.COVE_Boss1_2.value : 1820,
    LocationNames.COVE_Boss1_3.value : 1821,
    LocationNames.COVE_Boss2_1.value : 1822,
    LocationNames.COVE_Boss2_2.value : 1823,
    LocationNames.COVE_Boss2_3.value : 1824,
    }

class DarkestDungeonLocation(Location):
    game = "Darkest Dungeon"


def get_location_names_with_IDs(location_names : list[str]) -> dict[str, int | None]:
    return {location_name : LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def get_location_names_by_range(start : int, end : int) -> dict[str, int | None]:
    d = {key:value for key, value in LOCATION_NAME_TO_ID.items() if value >= start and value < end}
    return d

def create_locations(world : "DarkestDungeonWorld"):
    create_normal_locations(world);
    create_event_locations(world);
    pass;

def create_normal_locations(world : "DarkestDungeonWorld"):
    world.get_region(RegionNames.HAMLET.value).add_locations(get_location_names_by_range(1, 100));
    world.get_region(RegionNames.QUEST_GOALS.value).add_locations(get_location_names_by_range(101, 200))
    world.get_region(RegionNames.ABBEY.value).add_locations(get_location_names_by_range(201, 300))
    world.get_region(RegionNames.BLACKSMITH.value).add_locations(get_location_names_by_range(301, 400))
    world.get_region(RegionNames.GUILD.value).add_locations(get_location_names_by_range(401, 500))
    world.get_region(RegionNames.NOMAD_WAGON.value).add_locations(get_location_names_by_range(501, 600))
    world.get_region(RegionNames.SANITARIUM.value).add_locations(get_location_names_by_range(601, 700))
    world.get_region(RegionNames.STAGECOACH.value).add_locations(get_location_names_by_range(701, 800))
    world.get_region(RegionNames.SURVIVALIST.value).add_locations(get_location_names_by_range(801, 900))
    world.get_region(RegionNames.TAVERN.value).add_locations(get_location_names_by_range(901, 1000))
    world.get_region(RegionNames.RUINS.value).add_locations(get_location_names_by_range(1001, 1100))
    world.get_region(RegionNames.WARRENS.value).add_locations(get_location_names_by_range(1101, 1200))
    world.get_region(RegionNames.WEALD.value).add_locations(get_location_names_by_range(1201, 1300))
    world.get_region(RegionNames.COVE.value).add_locations(get_location_names_by_range(1301, 1400))
    world.get_region(RegionNames.DARKEST.value).add_locations(get_location_names_by_range(1701, 1800))


def create_event_locations(world : "DarkestDungeonWorld"):
    world.get_region(RegionNames.RUINS.value).add_event(LocationNames.RUINS_Boss1_1.value,ItemNames.RUINS_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.RUINS.value).add_event(LocationNames.RUINS_Boss1_2.value,ItemNames.RUINS_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.RUINS.value).add_event(LocationNames.RUINS_Boss1_3.value,ItemNames.RUINS_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.RUINS.value).add_event(LocationNames.RUINS_Boss2_1.value,ItemNames.RUINS_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.RUINS.value).add_event(LocationNames.RUINS_Boss2_2.value,ItemNames.RUINS_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.RUINS.value).add_event(LocationNames.RUINS_Boss2_3.value,ItemNames.RUINS_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WARRENS.value).add_event(LocationNames.WARRENS_Boss1_1.value,ItemNames.WARRENS_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WARRENS.value).add_event(LocationNames.WARRENS_Boss1_2.value,ItemNames.WARRENS_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WARRENS.value).add_event(LocationNames.WARRENS_Boss1_3.value,ItemNames.WARRENS_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WARRENS.value).add_event(LocationNames.WARRENS_Boss2_1.value,ItemNames.WARRENS_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WARRENS.value).add_event(LocationNames.WARRENS_Boss2_2.value,ItemNames.WARRENS_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WARRENS.value).add_event(LocationNames.WARRENS_Boss2_3.value,ItemNames.WARRENS_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WEALD.value).add_event(LocationNames.WEALD_Boss1_1.value,ItemNames.WEALD_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WEALD.value).add_event(LocationNames.WEALD_Boss1_2.value,ItemNames.WEALD_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WEALD.value).add_event(LocationNames.WEALD_Boss1_3.value,ItemNames.WEALD_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WEALD.value).add_event(LocationNames.WEALD_Boss2_1.value,ItemNames.WEALD_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WEALD.value).add_event(LocationNames.WEALD_Boss2_2.value,ItemNames.WEALD_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.WEALD.value).add_event(LocationNames.WEALD_Boss2_3.value,ItemNames.WEALD_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.COVE.value).add_event(LocationNames.COVE_Boss1_1.value,ItemNames.COVE_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.COVE.value).add_event(LocationNames.COVE_Boss1_2.value,ItemNames.COVE_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.COVE.value).add_event(LocationNames.COVE_Boss1_3.value,ItemNames.COVE_BOSS1_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.COVE.value).add_event(LocationNames.COVE_Boss2_1.value,ItemNames.COVE_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.COVE.value).add_event(LocationNames.COVE_Boss2_2.value,ItemNames.COVE_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.COVE.value).add_event(LocationNames.COVE_Boss2_3.value,ItemNames.COVE_BOSS2_TROPHY_PROG.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)
    world.get_region(RegionNames.DARKEST.value).add_event(LocationNames.DD_FinalQuest_4.value, ItemNames.VICTORY.value,location_type=DarkestDungeonLocation,item_type=DarkestDungeonItem)

