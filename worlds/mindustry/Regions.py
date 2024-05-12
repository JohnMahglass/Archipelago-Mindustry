from BaseClasses import Region, MultiWorld
from .Options import MindustryOptions


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

    def __add_region(self, hint: str):
        """Create a new region."""
        region: Region = Region(hint, self.player, self.multiworld)
        return region

    def __create_serpulo_campaign(self):
        """
        Create region related to the serpulo campaign.
        Method not implemented
        """

    def __create_erekir_campaign(self):
        """
        Create region related to the erekir campaign.
        Method not implemented
        """

    def __create_all_campaign(self):
        """
        Create region related to the all campaigns.
        Method not implemented
        """


    def __create_campaign(self, campaign: int):
        """
        Create region for selected campaign
        NOTE: campaign set as int is temporary
        """
        match campaign:
            case 1:
                self.__create_serpulo_campaign()
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

    def __init__(self, multiworld: MultiWorld, player: int, options: MindustryOptions):
        """
        Initialisation of the regions
        """
        self.multiworld = multiworld
        self.player = player
        self.options = options
        self.__initialize_rules(self.options)
        self.__create_campaign(1)

