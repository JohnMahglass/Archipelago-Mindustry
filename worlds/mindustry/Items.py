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
    """Non-item event with negative effect"""
    EVENT = 1
    """Non-item event"""
    USEFUL = 2
    """Item that are useful for progression"""
    NECESSARY = 3
    """Item that are necessary for progression"""
    TUTORIAL = 4
    """Item that are acquired in the tutorial"""
    EXTRA = 5
    """Item that are extra and not necessary to complete the game"""

class ItemGroup(Enum):
    """
    Used to group items, Item are grouped by their location in the building UI
    """
    TURRET = 0
    EXTRACTION = 1
    BELT = 2
    CONDUIT = 3
    ENERGY = 4
    WALL = 5
    INDUSTRY = 6
    FACTORY = 7
    LOGIC = 8
    MISC = 9
    UNIT = 10

class ItemPlanet(Enum):
    """
    Used to group items by planet
    """
    EREKIR = 0
    SERPULO = 1
    ALL = 2


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
    item_planet: ItemPlanet
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

"""Information table for every item that is not an event."""
item_table = {
    "Core: Shard": ItemData(mindustry_base_id + 0, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.MISC),
    "Core: Foundation": ItemData(mindustry_base_id + 1, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Core: Nucleus": ItemData(mindustry_base_id + 2, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Conveyor": ItemData(mindustry_base_id + 3, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.BELT),
    "Junction": ItemData(mindustry_base_id + 4, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Router": ItemData(mindustry_base_id + 5, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Launch Pad": ItemData(mindustry_base_id + 6, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Distributor": ItemData(mindustry_base_id + 7, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Sorter": ItemData(mindustry_base_id + 8, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Inverted Sorter": ItemData(mindustry_base_id + 9, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Overflow Gate": ItemData(mindustry_base_id + 10, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Underflow Gate": ItemData(mindustry_base_id + 11, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Container": ItemData(mindustry_base_id + 12, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Unloader": ItemData(mindustry_base_id + 13, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Vault": ItemData(mindustry_base_id + 14, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Bridge Conveyor": ItemData(mindustry_base_id + 15, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Titanium Conveyor": ItemData(mindustry_base_id + 16, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Phase Conveyor": ItemData(mindustry_base_id + 17, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Mass Driver": ItemData(mindustry_base_id + 18, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Payload Conveyor": ItemData(mindustry_base_id + 19, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Payload Router": ItemData(mindustry_base_id + 20, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Armored Conveyor": ItemData(mindustry_base_id + 21, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Plastanium Conveyor": ItemData(mindustry_base_id + 22, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Mechanical Drill": ItemData(mindustry_base_id + 23, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.EXTRACTION),
    "Mechanical Pump": ItemData(mindustry_base_id + 24, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.CONDUIT),
    "Conduit": ItemData(mindustry_base_id + 25, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.CONDUIT),
    "Liquid Junction": ItemData(mindustry_base_id + 26, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Router": ItemData(mindustry_base_id + 27, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Container": ItemData(mindustry_base_id + 28, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Tank": ItemData(mindustry_base_id + 29, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Bridge Conduit": ItemData(mindustry_base_id + 30, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Pulse Conduit": ItemData(mindustry_base_id + 31, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Phase Conduit": ItemData(mindustry_base_id + 32, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Plated Conduit": ItemData(mindustry_base_id + 33, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Rotary Pump": ItemData(mindustry_base_id + 34, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Impulse Pump": ItemData(mindustry_base_id + 35, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Graphite Press": ItemData(mindustry_base_id + 36, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.FACTORY),
    "Pneumatic Drill": ItemData(mindustry_base_id + 37, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Cultivator": ItemData(mindustry_base_id + 38, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),

}
