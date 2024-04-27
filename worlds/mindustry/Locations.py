from BaseClasses import Location
from Shared import mindustry_base_id

class MindustryLocation(Location):
    """
    Class for a Mindustry Location
    """
    name: str = "Mindustry"

    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        """
        Initialisation of the object
        :param player: the ID of the player
        :param name: the name of the location
        :param code: the ID (or address) of the location (Event if None)
        :param parent: the Region that this location belongs to
        """
        super(MindustryLocation, self).__init__(player, name, code, parent)
        self.event = code is None


"""It might be a good idea to inc the ID at each assignment on initialisation so that adding more locations is easy"""


class MindustryLocation:
    exemple_location = {
        "research_name", mindustry_base_id + 1
    }
    """Not sure about this one below"""
    location_table = {
        exemple_location,
    }
