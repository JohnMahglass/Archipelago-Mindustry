from typing import ClassVar, Dict, List, Mapping, Any

from BaseClasses import MultiWorld, ItemClassification
from worlds.AutoWorld import World, WebWorld
from worlds.mindustry.Shared import MINDUSTRY_BASE_ID
from worlds.mindustry.Items import item_table, MindustryItem, ItemType
from worlds.mindustry.Locations import location_table
from worlds.mindustry.Options import MindustryOptions
from worlds.mindustry.Regions import MindustryRegions
from Utils import visualize_regions

class MindustryWeb(WebWorld):
    """Mindustry web page for Archipelago"""
    theme = "stone"


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

    topology_present = True
    "show path to required location checks in spoiler"

    item_name_to_id: ClassVar[Dict[str, int]] =\
        {name: data.id for name, data in item_table.items()}
    "The name and associated ID of each item of the world"

    location_name_to_id = location_table
    "The name and associated ID of each location of the world"

    base_id = MINDUSTRY_BASE_ID
    "The starting ID of the items and locations of the world"

    options_dataclass = MindustryOptions
    "Used to manage world options"

    options: MindustryOptions
    "Every options of the world"

    regions: MindustryRegions
    "Used to manage Regions"

    exclude: List[str]

    def create_regions(self) -> None:
        """
        Create every Region in `regions`
        """
        self.regions.connect_regions()
        self.regions.add_event_locations()

    def create_item(self, name: str) -> MindustryItem:
        """
        Create an MindustryItem using `name` as item name.
        """
        result: MindustryItem
        try:
            data = item_table[name]
            classification: ItemClassification = ItemClassification.useful
            if data.type == ItemType.JUNK:
                classification = ItemClassification.filler
            if data.type == ItemType.NECESSARY:
                classification = ItemClassification.progression
            result = MindustryItem(name, classification, data.id, self.player)
        except BaseException:
            raise Exception('The item ' + name + ' is not valid.')

        return result

    def __pre_fill_item(self, item_name: str, location_name: str, precollected) -> None:
        """Pre-assign an item to a location"""
        if item_name not in precollected:
            self.exclude.append(item_name)
            data = item_table[item_name]
            item = MindustryItem(item_name, data.id, ItemClassification.useful, self.player)
            self.multiworld.get_location(location_name, self.player).place_locked_item(item)

    def create_items(self) -> None:
        """Create every item in the world"""
        precollected = [item.name for item in self.multiworld.precollected_items[self.player]]
        for name, data in item_table.items():
            if name in precollected:
                precollected.remove(name)
                self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))
            else:
                if name not in self.exclude:
                    item_count = item_table.get(name).count
                    for i in range(item_count):
                        item = self.create_item(name)
                        self.multiworld.itempool.append(item)


    def set_rules(self) -> None:
        """
        Launched when the Multiworld generator is ready to generate rules
        """
        self.regions.initialise_rules(self.options)
        self.multiworld.completion_condition[self.player] = lambda \
                state: state.has("Victory", self.player)

    def __init__(self, multiworld: MultiWorld, player: int):
        """Initialise the Mindustry World"""
        super(MindustryWorld, self).__init__(multiworld, player)
        self.regions = MindustryRegions(multiworld, player)
        self.exclude = []

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "tutorial_skip": bool (self.options.tutorial_skip.value),
            "campaign_choice": self.options.campaign_choice.value,
            "sector_behavior": self.options.sector_behavior.value,
            "ressource_behavior": self.options.ressource_behavior.value,
            "disable_invasion": bool (self.options.disable_invasions.value),
            "early_ressources": bool (self.options.early_ressources.value)
        }
