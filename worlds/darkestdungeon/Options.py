from dataclasses import dataclass
from Options import Choice, DeathLink, Toggle, PerGameCommonOptions, OptionGroup, Range

class TrophyRequirement(Range):
    """
    The amount of specific, randomly chosen trophies required to enter the Darkest Dungeon.
    """
    display_name = "Trophies Required"

    range_start = 0
    range_end = 18
    default = 1

class MarkRequirement(Range):
    """
    The amount of generic marks required to enter the Darkest Dungeon.
    """
    display_name = "Marks Required"
    range_start = 0
    range_end = 16
    default = 4

class EnableCCDLC(Toggle):
    """
    Enables the Crimson Court DLC.
    """
    display_name = "Enable Crimson Court DLC"
    default = False

class EnableCoMDLC(Toggle):
    """
    Enables the Color of Madness DLC.
    """
    display_name = "Enable Color of Madness DLC"
    default = False

class EnableSBDLC(Toggle):
    """
    Enables the Shieldbreaker DLC.
    """
    display_name = "Enable Shieldbreaker DLC"
    default = False

class DeathLinkAmnesty(Range):
    """
    The number of character deaths required to send a deathlink.
    """
    display_name = "Deathlink Amnesty"
    range_start = 1
    range_end = 4
    default = 4

class PageSanity(Toggle):
    """
    Adds 33 locations for collecting and completing the four sections of the Ancestor's Memorial.
    """
    display_name = "Pagesanity"
    default = False

class RosterSanity(Toggle):
    """
    Adds 17 locations for achieving Resolve Level 6 on various characters.
    """
    display_name = "Rostersanity"
    default = False

class Difficulty(Choice):
    """
    Difficulty of the randomizer's logic. Affects things like putting useful unlocks earlier.
    """
    display_name = "Difficulty Mode"

    option_easy = 1;
    option_normal = 2;
    option_hard = 3;

    default = option_normal;

class OpenDungeon(Toggle):
    """
    Shuffles the keys to the final missions into the itempool. All three introductory missions (We are the Flame, Lighting the Way, and Belly of the Beast) must be completed before the final mission.
    """
    display_name = "Open Dungeon"
    default = False

@dataclass
class DarkestDungeonOptions(PerGameCommonOptions):
    trophy_requirement : TrophyRequirement
    mark_requirement : MarkRequirement
    enable_CC_DLC : EnableCCDLC
    enable_CoM_DLC : EnableCoMDLC
    enable_SB_DLC : EnableSBDLC
    death_link : DeathLink
    death_link_amnesty : DeathLinkAmnesty
    page_sanity : PageSanity
    roster_sanity : RosterSanity
    open_dungeon : OpenDungeon
    difficulty : Difficulty


option_groups = [
    OptionGroup(
        "Goal Options",
                [TrophyRequirement, MarkRequirement]),
    OptionGroup(
        "DLC Options",
            [EnableCCDLC, EnableCoMDLC, EnableSBDLC]),
    OptionGroup(
        "Deathlink Options",
        [DeathLink, DeathLinkAmnesty]),
    OptionGroup(
        "Additional Check Options",
        [PageSanity, RosterSanity, OpenDungeon])
]

option_presets = {
    "radiant" : {
        "trophy_requirement" : 1,
        "mark_requirement" : 4,
        "enable_CC_DLC" : False,
        "enable_CoM_DLC" : False,
        "enable_SB_DLC" : False,
        "death_link" : False,
        "death_link_amnesty" : 4,
        "pagesanity" : False,
        "rostersanity" : False,
        "difficulty" : Difficulty.option_easy
        },
    "dungeoneer" : {
        "trophy_requirement" : 3,
        "mark_requirement" : 8,
        "death_link" : True,
        "death_link_amnesty" : 4,
        },
    "harker" : {
        "trophy_requirement" : 2,
        "mark_requirement" : 6,
        "enable_CC_DLC" : True,
        "death_link" : True,
        "death_link_amnesty" : 4,
        },
    "arkham" : {
        "trophy_requirement" : 2,
        "mark_requirement" : 6,
        "enable_CoM_DLC" : True,
        "death_link" : True,
        "death_link_amnesty" : 4,
        },
    "grindhouse" : {
        "trophy_requirement" : 1,
        "mark_requirement" : 4,
        "pagesanity" : True,
        "rostersanity" : True
        },
    }