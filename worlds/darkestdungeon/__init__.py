from BaseClasses import Item, ItemClassification, Tutorial, Location, MultiWorld

from worlds.AutoWorld import World, WebWorld, CollectionState
from worlds.generic.Rules import add_rule
from Items import base_id, item_table
from Types import DDItem, DDLocation
from Locations import location_names
from typing import List, Dict, TextIO
from worlds.LauncherComponents import Component, components, icon_paths, launch as launch_component, Type
from Utils import local_path


def launch_client():
    pass


components.append(Component("Darkest Dungeon Client", "DDClient", func=launch_client,
                            component_type=Type.CLIENT, icon=''))

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
    item_name_to_id = {item["name"] : (base_id + index) for index, item in enumerate(item_table)}
    location_name_to_id = {location_names["name"] : (base_id + index) for index, item in enumerate(location_names)}
    web_world = DarkestDungeonWebWorld()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def get_filler_item_name(self) -> str:
        pass
        #return self.random.choices(list(junk_weights.keys()), weights=junk_weights.values(), k=1)[0]

    def generate_early(self):
        pass

    def create_regions(self):
        multiworld = self.multiworld
        
        multiworld.completion_condition[self.player] = lambda state : state.has("Brewer's License",self.player)

    def create_items(self):
        pass

    def set_rules(self):
        pass

    def create_item(self, name: str) -> DDItem:
        item_id : int = self.item_name_to_id[name]
        id = item_id - base_id
        return DDItem(name, item_table[id]["classification"], item_id, player=self.player)

    def fill_slot_data(self) -> dict:

        slot_data = ""
        return slot_data

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        new_hint_data = {}
        hint_data[self.player] = new_hint_data

    def write_spoiler_header(self, spoiler_handle: TextIO):
        pass

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        pass

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        pass

