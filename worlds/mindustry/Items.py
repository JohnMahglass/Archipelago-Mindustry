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
    "Core: Shard": ItemData(MINDUSTRY_BASE_ID + 0, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.MISC),
    "Core: Foundation": ItemData(MINDUSTRY_BASE_ID + 1, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Core: Nucleus": ItemData(MINDUSTRY_BASE_ID + 2, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Conveyor": ItemData(MINDUSTRY_BASE_ID + 3, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.BELT),
    "Junction": ItemData(MINDUSTRY_BASE_ID + 4, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Router": ItemData(MINDUSTRY_BASE_ID + 5, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Launch Pad": ItemData(MINDUSTRY_BASE_ID + 6, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Distributor": ItemData(MINDUSTRY_BASE_ID + 7, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Sorter": ItemData(MINDUSTRY_BASE_ID + 8, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Inverted Sorter": ItemData(MINDUSTRY_BASE_ID + 9, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Overflow Gate": ItemData(MINDUSTRY_BASE_ID + 10, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Underflow Gate": ItemData(MINDUSTRY_BASE_ID + 11, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Container": ItemData(MINDUSTRY_BASE_ID + 12, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Unloader": ItemData(MINDUSTRY_BASE_ID + 13, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Vault": ItemData(MINDUSTRY_BASE_ID + 14, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Bridge Conveyor": ItemData(MINDUSTRY_BASE_ID + 15, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Titanium Conveyor": ItemData(MINDUSTRY_BASE_ID + 16, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Phase Conveyor": ItemData(MINDUSTRY_BASE_ID + 17, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Mass Driver": ItemData(MINDUSTRY_BASE_ID + 18, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Payload Conveyor": ItemData(MINDUSTRY_BASE_ID + 19, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Payload Router": ItemData(MINDUSTRY_BASE_ID + 20, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.BELT),
    "Armored Conveyor": ItemData(MINDUSTRY_BASE_ID + 21, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Plastanium Conveyor": ItemData(MINDUSTRY_BASE_ID + 22, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.BELT),
    "Mechanical Drill": ItemData(MINDUSTRY_BASE_ID + 23, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.EXTRACTION),
    "Mechanical Pump": ItemData(MINDUSTRY_BASE_ID + 24, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.CONDUIT),
    "Conduit": ItemData(MINDUSTRY_BASE_ID + 25, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.CONDUIT),
    "Liquid Junction": ItemData(MINDUSTRY_BASE_ID + 26, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Router": ItemData(MINDUSTRY_BASE_ID + 27, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Container": ItemData(MINDUSTRY_BASE_ID + 28, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Liquid Tank": ItemData(MINDUSTRY_BASE_ID + 29, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Bridge Conduit": ItemData(MINDUSTRY_BASE_ID + 30, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.CONDUIT),
    "Pulse Conduit": ItemData(MINDUSTRY_BASE_ID + 31, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Phase Conduit": ItemData(MINDUSTRY_BASE_ID + 32, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Plated Conduit": ItemData(MINDUSTRY_BASE_ID + 33, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Rotary Pump": ItemData(MINDUSTRY_BASE_ID + 34, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Impulse Pump": ItemData(MINDUSTRY_BASE_ID + 35, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.CONDUIT),
    "Graphite Press": ItemData(MINDUSTRY_BASE_ID + 36, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Pneumatic Drill": ItemData(MINDUSTRY_BASE_ID + 37, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Cultivator": ItemData(MINDUSTRY_BASE_ID + 38, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Laser Drill": ItemData(MINDUSTRY_BASE_ID + 39, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Airblast Drill": ItemData(MINDUSTRY_BASE_ID + 40, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.EXTRACTION),
    "Water Extractor": ItemData(MINDUSTRY_BASE_ID + 41, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Oil Extractor": ItemData(MINDUSTRY_BASE_ID + 42, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.EXTRACTION),
    "Pyratite Mixer": ItemData(MINDUSTRY_BASE_ID + 43, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Blast Mixer": ItemData(MINDUSTRY_BASE_ID + 44, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Silicon Smelter": ItemData(MINDUSTRY_BASE_ID + 45, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Spore Press": ItemData(MINDUSTRY_BASE_ID + 46, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Coal Centrifuge": ItemData(MINDUSTRY_BASE_ID + 47, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.INDUSTRY),
    "Multi-Press": ItemData(MINDUSTRY_BASE_ID + 48, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Silicon Crucible": ItemData(MINDUSTRY_BASE_ID + 49, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Plastanium Compressor": ItemData(MINDUSTRY_BASE_ID + 50, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Phase Weaver": ItemData(MINDUSTRY_BASE_ID + 51, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Kiln": ItemData(MINDUSTRY_BASE_ID + 52, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.INDUSTRY),
    "Pulverizer": ItemData(MINDUSTRY_BASE_ID + 53, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Incinerator": ItemData(MINDUSTRY_BASE_ID + 54, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Melter": ItemData(MINDUSTRY_BASE_ID + 55, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Surge Smelter": ItemData(MINDUSTRY_BASE_ID + 56, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Separator": ItemData(MINDUSTRY_BASE_ID + 57, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Disassembler": ItemData(MINDUSTRY_BASE_ID + 58, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Cryofluid Mixer": ItemData(MINDUSTRY_BASE_ID + 59, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.INDUSTRY),
    "Micro Processor": ItemData(MINDUSTRY_BASE_ID + 60, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Switch": ItemData(MINDUSTRY_BASE_ID + 61, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Message": ItemData(MINDUSTRY_BASE_ID + 62, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Logic Display": ItemData(MINDUSTRY_BASE_ID + 63, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Large Logic Display": ItemData(MINDUSTRY_BASE_ID + 64, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Memory Cell": ItemData(MINDUSTRY_BASE_ID + 65, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Memory Bank": ItemData(MINDUSTRY_BASE_ID + 66, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Logic Processor": ItemData(MINDUSTRY_BASE_ID + 67, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Hyper Processor": ItemData(MINDUSTRY_BASE_ID + 68, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.LOGIC),
    "Illuminator": ItemData(MINDUSTRY_BASE_ID + 69, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Combustion Generator": ItemData(MINDUSTRY_BASE_ID + 70, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.ENERGY),
    "Power Node": ItemData(MINDUSTRY_BASE_ID + 71, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.ENERGY),
    "Large Power Node": ItemData(MINDUSTRY_BASE_ID + 72, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Battery Diode": ItemData(MINDUSTRY_BASE_ID + 73, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Surge Tower": ItemData(MINDUSTRY_BASE_ID + 74, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Battery": ItemData(MINDUSTRY_BASE_ID + 75, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Large Battery": ItemData(MINDUSTRY_BASE_ID + 76, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Mender": ItemData(MINDUSTRY_BASE_ID + 77, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.MISC),
    "Mend Projector": ItemData(MINDUSTRY_BASE_ID + 78, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Force Projector": ItemData(MINDUSTRY_BASE_ID + 79, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Overdrive Projector": ItemData(MINDUSTRY_BASE_ID + 80, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Overdrive Dome": ItemData(MINDUSTRY_BASE_ID + 81, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Repair Point": ItemData(MINDUSTRY_BASE_ID + 82, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.FACTORY),
    "Repair Turret": ItemData(MINDUSTRY_BASE_ID + 83, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.FACTORY),
    "Steam Generator": ItemData(MINDUSTRY_BASE_ID + 84, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.ENERGY),
    "Thermal Generator": ItemData(MINDUSTRY_BASE_ID + 85, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Differential Generator": ItemData(MINDUSTRY_BASE_ID + 86, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Thorium Reactor": ItemData(MINDUSTRY_BASE_ID + 87, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Impact Reactor": ItemData(MINDUSTRY_BASE_ID + 88, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "RTG Generator": ItemData(MINDUSTRY_BASE_ID + 89, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Solar Panel": ItemData(MINDUSTRY_BASE_ID + 90, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Large Solar Panel": ItemData(MINDUSTRY_BASE_ID + 91, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.ENERGY),
    "Duo": ItemData(MINDUSTRY_BASE_ID + 92, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.TURRET),
    "Copper Wall": ItemData(MINDUSTRY_BASE_ID + 93, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.WALL),
    "Large Copper Wall": ItemData(MINDUSTRY_BASE_ID + 94, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Titanium Wall": ItemData(MINDUSTRY_BASE_ID + 95, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Large Titanium Wall": ItemData(MINDUSTRY_BASE_ID + 96, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.WALL),
    "Door": ItemData(MINDUSTRY_BASE_ID + 97, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Door": ItemData(MINDUSTRY_BASE_ID + 98, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Plastanium Wall": ItemData(MINDUSTRY_BASE_ID + 99, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Plastanium Wall": ItemData(MINDUSTRY_BASE_ID + 100, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Thorium Wall": ItemData(MINDUSTRY_BASE_ID + 101, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Thorium Wall": ItemData(MINDUSTRY_BASE_ID + 102, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Surge Wall": ItemData(MINDUSTRY_BASE_ID + 103, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Surge Wall": ItemData(MINDUSTRY_BASE_ID + 104, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Phase Wall": ItemData(MINDUSTRY_BASE_ID + 105, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Large Phase Wall": ItemData(MINDUSTRY_BASE_ID + 106, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.WALL),
    "Scatter": ItemData(MINDUSTRY_BASE_ID + 107, ItemPlanet.SERPULO, ItemType.TUTORIAL, ItemGroup.TURRET),
    "Hail": ItemData(MINDUSTRY_BASE_ID + 108, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Salvo": ItemData(MINDUSTRY_BASE_ID + 109, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Swarmer": ItemData(MINDUSTRY_BASE_ID + 110, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Cyclone": ItemData(MINDUSTRY_BASE_ID + 111, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Spectre": ItemData(MINDUSTRY_BASE_ID + 112, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Ripple": ItemData(MINDUSTRY_BASE_ID + 113, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Fuse": ItemData(MINDUSTRY_BASE_ID + 114, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Scorch": ItemData(MINDUSTRY_BASE_ID + 115, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Arc": ItemData(MINDUSTRY_BASE_ID + 116, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Wave": ItemData(MINDUSTRY_BASE_ID + 117, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.TURRET),
    "Parallax": ItemData(MINDUSTRY_BASE_ID + 118, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Segment": ItemData(MINDUSTRY_BASE_ID + 119, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Tsunami": ItemData(MINDUSTRY_BASE_ID + 120, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Lancer": ItemData(MINDUSTRY_BASE_ID + 121, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Meltdown": ItemData(MINDUSTRY_BASE_ID + 122, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Foreshadow": ItemData(MINDUSTRY_BASE_ID + 123, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.TURRET),
    "Shock Mine": ItemData(MINDUSTRY_BASE_ID + 124, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.MISC),
    "Ground Factory": ItemData(MINDUSTRY_BASE_ID + 125, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.FACTORY),
    "Dagger": ItemData(MINDUSTRY_BASE_ID + 126, ItemPlanet.SERPULO, ItemType.NECESSARY, ItemGroup.UNIT),
    "Mace": ItemData(MINDUSTRY_BASE_ID + 127, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Fortress": ItemData(MINDUSTRY_BASE_ID + 128, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Scepter": ItemData(MINDUSTRY_BASE_ID + 129, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Reign": ItemData(MINDUSTRY_BASE_ID + 130, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Nova": ItemData(MINDUSTRY_BASE_ID + 131, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Pulsar": ItemData(MINDUSTRY_BASE_ID + 132, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Quasar": ItemData(MINDUSTRY_BASE_ID + 133, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Vela": ItemData(MINDUSTRY_BASE_ID + 134, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Corvus": ItemData(MINDUSTRY_BASE_ID + 135, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Crawler": ItemData(MINDUSTRY_BASE_ID + 136, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Atrax": ItemData(MINDUSTRY_BASE_ID + 137, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Spiroct": ItemData(MINDUSTRY_BASE_ID + 138, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Arkyid": ItemData(MINDUSTRY_BASE_ID + 139, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Toxopid": ItemData(MINDUSTRY_BASE_ID + 140, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Air Factory": ItemData(MINDUSTRY_BASE_ID + 141, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    "Flare": ItemData(MINDUSTRY_BASE_ID + 142, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Horizon": ItemData(MINDUSTRY_BASE_ID + 143, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Zenith": ItemData(MINDUSTRY_BASE_ID + 144, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Antumbra": ItemData(MINDUSTRY_BASE_ID + 145, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Eclipse": ItemData(MINDUSTRY_BASE_ID + 146, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Mono": ItemData(MINDUSTRY_BASE_ID + 147, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Poly": ItemData(MINDUSTRY_BASE_ID + 148, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Mega": ItemData(MINDUSTRY_BASE_ID + 149, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Quad": ItemData(MINDUSTRY_BASE_ID + 150, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Oct": ItemData(MINDUSTRY_BASE_ID + 151, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Naval Factory": ItemData(MINDUSTRY_BASE_ID + 152, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    "Risso": ItemData(MINDUSTRY_BASE_ID + 153, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.UNIT),
    "Minke": ItemData(MINDUSTRY_BASE_ID + 154, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Bryde": ItemData(MINDUSTRY_BASE_ID + 155, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Sei": ItemData(MINDUSTRY_BASE_ID + 156, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Omura": ItemData(MINDUSTRY_BASE_ID + 157, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Retusa": ItemData(MINDUSTRY_BASE_ID + 158, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Oxynoe": ItemData(MINDUSTRY_BASE_ID + 159, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Cryerce": ItemData(MINDUSTRY_BASE_ID + 160, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Aegires": ItemData(MINDUSTRY_BASE_ID + 161, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Navanax": ItemData(MINDUSTRY_BASE_ID + 162, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.UNIT),
    "Additive Reconstructor": ItemData(MINDUSTRY_BASE_ID + 163, ItemPlanet.SERPULO, ItemType.USEFUL, ItemGroup.FACTORY),
    "Multiplicative Reconstructor": ItemData(MINDUSTRY_BASE_ID + 164, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.FACTORY),
    "Exponential Reconstructor": ItemData(MINDUSTRY_BASE_ID + 165, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.FACTORY),
    "Tetrative Reconstructor": ItemData(MINDUSTRY_BASE_ID + 166, ItemPlanet.SERPULO, ItemType.EXTRA, ItemGroup.FACTORY),

}
"""
Notes:
- "Filler items" should be created to balance the number of item/location when submiting them to the generation process.
- Spore press might be NECESSARY
- Coal Centrifuge might be NECESSARY
- Air Factory might be NECESSARY
- Units might be progressives item
"""
