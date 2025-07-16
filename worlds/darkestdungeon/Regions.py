from BaseClasses import Region, Entrance, ItemClassification, Location, LocationProgressType
from typing import TYPE_CHECKING, List, Dict, Optional
from .Types import RegionIndex

if TYPE_CHECKING:
    from . import DarkestDungeonWorld

MIN_FIRST_SPHERE_LOCATIONS = 20

region_list = {
    RegionIndex.OLD_ROAD: "The Old Road",
    RegionIndex.HAMLET : "The Hamlet",
    RegionIndex.ABBEY : "The Hamlet - Abbey",
    RegionIndex.BLACKSMITH : "The Hamlet - Blacksmith",
    RegionIndex.GUILD : "The Hamlet - Guild",
    RegionIndex.NOMAD_WAGON : "The Hamlet - Nomad Wagon",
    RegionIndex.SANITARIUM : "The Hamlet - Sanitarium",
    RegionIndex.STAGECOACH : "The Hamlet - Stagecoach",
    RegionIndex.SURVIVALIST : "The Hamlet - Survivalist",
    RegionIndex.TAVERN : "The Hamlet - Tavern",
    RegionIndex.RUINS : "The Ruins",
    RegionIndex.WEALD : "The Weald",
    RegionIndex.WARRENS : "The Warrens",
    RegionIndex.COVE : "The Cove",
    RegionIndex.DARKEST : "The Darkest Dungeon",
}