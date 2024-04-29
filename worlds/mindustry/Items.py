from typing import Optional
from BaseClasses import Item, ItemClassification
from enum import Enum

from worlds.mindustry.Shared import mindustry_base_id


"""This class (ItemType) might need to be renamed and have its content changed for something more useful?"""
class ItemType(Enum):
    """
    Indicate to the multi-world the item usefulness
    """
    TRAP = 0
    USEFUL = 1
    NECESSARY = 2


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
    WALL = 6


class ItemPlanet(Enum):
    """
    Used to group items by planet
    """
    EREKIR = 0
    SERPULO = 1


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


class ItemData:
    """
    Data of an item
    """
    id: int
    type: ItemType
    group: ItemGroup

    def __init__(self, id: int, planet: ItemPlanet, type: ItemType, group: ItemGroup):
        """
        Initialisation of the item data
        @param id: The ID of the item
        @param planet: The planet of the item
        @param type: The type of item
        @param group: The type of item
        """


item_table = {
    "Exemple Core Item": ItemData(mindustry_base_id + 0, ItemPlanet.EREKIR, ItemType.NECESSARY, ItemGroup.CORE)
}
