from dataclasses import dataclass
from Options import Choice, DeathLink, Toggle, PerGameCommonOptions

class EnableCCDLC(Toggle):
    """
    Enables the Crimson Court DLC.
    """
    display_name = "Enable Crimson Court DLC"

class EnableCoMDLC(Toggle):
    """
    Enables the Color of Madness DLC.
    """
    display_name = "Enable Color of Madness DLC"

class EnableSBDLC(Toggle):
    """
    Enables the Shieldbreaker DLC.
    """
    display_name = "Enable Shieldbreaker DLC"


@dataclass
class DarkestDungeonOptions(PerGameCommonOptions):
    enable_CC_DLC : EnableCCDLC
    enable_CoM_DLC : EnableCoMDLC
    enable_SB_DLC : EnableSBDLC