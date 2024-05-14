from BaseClasses import MultiWorld
from worlds.AutoWorld import World, WebWorld
from worlds.mindustry.Shared import MINDUSTRY_BASE_ID
from worlds.mindustry.Items import item_table
from worlds.mindustry.Locations import location_table
from worlds.mindustry.Options import MindustryOptions
from worlds.mindustry.Regions import MindustryRegions


class MindustryWeb(WebWorld):
    """Mindustry web page for Archipelago"""
    theme = "stone"

    def __init__(self):
        """Initialise the Mindustry web page"""


class MindustryWorld(World):
    """
    In Mindustry, you control a small ship that defends a structure called the Core,
    your job is to build production lines and defenses to survive, maintain and conquer.
    There are a total of eight different categories of structures to build, varying from
    drills and factories to extract and refine resources, to turrets and walls to defend your assets.
    There are many more buildings that help to take back Serpulo and other planets. the two current
    planets are; Serpulo and Erikir, Serpulo is the home planet of your faction; the Sharded,
    brought to defend the planet from the formidable enemy; the Crux. The second planet of Erikir
    has a far different and far more deadly enemy of Malis, and their strategies reflect such.
    Source: https://en.wikipedia.org/wiki/Draft:Mindustry
    """
    game: str = "Mindustry"
    """Name of the game"""

    options_dataclass = MindustryOptions

    options: MindustryOptions

    topology_present = True

    base_id: int = MINDUSTRY_BASE_ID

    web = MindustryWeb()
    """Web world instance"""

    item_name_to_id = {name: id for
                       id, name in enumerate(item_table, base_id)}

    location_name_to_id = {name: id for
                           id, name in enumerate(location_table, base_id)}

    regions: MindustryRegions
    """Used to manage regions"""

    item_name_groups = {
        """NOT IMPLEMENTED"""
    }

    def __init__(self, multiworld: MultiWorld, player: int):
        """Initialise the Mindustry World"""
        super(MindustryWorld, self).__init__(multiworld, player)
        self.regions = MindustryRegions(multiworld, player)
