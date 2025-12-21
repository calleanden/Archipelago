from email.policy import default
import gc
from BaseClasses import Item, ItemClassification, Tutorial, Location, MultiWorld
from worlds.AutoWorld import World, WebWorld, CollectionState
from worlds.generic.Rules import CollectionRule, ItemRule, add_item_rule, add_rule
from .CustomDataClasses import DDItemData, DDRegionData
from .Items import DarkestDungeonItem, item_list, item_dictionary
from .Regions import DarkestDungeonRegion, region_list, region_dictionary
from .Locations import DarkestDungeonLocation
from .Options import DarkestDungeonOptions
from .Types import RegionNames, LocationNames, ItemNames, DLCNames
from typing import List, Dict, TextIO, cast
from worlds.LauncherComponents import Component, components, icon_paths, launch as launch_component, Type
from Utils import local_path
from BaseClasses import CollectionState, Region, Location, Item, Entrance
from random import choice

class DarkestDungeonWebWorld(WebWorld):
    theme = "stone"
    tutorials = [
        Tutorial(
            "Darkest Dungeon Archipelago Setup Guide",
            "A guide for setting up Darkest Dungeon to be played in Archipelago",
            "English",
            "dd_en.md",
            "setup/en",
            ["Sungrass"]
        )
    ]


class DarkestDungeonWorld(World):
    """
    Darkest Dungeon is a challenging gothic roguelike turn-based RPG about the psychological stresses of adventuring. Can you keep your heroes together when all hope is lost? 
    """

    game = "Darkest Dungeon"
    options : DarkestDungeonOptions
    options_dataclass = DarkestDungeonOptions
    item_name_to_id = {data.name: data.address for data in item_list}
    location_name_to_id = {location.name : location.address for region in region_list for location in region.location_data}
    origin_region_name = RegionNames.MENU.value
    web_world = DarkestDungeonWebWorld()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def get_filler_item_name(self) -> str:
        filler_items = [item for item in item_list if item.classification == ItemClassification.filler]
        return choice(filler_items)

    def generate_early(self):
        self.created_regions = set()
        pass

    def create_region(self, data : DDRegionData):
        r = DarkestDungeonRegion(data, self)

        for location_data in data.location_data:
            location = DarkestDungeonLocation(self.player, location_data, r)
            r.locations.append(location)
        
        self.multiworld.regions.append(r)
        self.created_regions.add(r.name)
        return r


    def create_regions(self):
        regions = dict()
        regions[RegionNames.MENU.value] = self.create_region(DDRegionData(RegionNames.MENU.value,location_data=[]))
        for r in region_list:
            if r.dlc == DLCNames.NONE.value or (self.options.enable_CC_DLC and r.dlc == DLCNames.CC.value) or (self.options.enable_CoM_DLC and r.dlc == DLCNames.COM.value) or (self.options.enable_SB_DLC and r.dlc == DLCNames.SB.value):
                regions[r.name] = self.create_region(r)

        def create_connection(from_region : str, to_region : str):
            connection = Entrance(self.player, "{} Gate".format(to_region), regions[from_region])
            regions[from_region].exits.append(connection)
            connection.connect(regions[to_region])

        regions[RegionNames.MENU].exits.append(Entrance(self.player, "New Game",regions[RegionNames.MENU]))
        self.multiworld.get_entrance("New Game", self.player).connect(regions[RegionNames.HAMLET.value])

        create_connection(RegionNames.HAMLET.value, RegionNames.ABBEY.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.BLACKSMITH.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.GUILD.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.NOMAD_WAGON.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.SANITARIUM.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.STAGECOACH.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.SURVIVALIST.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.TAVERN.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.RUINS.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.WEALD.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.WARRENS.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.COVE.value)
        create_connection(RegionNames.HAMLET.value, RegionNames.DARKEST.value)        
        create_connection(RegionNames.HAMLET.value, RegionNames.QUEST_GOALS.value)
        
        if self.options.enable_CC_DLC:
            create_connection(RegionNames.HAMLET.value, RegionNames.COURT.value)
        
        if self.options.enable_CoM_DLC:
            create_connection(RegionNames.HAMLET.value, RegionNames.FARM.value)

        self.multiworld.completion_condition[self.player] = lambda state : state.has(ItemNames.RUINS_NECRO_TROPHY_1.value,self.player)

    def create_item(self, name: str) -> DarkestDungeonItem:
        data = item_dictionary[name]
        return DarkestDungeonItem(data.name, data, self.player)

    def create_items(self):
        item_set = set()

        local_itempool = []
        extra_items = 0

        for location in cast(List[DarkestDungeonLocation], self.multiworld.get_unfilled_locations(self.player)):
            default_item_name : str = location.data.default_item
            item : DDItemData = item_dictionary[default_item_name]
            if location.data.use_default:
                location.place_locked_item(self.create_item(item.name))
            else:
                if not item.is_unique():
                    local_itempool.append(self.create_item(default_item_name))
                else:
                    if default_item_name in item_set:
                        extra_items += 1
                    else:
                        item_set.add(default_item_name)
                        local_itempool.append(self.create_item(default_item_name))
        
        self.multiworld.itempool += local_itempool

    def _add_entrance_rule(self, region : str, rule : List, strict : bool = False):
        assert region in RegionNames
        if region not in self.created_regions: return
        if strict: 
            rule_lambda : CollectionRule = lambda state, item=rule: state.has_all(item, self.player)
        else:
            rule_lambda : CollectionRule = lambda state, item=rule: state.has_any(item, self.player)
        add_rule(self.multiworld.get_entrance("{} Gate".format(region), self.player), rule_lambda)

    def _add_item_rule(self, location : str, rule : ItemRule):
        add_item_rule(self.multiworld.get_location(location, self.player), rule)

    def _add_location_rule(self, region : str, location : str, rule : str):
        data = region_dictionary[region].location_dictionary()[location]
        valid_location = True
        match data.dlc:
            case DLCNames.CC.value:
                if self.options.enable_CC_DLC == False:
                    valid_location = False
            case DLCNames.COM.value:
                if self.options.enable_CoM_DLC == False:
                    valid_location = False
            case DLCNames.SB.value:
                if self.options.enable_SB_DLC == False:
                    valid_location = False
        if (valid_location):
            rule = lambda state, item=rule: state.has(item, self.player)
            add_rule(self.multiworld.get_location(location, self.player), rule)
            
    def set_rules(self):
        self._add_entrance_rule(RegionNames.RUINS.value, [ItemNames.RUINS_KEY.value])
        self._add_entrance_rule(RegionNames.WEALD.value, [ItemNames.WEALD_KEY.value])
        self._add_entrance_rule(RegionNames.COVE.value, [ItemNames.COVE_KEY.value])
        self._add_entrance_rule(RegionNames.WARRENS.value, [ItemNames.WARRENS_KEY.value])
        self._add_entrance_rule(RegionNames.DARKEST.value, [ItemNames.DARKEST_KEY.value])
        self._add_entrance_rule(RegionNames.ABBEY.value,[ItemNames.ABBEY_KEY.value])
        self._add_entrance_rule(RegionNames.BLACKSMITH.value, [ItemNames.BLACKSMITH_KEY.value])
        self._add_entrance_rule(RegionNames.GUILD.value, [ItemNames.GUILD_KEY.value])
        self._add_entrance_rule(RegionNames.NOMAD_WAGON.value, [ItemNames.NOMAD_WAGON_KEY.value])
        self._add_entrance_rule(RegionNames.SANITARIUM.value, [ItemNames.SANITARIUM_KEY.value])
        self._add_entrance_rule(RegionNames.STAGECOACH.value, [ItemNames.STAGECOACH_KEY.value])
        self._add_entrance_rule(RegionNames.SURVIVA LIST.value, [ItemNames.SURVIVALIST_KEY.value])
        self._add_entrance_rule(RegionNames.TAVERN.value, [ItemNames.TAVERN_KEY.value])
        self._add_entrance_rule(RegionNames.QUEST_GOALS.value, [ItemNames.RUINS_KEY.value, ItemNames.WEALD_KEY.value, ItemNames.COVE_KEY.value, ItemNames.WARRENS_KEY.value, ItemNames.DARKEST_KEY.value])

        self._add_location_rule(RegionNames.RUINS, LocationNames.Ruins_Necromancer_1.value,ItemNames.RUINS_NECRO_KEY_1.value)

    def fill_slot_data(self) -> dict:

        slot_data = ""
        return slot_data

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        new_hint_data = {}
        hint_data[self.player] = new_hint_data

    def write_spoiler_header(self, spoiler_handle: TextIO):
        pass