from ctypes import Array
from BaseClasses import ItemClassification
from dataclasses import dataclass, field
from typing import ClassVar
from .Types import DLCNames, ItemNames, ItemCategories


@dataclass
class DDItemData:
    __item_id : ClassVar[int] = 190000

    name : str
    address : int = 0
    classification : ItemClassification = ItemClassification.filler
    category : ItemCategories = ItemCategories.MISC.value
    dlc = DLCNames.NONE.value

    def __post_init__(self):
        self.address = DDItemData.__item_id
        DDItemData.__item_id += 1

    def __str__(self):
        return self.name
    
    def is_unique(self):
        return self.category in [ItemCategories.KEY.value, ItemCategories.TROPHY.value]

@dataclass
class DDLocationData:
    __location_id : ClassVar[int] = 190000

    name: str

    default_item : str

    address : int = -1

    dlc : str = DLCNames.NONE.value

    use_default: bool = False

    def __post_init__(self):
        self.address = DDLocationData.__location_id
        DDLocationData.__location_id += 1

@dataclass
class DDRegionData:
    name : str
    dlc : DLCNames = DLCNames.NONE
    location_data : list[DDLocationData] = field(default_factory=list)

    def location_dictionary(self):
        return {data.name : data for data in self.location_data}