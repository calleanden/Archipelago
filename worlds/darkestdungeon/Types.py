from enum import IntEnum
from BaseClasses import Item, Location

class DDItem(Item):
    name = "Darkest Dungeon"

class DDLocation(Location):
    name = "Darkest Dungeon"

class RegionIndex(IntEnum):
    OLD_ROAD = 0
    HAMLET = 1
    RUINS = 2
    WEALD = 3
    WARRENS = 4
    COVE = 5
    DARKEST = 6
    ABBEY = 7
    BLACKSMITH = 8
    GUILD = 9
    NOMAD_WAGON = 10
    SANITARIUM = 11
    STAGECOACH = 12
    SURVIVALIST = 13
    TAVERN = 14


