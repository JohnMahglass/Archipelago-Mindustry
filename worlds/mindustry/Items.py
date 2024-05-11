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
    "Graphite Press": ItemData(mindustry_base_id + 36, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Pneumatic Drill": ItemData(mindustry_base_id + 37, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Cultivator": ItemData(mindustry_base_id + 38, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Laser Drill": ItemData(mindustry_base_id + 39, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Airblast Drill": ItemData(mindustry_base_id + 40, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.EXTRACTION),
    "Water Extractor": ItemData(mindustry_base_id + 41, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Oil Extractor": ItemData(mindustry_base_id + 42, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Pyratite Mixer": ItemData(mindustry_base_id + 43, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Blast Mixer": ItemData(mindustry_base_id + 44, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Silicon Smelter": ItemData(mindustry_base_id + 45, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Spore Press": ItemData(mindustry_base_id + 46, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Coal Centrifuge": ItemData(mindustry_base_id + 47, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Multi-Press": ItemData(mindustry_base_id + 48, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Silicon Crucible": ItemData(mindustry_base_id + 49, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Plastanium Compressor": ItemData(mindustry_base_id + 50, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Phase Weaver": ItemData(mindustry_base_id + 51, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Kiln": ItemData(mindustry_base_id + 52, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Pulverizer": ItemData(mindustry_base_id + 53, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Incinerator": ItemData(mindustry_base_id + 54, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Melter": ItemData(mindustry_base_id + 55, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Surge Smelter": ItemData(mindustry_base_id + 56, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Separator": ItemType(mindustry_base_id + 57, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Disassembler": ItemType(mindustry_base_id + 58, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Cryofluid Mixer": ItemType(mindustry_base_id + 59, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Micro Processor": ItemType(mindustry_base_id + 60, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Switch": ItemType(mindustry_base_id + 61, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Message": ItemType(mindustry_base_id + 62, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Logic Display": ItemType(mindustry_base_id + 63, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Large Logic Display": ItemType(mindustry_base_id + 64, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Memory Cell": ItemType(mindustry_base_id + 65, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Memory Bank": ItemType(mindustry_base_id + 66, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Logic Processor": ItemType(mindustry_base_id + 67, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Hyper Processor": ItemType(mindustry_base_id + 68, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Illuminator": ItemType(mindustry_base_id + 69, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Combustion Generator": ItemType(mindustry_base_id + 70, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.ENERGY),
    "Power Node": ItemType(mindustry_base_id + 71, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.ENERGY),
    "Large Power Node": ItemType(mindustry_base_id + 72, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Battery Diode": ItemType(mindustry_base_id + 73, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Surge Tower": ItemType(mindustry_base_id + 74, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Battery": ItemType(mindustry_base_id + 75, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Large Battery": ItemType(mindustry_base_id + 76, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Mender": ItemType(mindustry_base_id + 77, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Mend Projector": ItemType(mindustry_base_id + 78, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Force Projector": ItemType(mindustry_base_id + 79, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Overdrive Projector": ItemType(mindustry_base_id + 80, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Overdrive Dome": ItemType(mindustry_base_id + 81, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Repair Point": ItemType(mindustry_base_id + 82, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.FACTORY),
    "Repair Turret": ItemType(mindustry_base_id + 83, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.FACTORY),
    "Steam Generator": ItemType(mindustry_base_id + 84, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Thermal Generator": ItemType(mindustry_base_id + 85, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Differential Generator": ItemType(mindustry_base_id + 86, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Thorium Reactor": ItemType(mindustry_base_id + 87, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Impact Reactor": ItemType(mindustry_base_id + 88, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "RTG Generator": ItemType(mindustry_base_id + 89, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Solar Panel": ItemType(mindustry_base_id + 90, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Large Solar Panel": ItemType(mindustry_base_id + 91, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Duo": ItemType(mindustry_base_id + 92, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.TURRET),
    "Copper Wall": ItemType(mindustry_base_id + 93, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.WALL),
    "Large Copper Wall": ItemType(mindustry_base_id + 94, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Titanium Wall": ItemType(mindustry_base_id + 95, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Large Titanium Wall": ItemType(mindustry_base_id + 96, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Door": ItemType(mindustry_base_id + 97, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Door": ItemType(mindustry_base_id + 98, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Plastanium Wall": ItemType(mindustry_base_id + 99, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Plastanium Wall": ItemType(mindustry_base_id + 100, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Thorium Wall": ItemType(mindustry_base_id + 101, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Thorium Wall": ItemType(mindustry_base_id + 102, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Surge Wall": ItemType(mindustry_base_id + 103, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Surge Wall": ItemType(mindustry_base_id + 104, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Phase Wall": ItemType(mindustry_base_id + 105, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Phase Wall": ItemType(mindustry_base_id + 106, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Scatter": ItemType(mindustry_base_id + 107, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.TURRET),
    "Hail": ItemType(mindustry_base_id + 108, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Salvo": ItemType(mindustry_base_id + 109, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Swarmer": ItemType(mindustry_base_id + 110, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Cyclone": ItemType(mindustry_base_id + 111, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Spectre": ItemType(mindustry_base_id + 112, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Ripple": ItemType(mindustry_base_id + 113, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Fuse": ItemType(mindustry_base_id + 114, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Scorch": ItemType(mindustry_base_id + 115, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Arc": ItemType(mindustry_base_id + 116, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Wave": ItemType(mindustry_base_id + 117, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Parallax": ItemType(mindustry_base_id + 118, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Segment": ItemType(mindustry_base_id + 119, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Tsunami": ItemType(mindustry_base_id + 120, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Lancer": ItemType(mindustry_base_id + 121, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Meltdown": ItemType(mindustry_base_id + 122, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Foreshadow": ItemType(mindustry_base_id + 123, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Shock Mine": ItemType(mindustry_base_id + 124, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),

}
"""
Notes:
- Spore press might be NECESSARY
- Coal Centrifuge might be NECESSARY
"""
