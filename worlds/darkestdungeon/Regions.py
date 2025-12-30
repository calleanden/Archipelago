from BaseClasses import Location, Region, Entrance
from typing import TYPE_CHECKING
from .Types import DLCNames, RegionNames, ItemNames, EntranceNames

if TYPE_CHECKING:
    from . import DarkestDungeonWorld

MIN_FIRST_SPHERE_LOCATIONS = 20

def create_and_connect_regions(world: "DarkestDungeonWorld"):
    create_regions(world);
    connect_regions(world);

def create_regions(world: "DarkestDungeonWorld"):
    hamlet = Region(RegionNames.HAMLET.value, world.player, world.multiworld)
    abbey = Region(RegionNames.ABBEY.value, world.player, world.multiworld)
    blacksmith = Region(RegionNames.BLACKSMITH.value, world.player, world.multiworld)
    guild = Region(RegionNames.GUILD.value, world.player, world.multiworld)
    nomad_wagon = Region(RegionNames.NOMAD_WAGON.value, world.player, world.multiworld)
    sanitarium = Region(RegionNames.SANITARIUM.value, world.player, world.multiworld)
    stagecoach = Region(RegionNames.STAGECOACH.value, world.player, world.multiworld)
    survivalist = Region(RegionNames.SURVIVALIST.value, world.player, world.multiworld)
    tavern = Region(RegionNames.TAVERN.value, world.player, world.multiworld)
    ruins = Region(RegionNames.RUINS.value, world.player, world.multiworld)
    weald = Region(RegionNames.WEALD.value, world.player, world.multiworld)
    warrens = Region(RegionNames.WARRENS.value, world.player, world.multiworld)
    cove = Region(RegionNames.COVE.value, world.player, world.multiworld)
    darkest = Region(RegionNames.DARKEST.value, world.player, world.multiworld)
    farm = Region(RegionNames.FARM.value, world.player, world.multiworld)
    court = Region(RegionNames.COURT.value, world.player, world.multiworld)
    quest_goals = Region(RegionNames.QUEST_GOALS.value, world.player, world.multiworld)

    
    regions = [hamlet, abbey, blacksmith, guild, nomad_wagon, sanitarium, stagecoach, survivalist, tavern, ruins, weald, warrens, cove, darkest, quest_goals]

    if world.options.enable_CC_DLC:
        regions.append(court)

    if world.options.enable_CoM_DLC:
        regions.append(farm)

    world.multiworld.regions += regions

def connect_regions(world: "DarkestDungeonWorld"):
    hamlet = world.get_region(RegionNames.HAMLET.value)
    abbey = world.get_region(RegionNames.ABBEY.value)
    blacksmith = world.get_region(RegionNames.BLACKSMITH.value)
    guild = world.get_region(RegionNames.GUILD.value)
    nomad_wagon = world.get_region(RegionNames.NOMAD_WAGON.value)
    sanitarium = world.get_region(RegionNames.SANITARIUM.value)
    stagecoach = world.get_region(RegionNames.STAGECOACH.value)
    survivalist = world.get_region(RegionNames.SURVIVALIST.value)
    tavern = world.get_region(RegionNames.TAVERN.value)
    ruins = world.get_region(RegionNames.RUINS.value)
    weald = world.get_region(RegionNames.WEALD.value)
    warrens = world.get_region(RegionNames.WARRENS.value)
    cove = world.get_region(RegionNames.COVE.value)
    darkest = world.get_region(RegionNames.DARKEST.value)
    if world.options.enable_CoM_DLC:
        farm = world.get_region(RegionNames.FARM.value)
    if world.options.enable_CC_DLC:
        court = world.get_region(RegionNames.COURT.value)
    quest_goals = world.get_region(RegionNames.QUEST_GOALS.value)

    hamlet.connect(abbey, EntranceNames.ABBEY_GATE.value, lambda state: state.has(ItemNames.ABBEY_KEY.value, world.player))
    hamlet.connect(blacksmith, EntranceNames.BLACKSMITH_GATE.value, lambda state: state.has(ItemNames.BLACKSMITH_KEY.value, world.player))
    hamlet.connect(guild, EntranceNames.GUILD_GATE.value, lambda state: state.has(ItemNames.GUILD_KEY.value, world.player))
    hamlet.connect(nomad_wagon, EntranceNames.NOMAD_WAGON_GATE.value, lambda state: state.has(ItemNames.NOMAD_WAGON_KEY.value, world.player))
    hamlet.connect(sanitarium, EntranceNames.SANITARIUM_GATE.value, lambda state: state.has(ItemNames.SANITARIUM_KEY.value, world.player))
    hamlet.connect(stagecoach, EntranceNames.STAGECOACH_GATE.value, lambda state: state.has(ItemNames.STAGECOACH_KEY.value, world.player))
    hamlet.connect(survivalist, EntranceNames.SURVIVALIST_GATE.value, lambda state: state.has(ItemNames.SURVIVALIST_KEY.value, world.player))
    hamlet.connect(tavern, EntranceNames.TAVERN_GATE.value, lambda state: state.has(ItemNames.TAVERN_KEY.value, world.player))
    hamlet.connect(ruins, EntranceNames.RUINS_GATE.value, lambda state: state.has(ItemNames.RUINS_KEY.value, world.player))
    hamlet.connect(weald, EntranceNames.WEALD_GATE.value, lambda state: state.has(ItemNames.WEALD_KEY.value, world.player))
    hamlet.connect(warrens, EntranceNames.WARRENS_GATE.value, lambda state: state.has(ItemNames.WARRENS_KEY.value, world.player))
    hamlet.connect(cove, EntranceNames.COVE_GATE.value, lambda state: state.has(ItemNames.COVE_KEY.value, world.player))
    hamlet.connect(quest_goals, EntranceNames.QUEST_GOALS_GATE, lambda state: state.has_any([ItemNames.RUINS_KEY.value,ItemNames.WEALD_KEY.value, ItemNames.WARRENS_KEY.value, ItemNames.COVE_KEY], world.player))
    if world.options.enable_CC_DLC:
        hamlet.connect(court, EntranceNames.COURT_GATE.value, lambda state: state.has(ItemNames.COURT_KEY.value, world.player))
    if world.options.enable_CoM_DLC: 
        hamlet.connect(farm, EntranceNames.FARM_GATE.value, lambda state: state.has(ItemNames.FARMSTEAD_KEY.value, world.player))


 