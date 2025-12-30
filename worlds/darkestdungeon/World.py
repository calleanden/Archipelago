
from worlds.AutoWorld import World
from . import Options, Items, Locations, Regions, Rules, Types, WebWorld

class DarkestDungeonWorld(World):
    """
    Darkest Dungeon is a challenging gothic roguelike turn-based RPG about the psychological stresses of adventuring. Can you keep your heroes together when all hope is lost? 
    """

    game = "Darkest Dungeon"
    options : Options.DarkestDungeonOptions
    options_dataclass = Options.DarkestDungeonOptions
    item_name_to_id = Items.ITEM_NAME_TO_ID
    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    origin_region_name = Types.RegionNames.HAMLET.value;
    web_world = WebWorld.DarkestDungeonWebWorld()

    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self);
        Locations.create_locations(self);

    def set_rules(self):
        Rules.set_all_rules(self);

    def create_items(self):
        Items.create_all_items(self);

    def create_item(self, name : str) -> Items.DarkestDungeonItem:
        return Items.create_item_with_correct_classification(self, name);

    def get_filler_item_name(self):
        return Items.get_random_filler_name(self);
