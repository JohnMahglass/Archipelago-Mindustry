from BaseClasses import Region, MultiWorld


class MindustryRegions:
    """
    Class used to create region for Mindustry
    """

    menu: Region
    """Additional region should be added here once they are decided"""

    multiworld: MultiWorld
    """
    Current Multiworld game
    """

    player: int
    """
    Player Id
    """

    def __init__(self, multiworld: MultiWorld, player: int):
        """
        Initialisation of the regions
        """
        self.multiworld = multiworld
        self.player = player
        """Actual region initialisation goes here"""
