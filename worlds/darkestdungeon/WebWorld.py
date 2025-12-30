from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .Options import option_groups, option_presets

class DarkestDungeonWebWorld(WebWorld):
    game = "Darkest Dungeon"
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

    option_groups = option_groups;
    options_presets = option_presets;
