from typing import Optional
from BaseClasses import Item, ItemClassification
from enum import Enum

from worlds.mindustry.Shared import mindustry_base_id


class ItemType(Enum):
    """
    Indicate to the multi-world the item usefulness
    """
    TRAP = 0
    USEFUL = 1
    """
    The 'Progression' type are temporary until better type names are found
    """
    EARLYPROGRESSION = 2
    MIDPROGRESSION = 3
    ENDPROGRESSION = 4
    NECESSARY = 5

class ItemGroup(Enum):
    """
    Used to group items
    """
    CORE = 0
    EXTRACTION = 1
    PRODUCTION = 2
    POWER = 3
    MILITARY = 4
    UNIT = 5

class MindustryItem(Item):
    """
    A single item in the Mindustry game.
    """
    game: str = "Mindustry"
    """The name of the game"""

    def __init__(self, name: str, classification: ItemClassification,
                 code: Optional[int], player: int):
        """
        Initialisation of the Item
        :param name: The name of the item
        :param classification: If the item is usefull or not
        :param code: The ID of the item (if None, it is an event)
        :param player: The ID of the player in the multiworld
        """
        super().__init__(name, classification, code, player)

    item_table = {
        "Exemple Core Item", mindustry_base_id + 0, ItemType.USEFUL, ItemGroup.CORE
    }


