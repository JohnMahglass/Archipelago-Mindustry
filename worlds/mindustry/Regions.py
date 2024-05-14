from BaseClasses import Region, MultiWorld, Entrance
from .Options import MindustryOptions
from typing import Optional


class RegionData:
    """
    Data of a region
    """
    hint: str

class MindustryRegions:
    """
    Class used to create region for Mindustry
    """
    menu: Region
    serpulo: Region
    erekir: Region
    copper: Region
    water: Region
    lead: Region
    titanium: Region
    cryofluid: Region
    thorium: Region
    surge_alloy: Region
    phase_fabric: Region
    metaglass: Region
    sand: Region
    scrap: Region
    slag: Region
    coal: Region
    graphite: Region
    silicon: Region
    pyratite: Region
    blast_compound: Region
    spore_pod: Region
    oil: Region
    plastanium: Region
    ground_zero: Region
    frozen_forest: Region
    the_craters: Region
    ruinous_shores: Region
    windswept_islands: Region
    tar_fields: Region
    impact_0078: Region
    desolate_rift: Region
    planetary_launch_terminal: Region
    extraction_outpost: Region
    salt_flats: Region
    coastline: Region
    naval_fortress: Region
    overgrowth: Region
    biomass_synthesis_facility: Region
    stained_mountains: Region
    fungal_pass: Region
    nuclear_production_complex: Region


    multiworld: MultiWorld
    """
    Current Multiworld game
    """

    player: int
    """
    Player Id
    """

    options: MindustryOptions
    """
    Options for the Mindustry World
    """

    def __add_region(self, hint: str, locations: Optional):
        """Create a new region."""
        region: Region = Region(hint, self.player, self.multiworld, hint)
        region.locations = locations.copy
        return region

    def __connect_regions(self, source_region: Region, target_region: Region):
        """
        Connect regions between themselves
        """
        entrance = Entrance(source_region.player, source_region.name + " -> " + target_region.name, source_region)
        source_region.exits.append(entrance)
        entrance.connect(target_region)

        entrance_reverse = Entrance(target_region.player, target_region.name + " -> " + source_region.name, target_region)
        target_region.exits.append(entrance_reverse)
        entrance_reverse.connect(source_region)

    def __create_serpulo_campaign(self):
        """
        Create region related to the serpulo campaign.
        Method not implemented
        """
        serpulo: Region = self.__add_region("Serpulo", None)
        copper: Region = self.__add_region("Copper", None)
        water: Region = self.__add_region("Water", None)
        lead: Region = self.__add_region("Lead", None)
        titanium: Region = self.__add_region("Titanium", None)
        cryofluid: Region = self.__add_region("Cryfluid", None)
        thorium: Region = self.__add_region("Thorium", None)
        surge_alloy: Region = self.__add_region("Surge Alloy", None)
        phase_fabric: Region = self.__add_region("Phase Fabric", None)
        metaglass: Region = self.__add_region("Metaglass", None)
        sand: Region = self.__add_region("Sand", None)
        scrap: Region = self.__add_region("Scrap", None)
        slag: Region = self.__add_region("Slag", None)
        coal: Region = self.__add_region("Coal", None)
        graphite: Region = self.__add_region("Graphite", None)
        silicon: Region = self.__add_region("Silicon", None)
        pyratite: Region = self.__add_region("pyratite", None)
        blast_compound: Region = self.__add_region("Blast Compound", None)
        spore_pod: Region = self.__add_region("Spore pod", None)
        oil: Region = self.__add_region("Oil", None)
        plastanium: Region = self.__add_region("Plastanium", None)
        ground_zero: Region = self.__add_region("Ground Zero", None)
        frozen_forest: Region  = self.__add_region("Frozen Forest", None)
        the_craters: Region = self.__add_region("The Craters", None)
        ruinous_shores: Region = self.__add_region("Ruinous Shores", None)
        windswept_islands: Region = self.__add_region("Windswept Islands", None)
        tar_fields: Region = self.__add_region("Tar Fields", None)
        impact_0078: Region = self.__add_region("Impact 0078", None)
        desolate_rift: Region = self.__add_region("Desolate Rift", None)
        planetary_launch_terminal: Region = self.__add_region("Planetary Launch Terminal", None)
        extraction_outpost: Region = self.__add_region("Extraction Outpost", None)
        salt_flats: Region = self.__add_region("Salt Flats", None)
        coastline: Region = self.__add_region("Coastline", None)
        naval_fortress: Region = self.__add_region("Naval Fortress", None)
        overgrowth: Region = self.__add_region("Overgrowth", None)
        biomass_synthesis_facility: Region = self.__add_region("Biomass Synthesis Facility", None)
        stained_mountains: Region = self.__add_region("Stained Mountains", None)
        fungal_pass: Region = self.__add_region("Fungal Pass", None)
        nuclear_production_complex: Region = self.__add_region("Nuclear Production Complex", None)

    def __connect_serpulo_campaign(self):
        """
        Connect region related to Serpulo's campaign
        """


    def __create_erekir_campaign(self):
        """
        Create region related to the erekir campaign.
        Method not implemented
        """

    def __connect_erekir_campaign(self):
        """
        Connect region related to Erekir's campaign
        """

    def __create_all_campaign(self):
        """
        Create region related to the all campaigns.
        Method not implemented
        """

    def __connect_all_campaign(self):
        """
        Connect region related to all campaigns
        """

    def __create_campaign(self, campaign: int):
        """
        Create region for selected campaign
        NOTE: campaign set as int is temporary
        """
        self.menu = self.__add_region("Menu", None)
        match campaign:
            case 1:
                self.__create_serpulo_campaign()
                self.__connect_serpulo_campaign()
            case 2:
                self.__create_erekir_campaign()
            case 3:
                self.__create_all_campaign()
            case _:
                raise ValueError



    def __initialize_rules(self, options: MindustryOptions):
        """
        Apply options for region creation
        Method not implemented
        """

    def __init__(self, multiworld: MultiWorld, player: int):
        """
        Initialisation of the regions
        """
        self.multiworld = multiworld
        self.player = player
        self.__create_campaign(1)

