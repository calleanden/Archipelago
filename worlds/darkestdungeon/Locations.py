from typing import Dict, ClassVar
from dataclasses import dataclass
from BaseClasses import Location
from .CustomDataClasses import DDLocationData

class DarkestDungeonLocation(Location):

    def __init__(self, player, data : DDLocationData, parent):
       super().__init__(player, data.name, data.address, parent)
       self.data : DDLocationData = data