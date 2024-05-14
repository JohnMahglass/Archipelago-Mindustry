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

class MindustryLocation:

    locations_copper = {

    }

    locations_ground_zero = {

    }



    tech_tree_serpulo = {
        "AP-S-0-1": mindustry_base_id + 0,

        "AP-S-1-1": mindustry_base_id + 1,
        "AP-S-1-2": mindustry_base_id + 2,
        "AP-S-1-3": mindustry_base_id + 3,
        "AP-S-1-4": mindustry_base_id + 4,
        "AP-S-1-5": mindustry_base_id + 5,
        "AP-S-1-6": mindustry_base_id + 6,
        "AP-S-1-7": mindustry_base_id + 7,
        "AP-S-1-8": mindustry_base_id + 8,
        "AP-S-1-9": mindustry_base_id + 9,
        "AP-S-1-10": mindustry_base_id + 10,
        "AP-S-1-11": mindustry_base_id + 11,
        "AP-S-1-12": mindustry_base_id + 12,
        "AP-S-1-13": mindustry_base_id + 13,
        "AP-S-1-14": mindustry_base_id + 14,
        "AP-S-1-15": mindustry_base_id + 15,
        "AP-S-1-16": mindustry_base_id + 16,
        "AP-S-1-17": mindustry_base_id + 17,
        "AP-S-1-18": mindustry_base_id + 18,
        "AP-S-1-19": mindustry_base_id + 19,
        "AP-S-1-20": mindustry_base_id + 20,

        "AP-S-2-1": mindustry_base_id + 21,
        "AP-S-2-2": mindustry_base_id + 22,

        "AP-S-3-1": mindustry_base_id + 23,

        "AP-S-4-1": mindustry_base_id + 24,
        "AP-S-4-2": mindustry_base_id + 25,
        "AP-S-4-3": mindustry_base_id + 26,
        "AP-S-4-4": mindustry_base_id + 27,
        "AP-S-4-5": mindustry_base_id + 28,
        "AP-S-4-6": mindustry_base_id + 29,
        "AP-S-4-7": mindustry_base_id + 30,
        "AP-S-4-8": mindustry_base_id + 31,
        "AP-S-4-9": mindustry_base_id + 32,
        "AP-S-4-10": mindustry_base_id + 33,
        "AP-S-4-11": mindustry_base_id + 34,
        "AP-S-4-12": mindustry_base_id + 35,

        "AP-S-5-1": mindustry_base_id + 36,

        "AP-S-6-1": mindustry_base_id + 37,
        "AP-S-6-2": mindustry_base_id + 38,
        "AP-S-6-3": mindustry_base_id + 39,
        "AP-S-6-4": mindustry_base_id + 40,
        "AP-S-6-5": mindustry_base_id + 41,
        "AP-S-6-6": mindustry_base_id + 42,

        "AP-S-7-1": mindustry_base_id + 43,
        "AP-S-7-2": mindustry_base_id + 44,

        "AP-S-8-1": mindustry_base_id + 45,

        "AP-S-9-1": mindustry_base_id + 46,

        "AP-S-10-1": mindustry_base_id + 47,
        "AP-S-10-2": mindustry_base_id + 48,
        "AP-S-10-3": mindustry_base_id + 49,
        "AP-S-10-4": mindustry_base_id + 50,
        "AP-S-10-5": mindustry_base_id + 51,
        "AP-S-10-6": mindustry_base_id + 52,

        "AP-S-11-1": mindustry_base_id + 53,
        "AP-S-11-2": mindustry_base_id + 54,
        "AP-S-11-3": mindustry_base_id + 55,
        "AP-S-11-4": mindustry_base_id + 56,
        "AP-S-11-5": mindustry_base_id + 57,
        "AP-S-11-6": mindustry_base_id + 58,
        "AP-S-11-7": mindustry_base_id + 59,
        "AP-S-11-8": mindustry_base_id + 60,

        "AP-S-12-1": mindustry_base_id + 61,
        "AP-S-12-2": mindustry_base_id + 62,
        "AP-S-12-3": mindustry_base_id + 63,
        "AP-S-12-4": mindustry_base_id + 64,
        "AP-S-12-5": mindustry_base_id + 64,
        "AP-S-12-6": mindustry_base_id + 65,
        "AP-S-12-7": mindustry_base_id + 66,
        "AP-S-12-8": mindustry_base_id + 67,
        "AP-S-12-9": mindustry_base_id + 68,

        "AP-S-13-1": mindustry_base_id + 69,

        "AP-S-14-1": mindustry_base_id + 70,

        "AP-S-15-1": mindustry_base_id + 71,

        "AP-S-16-1": mindustry_base_id + 72,
        "AP-S-16-2": mindustry_base_id + 73,
        "AP-S-16-3": mindustry_base_id + 74,

        "AP-S-17-1": mindustry_base_id + 75,
        "AP-S-17-2": mindustry_base_id + 76,

        "AP-S-18-1": mindustry_base_id + 77,
        "AP-S-18-2": mindustry_base_id + 78,
        "AP-S-18-3": mindustry_base_id + 79,
        "AP-S-18-4": mindustry_base_id + 80,
        "AP-S-18-5": mindustry_base_id + 81,
        "AP-S-18-6": mindustry_base_id + 82,
        "AP-S-18-7": mindustry_base_id + 83,

        "AP-S-19-1": mindustry_base_id + 84,
        "AP-S-19-2": mindustry_base_id + 85,
        "AP-S-19-3": mindustry_base_id + 86,
        "AP-S-19-4": mindustry_base_id + 87,
        "AP-S-19-5": mindustry_base_id + 88,
        "AP-S-19-6": mindustry_base_id + 89,

        "AP-S-20-1": mindustry_base_id + 90,
        "AP-S-20-2": mindustry_base_id + 91,

        "AP-S-21-1": mindustry_base_id + 92,

        "AP-S-22-1": mindustry_base_id + 93,
        "AP-S-22-2": mindustry_base_id + 94,
        "AP-S-22-3": mindustry_base_id + 95,
        "AP-S-22-4": mindustry_base_id + 96,
        "AP-S-22-5": mindustry_base_id + 97,
        "AP-S-22-6": mindustry_base_id + 98,
        "AP-S-22-7": mindustry_base_id + 99,
        "AP-S-22-8": mindustry_base_id + 100,
        "AP-S-22-9": mindustry_base_id + 101,
        "AP-S-22-10": mindustry_base_id + 102,
        "AP-S-22-11": mindustry_base_id + 103,
        "AP-S-22-13": mindustry_base_id + 104,
        "AP-S-22-14": mindustry_base_id + 105,

        "AP-S-23-1": mindustry_base_id + 106,
        "AP-S-23-2": mindustry_base_id + 107,
        "AP-S-23-3": mindustry_base_id + 108,
        "AP-S-23-4": mindustry_base_id + 109,
        "AP-S-23-5": mindustry_base_id + 110,
        "AP-S-23-6": mindustry_base_id + 111,
        "AP-S-23-7": mindustry_base_id + 112,
        "AP-S-23-8": mindustry_base_id + 113,

        "AP-S-24-1": mindustry_base_id + 114,
        "AP-S-24-2": mindustry_base_id + 115,
        "AP-S-24-3": mindustry_base_id + 116,
        "AP-S-24-4": mindustry_base_id + 117,
        "AP-S-24-5": mindustry_base_id + 118,
        "AP-S-24-6": mindustry_base_id + 119,
        "AP-S-24-7": mindustry_base_id + 120,
        "AP-S-24-8": mindustry_base_id + 120,
        "AP-S-24-9": mindustry_base_id + 121,
        "AP-S-24-10": mindustry_base_id + 122,

        "AP-S-25-1": mindustry_base_id + 123,

        "AP-S-26-1": mindustry_base_id + 124,
        "AP-S-26-2": mindustry_base_id + 125,
        "AP-S-26-3": mindustry_base_id + 126,
        "AP-S-26-4": mindustry_base_id + 127,
        "AP-S-26-5": mindustry_base_id + 128,
        "AP-S-26-6": mindustry_base_id + 129,
        "AP-S-26-7": mindustry_base_id + 130,
        "AP-S-26-8": mindustry_base_id + 131,
        "AP-S-26-9": mindustry_base_id + 132,
        "AP-S-26-10": mindustry_base_id + 133,
        "AP-S-26-11": mindustry_base_id + 134,
        "AP-S-26-12": mindustry_base_id + 135,
        "AP-S-26-13": mindustry_base_id + 136,
        "AP-S-26-14": mindustry_base_id + 137,
        "AP-S-26-15": mindustry_base_id + 138,

        "AP-S-27-1": mindustry_base_id + 139,

        "AP-S-28-1": mindustry_base_id + 140,
        "AP-S-28-2": mindustry_base_id + 141,
        "AP-S-28-3": mindustry_base_id + 142,
        "AP-S-28-4": mindustry_base_id + 143,
        "AP-S-28-5": mindustry_base_id + 144,
        "AP-S-28-6": mindustry_base_id + 145,
        "AP-S-28-7": mindustry_base_id + 146,
        "AP-S-28-8": mindustry_base_id + 147,
        "AP-S-28-9": mindustry_base_id + 148,
        "AP-S-28-10": mindustry_base_id + 149,

        "AP-S-29-1": mindustry_base_id + 150,

        "AP-S-30-1": mindustry_base_id + 151,
        "AP-S-30-2": mindustry_base_id + 152,
        "AP-S-30-3": mindustry_base_id + 153,
        "AP-S-30-4": mindustry_base_id + 154,
        "AP-S-30-5": mindustry_base_id + 155,
        "AP-S-30-6": mindustry_base_id + 156,
        "AP-S-30-7": mindustry_base_id + 157,
        "AP-S-30-8": mindustry_base_id + 158,
        "AP-S-30-9": mindustry_base_id + 159,

        "AP-S-31-1": mindustry_base_id + 160,
        "AP-S-31-2": mindustry_base_id + 161,
        "AP-S-31-3": mindustry_base_id + 162,
        "AP-S-31-4": mindustry_base_id + 163,
    }

location_table = {
    MindustryLocation.tech_tree_serpulo
}
