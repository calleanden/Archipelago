from BaseClasses import Location, Region
from typing import TYPE_CHECKING
from .Types import DLCNames, RegionNames, LocationNames, ItemNames
from .CustomDataClasses import DDLocationData, DDRegionData

if TYPE_CHECKING:
    from . import DarkestDungeonWorld

MIN_FIRST_SPHERE_LOCATIONS = 20


class DarkestDungeonRegion(Region):

    def __init__(self, data : DDRegionData, world : "DarkestDungeonWorld", hint = None):
        self.data = data
        super().__init__(data.name, world.player, world.multiworld, hint)
   

region_list = [
    DDRegionData(RegionNames.HAMLET.value,location_data=[
        DDLocationData(LocationNames.Quests_0.value, default_item=ItemNames.RUINS_KEY.value,use_default=True)
        ]),
    DDRegionData(RegionNames.ABBEY.value,location_data=[
        DDLocationData(LocationNames.Abbey_Cloister_1.value,default_item=ItemNames.ABBEY_CLOISTER_PROG.value),
        DDLocationData(LocationNames.Abbey_Cloister_2.value,default_item=ItemNames.ABBEY_CLOISTER_PROG.value),
        DDLocationData(LocationNames.Abbey_Cloister_3.value,default_item=ItemNames.ABBEY_CLOISTER_PROG.value),
        DDLocationData(LocationNames.Abbey_Cloister_4.value,default_item=ItemNames.ABBEY_CLOISTER_PROG.value),
        DDLocationData(LocationNames.Abbey_Cloister_5.value,default_item=ItemNames.ABBEY_CLOISTER_PROG.value),
        DDLocationData(LocationNames.Abbey_Cloister_6.value,default_item=ItemNames.ABBEY_CLOISTER_PROG.value),
        ]),
    DDRegionData(RegionNames.BLACKSMITH.value,location_data=[
        DDLocationData(LocationNames.Blacksmith_Weaponsmithing_1.value, default_item = ItemNames.BLACKSMITH_WEAPONSMITHING.value)
        ]),
    DDRegionData(RegionNames.GUILD.value),
    DDRegionData(RegionNames.NOMAD_WAGON.value),
    DDRegionData(RegionNames.SANITARIUM.value),
    DDRegionData(RegionNames.STAGECOACH.value),
    DDRegionData(RegionNames.SURVIVALIST.value),
    DDRegionData(RegionNames.TAVERN.value),
    DDRegionData(RegionNames.RUINS.value,location_data=[
        DDLocationData(LocationNames.Ruins_Level_1.value, default_item=ItemNames.RUINS_NECRO_KEY_1.value),
        DDLocationData(LocationNames.Ruins_Necromancer_1.value, default_item=ItemNames.RUINS_NECRO_TROPHY_1.value),
        DDLocationData(LocationNames.Ruins_Necromancer_1_mark.value, default_item=ItemNames.DD_MARK.value)
        ]),
    DDRegionData(RegionNames.WEALD.value),
    DDRegionData(RegionNames.WARRENS.value),
    DDRegionData(RegionNames.COVE.value),
    DDRegionData(RegionNames.DARKEST.value,location_data=[
        DDLocationData(LocationNames.DD_FinalQuest_1.value),
        DDLocationData(LocationNames.DD_FinalQuest_2.value),
        DDLocationData(LocationNames.DD_FinalQuest_3.value),
        DDLocationData(LocationNames.DD_FinalQuest_4.value),
        ]),
    DDRegionData(RegionNames.COURT.value, dlc=DLCNames.CC.value),
    DDRegionData(RegionNames.FARM.value, dlc=DLCNames.COM.value),
    DDRegionData(RegionNames.QUEST_GOALS.value, location_data=[
        DDLocationData(LocationNames.Quests_0_ST.value, default_item=ItemNames.STAGECOACH_KEY.value),
        DDLocationData(LocationNames.Quests_0_NW.value, default_item=ItemNames.NOMAD_WAGON_KEY.value),
        DDLocationData(LocationNames.Quests_0_RU.value, default_item=ItemNames.RUINS_KEY.value),
        DDLocationData(LocationNames.Quests_0_DD.value, default_item=ItemNames.DARKEST_KEY.value),
        DDLocationData(LocationNames.Quests_1_AB.value, default_item=ItemNames.ABBEY_KEY.value),
        DDLocationData(LocationNames.Quests_1_TA.value, default_item=ItemNames.TAVERN_KEY.value),
        DDLocationData(LocationNames.Quests_1_FS.value, dlc=DLCNames.COM, default_item=ItemNames.FARMSTEAD_KEY.value),
        DDLocationData(LocationNames.Quests_2_BS.value, default_item=ItemNames.BLACKSMITH_KEY.value),
        DDLocationData(LocationNames.Quests_2_GU.value, default_item=ItemNames.GUILD_KEY.value),
        DDLocationData(LocationNames.Quests_2_WE.value, default_item=ItemNames.WEALD_KEY.value),
        DDLocationData(LocationNames.Quests_3_CO.value, default_item=ItemNames.COVE_KEY.value),
        DDLocationData(LocationNames.Quests_3_SA.value, default_item=ItemNames.SANITARIUM_KEY.value),
        DDLocationData(LocationNames.Quests_3_WA.value, default_item=ItemNames.WARRENS_KEY.value)
        ])
]

region_dictionary = {data.name : data for data in region_list}