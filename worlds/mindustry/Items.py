from typing import Optional
from BaseClasses import Item, ItemClassification
from enum import Enum

from worlds.mindustry.Shared import MINDUSTRY_BASE_ID


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
    JUNK = 4
    """Item that are not useful or necessary for progression"""

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
    RESSOURCES = 11
    SECTOR = 12

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
        self.id = id
        self.item_planet = planet
        self.type = type
        self.group = group

"""Information table for every item that is not an event."""
item_table = {
    "Conveyor": ItemData(MINDUSTRY_BASE_ID + 0, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.BELT),
    "Junction": ItemData(MINDUSTRY_BASE_ID + 1, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Router": ItemData(MINDUSTRY_BASE_ID + 2, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Launch Pad": ItemData(MINDUSTRY_BASE_ID + 3, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Distributor": ItemData(MINDUSTRY_BASE_ID + 4, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Sorter": ItemData(MINDUSTRY_BASE_ID + 5, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Inverted Sorter": ItemData(MINDUSTRY_BASE_ID + 6, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Overflow Gate": ItemData(MINDUSTRY_BASE_ID + 7, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Underflow Gate": ItemData(MINDUSTRY_BASE_ID + 8, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Container": ItemData(MINDUSTRY_BASE_ID + 9, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Unloader": ItemData(MINDUSTRY_BASE_ID + 10, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Vault": ItemData(MINDUSTRY_BASE_ID + 11, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Bridge Conveyor": ItemData(MINDUSTRY_BASE_ID + 12, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Titanium Conveyor": ItemData(MINDUSTRY_BASE_ID + 13, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Phase Conveyor": ItemData(MINDUSTRY_BASE_ID + 14, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Mass Driver": ItemData(MINDUSTRY_BASE_ID + 15, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Payload Conveyor": ItemData(MINDUSTRY_BASE_ID + 16, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Payload Router": ItemData(MINDUSTRY_BASE_ID + 17, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Armored Conveyor": ItemData(MINDUSTRY_BASE_ID + 18, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Plastanium Conveyor": ItemData(MINDUSTRY_BASE_ID + 19, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Core: Foundation": ItemData(MINDUSTRY_BASE_ID + 20, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Core: Nucleus": ItemData(MINDUSTRY_BASE_ID + 21, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Mechanical Drill": ItemData(MINDUSTRY_BASE_ID + 22, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.EXTRACTION),
    "Mechanical Pump": ItemData(MINDUSTRY_BASE_ID + 23, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.CONDUIT),
    "Conduit": ItemData(MINDUSTRY_BASE_ID + 24, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.CONDUIT),
    "Liquid Junction": ItemData(MINDUSTRY_BASE_ID + 25, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Router": ItemData(MINDUSTRY_BASE_ID + 26, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Container": ItemData(MINDUSTRY_BASE_ID + 27, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Tank": ItemData(MINDUSTRY_BASE_ID + 28, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Bridge Conduit": ItemData(MINDUSTRY_BASE_ID + 29, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Pulse Conduit": ItemData(MINDUSTRY_BASE_ID + 30, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Phase Conduit": ItemData(MINDUSTRY_BASE_ID + 31, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Plated Conduit": ItemData(MINDUSTRY_BASE_ID + 32, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Rotary Pump": ItemData(MINDUSTRY_BASE_ID + 33, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Impulse Pump": ItemData(MINDUSTRY_BASE_ID + 34, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Graphite Press": ItemData(MINDUSTRY_BASE_ID + 35, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Pneumatic Drill": ItemData(MINDUSTRY_BASE_ID + 36, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.EXTRACTION),
    "Cultivator": ItemData(MINDUSTRY_BASE_ID + 37, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.EXTRACTION),
    "Laser Drill": ItemData(MINDUSTRY_BASE_ID + 38, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.EXTRACTION),
    "Airblast Drill": ItemData(MINDUSTRY_BASE_ID + 39, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Water Extractor": ItemData(MINDUSTRY_BASE_ID + 40, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Oil Extractor": ItemData(MINDUSTRY_BASE_ID + 41, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Pyratite Mixer": ItemData(MINDUSTRY_BASE_ID + 42, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Blast Mixer": ItemData(MINDUSTRY_BASE_ID + 43, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Silicon Smelter": ItemData(MINDUSTRY_BASE_ID + 44, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Spore Press": ItemData(MINDUSTRY_BASE_ID + 45, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Coal Centrifuge": ItemData(MINDUSTRY_BASE_ID + 46, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Multi-Press": ItemData(MINDUSTRY_BASE_ID + 47, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Silicon Crucible": ItemData(MINDUSTRY_BASE_ID + 48, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Plastanium Compressor": ItemData(MINDUSTRY_BASE_ID + 49, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Phase Weaver": ItemData(MINDUSTRY_BASE_ID + 50, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Kiln": ItemData(MINDUSTRY_BASE_ID + 51, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Pulverizer": ItemData(MINDUSTRY_BASE_ID + 52, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Incinerator": ItemData(MINDUSTRY_BASE_ID + 53, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Melter": ItemData(MINDUSTRY_BASE_ID + 54, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Surge Smelter": ItemData(MINDUSTRY_BASE_ID + 55, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Separator": ItemData(MINDUSTRY_BASE_ID + 56, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Disassembler": ItemData(MINDUSTRY_BASE_ID + 57, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Cryofluid Mixer": ItemData(MINDUSTRY_BASE_ID + 58, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Micro Processor": ItemData(MINDUSTRY_BASE_ID + 59, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Switch": ItemData(MINDUSTRY_BASE_ID + 60, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Message": ItemData(MINDUSTRY_BASE_ID + 61, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Logic Display": ItemData(MINDUSTRY_BASE_ID + 62, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Large Logic Display": ItemData(MINDUSTRY_BASE_ID + 63, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Memory Cell": ItemData(MINDUSTRY_BASE_ID + 64, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Memory Bank": ItemData(MINDUSTRY_BASE_ID + 65, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Logic Processor": ItemData(MINDUSTRY_BASE_ID + 66, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Hyper Processor": ItemData(MINDUSTRY_BASE_ID + 67, ItemPlanet.SERPULO, ItemType.JUNK, ItemGroup.LOGIC),
    "Illuminator": ItemData(MINDUSTRY_BASE_ID + 68, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Combustion Generator": ItemData(MINDUSTRY_BASE_ID + 69, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.ENERGY),
    "Power Node": ItemData(MINDUSTRY_BASE_ID + 70, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.ENERGY),
    "Large Power Node": ItemData(MINDUSTRY_BASE_ID + 71, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Battery Diode": ItemData(MINDUSTRY_BASE_ID + 72, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Surge Tower": ItemData(MINDUSTRY_BASE_ID + 73, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Battery": ItemData(MINDUSTRY_BASE_ID + 74, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Large Battery": ItemData(MINDUSTRY_BASE_ID + 75, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Mender": ItemData(MINDUSTRY_BASE_ID + 76, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Mend Projector": ItemData(MINDUSTRY_BASE_ID + 77, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Force Projector": ItemData(MINDUSTRY_BASE_ID + 78, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Overdrive Projector": ItemData(MINDUSTRY_BASE_ID + 79, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Overdrive Dome": ItemData(MINDUSTRY_BASE_ID + 80, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Repair Point": ItemData(MINDUSTRY_BASE_ID + 81, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    "Repair Turret": ItemData(MINDUSTRY_BASE_ID + 82, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    "Steam Generator": ItemData(MINDUSTRY_BASE_ID + 83, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Thermal Generator": ItemData(MINDUSTRY_BASE_ID + 84, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Differential Generator": ItemData(MINDUSTRY_BASE_ID + 85, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Thorium Reactor": ItemData(MINDUSTRY_BASE_ID + 86, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Impact Reactor": ItemData(MINDUSTRY_BASE_ID + 87, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "RTG Generator": ItemData(MINDUSTRY_BASE_ID + 88, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Solar Panel": ItemData(MINDUSTRY_BASE_ID + 89, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Large Solar Panel": ItemData(MINDUSTRY_BASE_ID + 90, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Duo": ItemData(MINDUSTRY_BASE_ID + 91, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.TURRET),
    "Copper Wall": ItemData(MINDUSTRY_BASE_ID + 92, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.WALL),
    "Large Copper Wall": ItemData(MINDUSTRY_BASE_ID + 93, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Titanium Wall": ItemData(MINDUSTRY_BASE_ID + 94, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Large Titanium Wall": ItemData(MINDUSTRY_BASE_ID + 95, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Door": ItemData(MINDUSTRY_BASE_ID + 96, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Large Door": ItemData(MINDUSTRY_BASE_ID + 97, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Plastanium Wall": ItemData(MINDUSTRY_BASE_ID + 98, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Large Plastanium Wall": ItemData(MINDUSTRY_BASE_ID + 99, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Thorium Wall": ItemData(MINDUSTRY_BASE_ID + 100, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Large Thorium Wall": ItemData(MINDUSTRY_BASE_ID + 101, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Surge Wall": ItemData(MINDUSTRY_BASE_ID + 102, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Large Surge Wall": ItemData(MINDUSTRY_BASE_ID + 103, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Phase Wall": ItemData(MINDUSTRY_BASE_ID + 104, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Large Phase Wall": ItemData(MINDUSTRY_BASE_ID + 105, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Scatter": ItemData(MINDUSTRY_BASE_ID + 106, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.TURRET),
    "Hail": ItemData(MINDUSTRY_BASE_ID + 107, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Salvo": ItemData(MINDUSTRY_BASE_ID + 108, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Swarmer": ItemData(MINDUSTRY_BASE_ID + 109, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Cyclone": ItemData(MINDUSTRY_BASE_ID + 110, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Spectre": ItemData(MINDUSTRY_BASE_ID + 111, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Ripple": ItemData(MINDUSTRY_BASE_ID + 112, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Fuse": ItemData(MINDUSTRY_BASE_ID + 113, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Scorch": ItemData(MINDUSTRY_BASE_ID + 114, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Arc": ItemData(MINDUSTRY_BASE_ID + 115, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Wave": ItemData(MINDUSTRY_BASE_ID + 116, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Parallax": ItemData(MINDUSTRY_BASE_ID + 117, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Segment": ItemData(MINDUSTRY_BASE_ID + 118, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Tsunami": ItemData(MINDUSTRY_BASE_ID + 119, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Lancer": ItemData(MINDUSTRY_BASE_ID + 120, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Meltdown": ItemData(MINDUSTRY_BASE_ID + 121, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Foreshadow": ItemData(MINDUSTRY_BASE_ID + 122, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Shock Mine": ItemData(MINDUSTRY_BASE_ID + 123, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Ground Factory": ItemData(MINDUSTRY_BASE_ID + 124, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.FACTORY),
    "Dagger": ItemData(MINDUSTRY_BASE_ID + 125, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.UNIT),
    "Progressive Ground Unit Type A": ItemData(MINDUSTRY_BASE_ID + 126, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type A": ItemData(MINDUSTRY_BASE_ID + 126, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type A": ItemData(MINDUSTRY_BASE_ID + 126, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type A": ItemData(MINDUSTRY_BASE_ID + 126, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type B": ItemData(MINDUSTRY_BASE_ID + 127, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type B": ItemData(MINDUSTRY_BASE_ID + 127, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type B": ItemData(MINDUSTRY_BASE_ID + 127, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type B": ItemData(MINDUSTRY_BASE_ID + 127, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type B": ItemData(MINDUSTRY_BASE_ID + 127, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type C": ItemData(MINDUSTRY_BASE_ID + 128, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type C": ItemData(MINDUSTRY_BASE_ID + 128, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type C": ItemData(MINDUSTRY_BASE_ID + 128, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type C": ItemData(MINDUSTRY_BASE_ID + 128, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Ground Unit Type C": ItemData(MINDUSTRY_BASE_ID + 128, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Air Factory": ItemData(MINDUSTRY_BASE_ID + 129, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.FACTORY),
    "Flare": ItemData(MINDUSTRY_BASE_ID + 130, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.UNIT),
    "Progressive Air Unit Type A": ItemData(MINDUSTRY_BASE_ID + 131, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Air Unit Type A": ItemData(MINDUSTRY_BASE_ID + 131, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Air Unit Type A": ItemData(MINDUSTRY_BASE_ID + 131, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Air Unit Type A": ItemData(MINDUSTRY_BASE_ID + 131, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Air Unit Type B": ItemData(MINDUSTRY_BASE_ID + 132, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Air Unit Type B": ItemData(MINDUSTRY_BASE_ID + 132, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Air Unit Type B": ItemData(MINDUSTRY_BASE_ID + 132, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Air Unit Type B": ItemData(MINDUSTRY_BASE_ID + 132, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Air Unit Type B": ItemData(MINDUSTRY_BASE_ID + 132, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Naval Factory": ItemData(MINDUSTRY_BASE_ID + 133, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.FACTORY),
    "Risso": ItemData(MINDUSTRY_BASE_ID + 134, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.UNIT),
    "Progressive Naval Unit Type A": ItemData(MINDUSTRY_BASE_ID + 135, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Naval Unit Type A": ItemData(MINDUSTRY_BASE_ID + 135, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Naval Unit Type A": ItemData(MINDUSTRY_BASE_ID + 135, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Naval Unit Type A": ItemData(MINDUSTRY_BASE_ID + 135, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Naval Unit Type B": ItemData(MINDUSTRY_BASE_ID + 136, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Naval Unit Type B": ItemData(MINDUSTRY_BASE_ID + 136, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Naval Unit Type B": ItemData(MINDUSTRY_BASE_ID + 136, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Naval Unit Type B": ItemData(MINDUSTRY_BASE_ID + 136, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Naval Unit Type B": ItemData(MINDUSTRY_BASE_ID + 136, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Progressive Reconstructor": ItemData(MINDUSTRY_BASE_ID + 137, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    "Progressive Reconstructor": ItemData(MINDUSTRY_BASE_ID + 137, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    "Progressive Reconstructor": ItemData(MINDUSTRY_BASE_ID + 137, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    "Progressive Reconstructor": ItemData(MINDUSTRY_BASE_ID + 137, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    #"Frozen Forest": ItemData(MINDUSTRY_BASE_ID + 166, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"The Craters": ItemData(MINDUSTRY_BASE_ID + 167, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Ruinous Shores": ItemData(MINDUSTRY_BASE_ID + 168, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Windswept Islands": ItemData(MINDUSTRY_BASE_ID + 169, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Tar Fields": ItemData(MINDUSTRY_BASE_ID + 170, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Impact 0078": ItemData(MINDUSTRY_BASE_ID + 171, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Desolate Rift": ItemData(MINDUSTRY_BASE_ID + 172, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Planetary Launch Terminal": ItemData(MINDUSTRY_BASE_ID + 173, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Extraction Outpost": ItemData(MINDUSTRY_BASE_ID + 174, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Salt Flats": ItemData(MINDUSTRY_BASE_ID + 175, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Coastline": ItemData(MINDUSTRY_BASE_ID + 176, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Naval Fortress": ItemData(MINDUSTRY_BASE_ID + 177, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Overgrowth": ItemData(MINDUSTRY_BASE_ID + 178, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Biomass Synthesis Facility": ItemData(MINDUSTRY_BASE_ID + 179, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Stained Mountains": ItemData(MINDUSTRY_BASE_ID + 180, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Fungal Pass": ItemData(MINDUSTRY_BASE_ID + 181, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Nuclear Production Complex": ItemData(MINDUSTRY_BASE_ID + 182, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.SECTOR),
    #"Lead": ItemData(MINDUSTRY_BASE_ID + 183, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Titanium": ItemData(MINDUSTRY_BASE_ID + 184, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Cryofluid": ItemData(MINDUSTRY_BASE_ID + 185, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Thorium": ItemData(MINDUSTRY_BASE_ID + 186, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Surge Alloy": ItemData(MINDUSTRY_BASE_ID + 187, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Phase Fabric": ItemData(MINDUSTRY_BASE_ID + 188, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Metaglass": ItemData(MINDUSTRY_BASE_ID + 189, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Scrap": ItemData(MINDUSTRY_BASE_ID + 190, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.RESSOURCES),
    #"Slag": ItemData(MINDUSTRY_BASE_ID + 191, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.RESSOURCES),
    #"Coal": ItemData(MINDUSTRY_BASE_ID + 192, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Graphite": ItemData(MINDUSTRY_BASE_ID + 193, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Silicon": ItemData(MINDUSTRY_BASE_ID + 194, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Pyratite": ItemData(MINDUSTRY_BASE_ID + 195, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Blast Compound": ItemData(MINDUSTRY_BASE_ID + 196, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Spore Pod": ItemData(MINDUSTRY_BASE_ID + 197, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Oil": ItemData(MINDUSTRY_BASE_ID + 198, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
    #"Plastanium": ItemData(MINDUSTRY_BASE_ID + 199, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.RESSOURCES),
}
