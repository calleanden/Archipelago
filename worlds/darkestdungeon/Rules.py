from typing import TYPE_CHECKING

from BaseClasses import CollectionState, Mapping
from .Types import EntranceNames, ItemNames, LocationNames, RegionNames
from .Locations import get_location_names_by_range
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .World import DarkestDungeonWorld

def set_all_rules(world : "DarkestDungeonWorld"):
    set_entrance_rules(world);
    set_location_rules(world);
    set_win_condition(world);


def set_entrance_rules(world: "DarkestDungeonWorld"):

    trophies = [
        ItemNames.RUINS_BOSS1_TROPHY_PROG.value, ItemNames.RUINS_BOSS2_TROPHY_PROG.value,
        ItemNames.WARRENS_BOSS1_TROPHY_PROG.value, ItemNames.WARRENS_BOSS2_TROPHY_PROG.value,
        ItemNames.WEALD_BOSS1_TROPHY_PROG.value, ItemNames.WEALD_BOSS2_TROPHY_PROG.value,
        ItemNames.COVE_BOSS1_TROPHY_PROG.value, ItemNames.COVE_BOSS2_TROPHY_PROG.value
        ]
    goal_trophies = []
    trophyCount = world.options.trophy_requirement.value;
    marks = world.options.mark_requirement.value

    for i in range(trophyCount):
            goal_trophies.append(world.random.choice(trophies))

    goal_trophies_set = list(set(goal_trophies))
    goal_trophy_counts = {goal : goal_trophies.count(goal) for goal in goal_trophies_set}
    #print(goal_trophy_counts)

    hamlet = world.get_region(RegionNames.HAMLET.value)
    darkest = world.get_region(RegionNames.DARKEST.value)
    hamlet.connect(darkest,EntranceNames.DARKEST_GATE.value, lambda state : state.has(ItemNames.DARKEST_KEY.value, world.player) and state.has(ItemNames.DD_MARK.value, world.player, marks) and state.has_all_counts(goal_trophy_counts, world.player))
    


def set_location_rules(world: "DarkestDungeonWorld"):

    def can_earn_heirlooms(state : CollectionState):
        return state.has_any([ItemNames.RUINS_KEY.value, ItemNames.WARRENS_KEY.value, ItemNames.WEALD_KEY.value, ItemNames.COVE_KEY.value], world.player);

    add_rule(world.get_location(LocationNames.RUINS_Boss1_1.value), lambda state : state.has(ItemNames.RUINS_BOSS1_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.RUINS_Boss1_2.value), lambda state : state.has(ItemNames.RUINS_BOSS1_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.RUINS_Boss1_3.value), lambda state : state.has(ItemNames.RUINS_BOSS1_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.RUINS_Boss2_1.value), lambda state : state.has(ItemNames.RUINS_BOSS2_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.RUINS_Boss2_2.value), lambda state : state.has(ItemNames.RUINS_BOSS2_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.RUINS_Boss2_3.value), lambda state : state.has(ItemNames.RUINS_BOSS2_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.WARRENS_Boss1_1.value), lambda state : state.has(ItemNames.WARRENS_BOSS1_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.WARRENS_Boss1_2.value), lambda state : state.has(ItemNames.WARRENS_BOSS1_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.WARRENS_Boss1_3.value), lambda state : state.has(ItemNames.WARRENS_BOSS1_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.WARRENS_Boss2_1.value), lambda state : state.has(ItemNames.WARRENS_BOSS2_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.WARRENS_Boss2_2.value), lambda state : state.has(ItemNames.WARRENS_BOSS2_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.WARRENS_Boss2_3.value), lambda state : state.has(ItemNames.WARRENS_BOSS2_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.WEALD_Boss1_1.value), lambda state : state.has(ItemNames.WEALD_BOSS1_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.WEALD_Boss1_2.value), lambda state : state.has(ItemNames.WEALD_BOSS1_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.WEALD_Boss1_3.value), lambda state : state.has(ItemNames.WEALD_BOSS1_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.WEALD_Boss2_1.value), lambda state : state.has(ItemNames.WEALD_BOSS2_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.WEALD_Boss2_2.value), lambda state : state.has(ItemNames.WEALD_BOSS2_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.WEALD_Boss2_3.value), lambda state : state.has(ItemNames.WEALD_BOSS2_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.COVE_Boss1_1.value), lambda state : state.has(ItemNames.COVE_BOSS1_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.COVE_Boss1_2.value), lambda state : state.has(ItemNames.COVE_BOSS1_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.COVE_Boss1_3.value), lambda state : state.has(ItemNames.COVE_BOSS1_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.COVE_Boss2_1.value), lambda state : state.has(ItemNames.COVE_BOSS2_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.COVE_Boss2_2.value), lambda state : state.has(ItemNames.COVE_BOSS2_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.COVE_Boss2_3.value), lambda state : state.has(ItemNames.COVE_BOSS2_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.RUINS_Boss1_1_mark.value), lambda state : state.has(ItemNames.RUINS_BOSS1_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.RUINS_Boss1_2_mark.value), lambda state : state.has(ItemNames.RUINS_BOSS1_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.RUINS_Boss1_3_mark.value), lambda state : state.has(ItemNames.RUINS_BOSS1_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.RUINS_Boss2_1_mark.value), lambda state : state.has(ItemNames.RUINS_BOSS2_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.RUINS_Boss2_2_mark.value), lambda state : state.has(ItemNames.RUINS_BOSS2_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.RUINS_Boss2_3_mark.value), lambda state : state.has(ItemNames.RUINS_BOSS2_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.WARRENS_Boss1_1_mark.value), lambda state : state.has(ItemNames.WARRENS_BOSS1_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.WARRENS_Boss1_2_mark.value), lambda state : state.has(ItemNames.WARRENS_BOSS1_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.WARRENS_Boss1_3_mark.value), lambda state : state.has(ItemNames.WARRENS_BOSS1_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.WARRENS_Boss2_1_mark.value), lambda state : state.has(ItemNames.WARRENS_BOSS2_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.WARRENS_Boss2_2_mark.value), lambda state : state.has(ItemNames.WARRENS_BOSS2_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.WARRENS_Boss2_3_mark.value), lambda state : state.has(ItemNames.WARRENS_BOSS2_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.WEALD_Boss1_1_mark.value), lambda state : state.has(ItemNames.WEALD_BOSS1_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.WEALD_Boss1_2_mark.value), lambda state : state.has(ItemNames.WEALD_BOSS1_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.WEALD_Boss1_3_mark.value), lambda state : state.has(ItemNames.WEALD_BOSS1_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.WEALD_Boss2_1_mark.value), lambda state : state.has(ItemNames.WEALD_BOSS2_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.WEALD_Boss2_2_mark.value), lambda state : state.has(ItemNames.WEALD_BOSS2_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.WEALD_Boss2_3_mark.value), lambda state : state.has(ItemNames.WEALD_BOSS2_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.COVE_Boss1_1_mark.value), lambda state : state.has(ItemNames.COVE_BOSS1_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.COVE_Boss1_2_mark.value), lambda state : state.has(ItemNames.COVE_BOSS1_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.COVE_Boss1_3_mark.value), lambda state : state.has(ItemNames.COVE_BOSS1_KEY_PROG.value, world.player, count = 3))
    add_rule(world.get_location(LocationNames.COVE_Boss2_1_mark.value), lambda state : state.has(ItemNames.COVE_BOSS2_KEY_PROG.value, world.player, count = 1))
    add_rule(world.get_location(LocationNames.COVE_Boss2_2_mark.value), lambda state : state.has(ItemNames.COVE_BOSS2_KEY_PROG.value, world.player, count = 2))
    add_rule(world.get_location(LocationNames.COVE_Boss2_3_mark.value), lambda state : state.has(ItemNames.COVE_BOSS2_KEY_PROG.value, world.player, count = 3))
    
    upgrade_locations = get_location_names_by_range(101, 1000);
    upgrade_loc_names = list(upgrade_locations.keys());
    for name in upgrade_loc_names:
        add_rule(world.get_location(name), can_earn_heirlooms)

    if world.options.open_dungeon:
        add_rule(world.get_location(LocationNames.DD_FinalQuest_4.value), lambda state : state.has_all([ItemNames.DD_FINAL_QUEST_ITEM_1.value, ItemNames.DD_FINAL_QUEST_ITEM_2.value, ItemNames.DD_FINAL_QUEST_ITEM_3.value]));

def set_win_condition(world: "DarkestDungeonWorld"):
    world.multiworld.completion_condition[world.player] = lambda state : state.has(ItemNames.VICTORY.value, world.player);