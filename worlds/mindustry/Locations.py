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

    tech_tree_serpulo = {
        "AP-0-1": mindustry_base_id + 0,

        "AP-1-1": mindustry_base_id + 1,
        "AP-1-2": mindustry_base_id + 2,
        "AP-1-3": mindustry_base_id + 3,
        "AP-1-4": mindustry_base_id + 4,
        "AP-1-5": mindustry_base_id + 5,
        "AP-1-6": mindustry_base_id + 6,
        "AP-1-7": mindustry_base_id + 7,
        "AP-1-8": mindustry_base_id + 8,
        "AP-1-9": mindustry_base_id + 9,
        "AP-1-10": mindustry_base_id + 10,
        "AP-1-11": mindustry_base_id + 11,
        "AP-1-12": mindustry_base_id + 12,
        "AP-1-13": mindustry_base_id + 13,
        "AP-1-14": mindustry_base_id + 14,
        "AP-1-15": mindustry_base_id + 15,
        "AP-1-16": mindustry_base_id + 16,
        "AP-1-17": mindustry_base_id + 17,
        "AP-1-18": mindustry_base_id + 18,
        "AP-1-19": mindustry_base_id + 19,
        "AP-1-20": mindustry_base_id + 20,

        "AP-2-1": mindustry_base_id + 21,
        "AP-2-2": mindustry_base_id + 22,

        "AP-3-1": mindustry_base_id + 23,

        "AP-4-1": mindustry_base_id + 24,
        "AP-4-2": mindustry_base_id + 25,
        "AP-4-3": mindustry_base_id + 26,
        "AP-4-4": mindustry_base_id + 27,
        "AP-4-5": mindustry_base_id + 28,
        "AP-4-6": mindustry_base_id + 29,
        "AP-4-7": mindustry_base_id + 30,
        "AP-4-8": mindustry_base_id + 31,
        "AP-4-9": mindustry_base_id + 32,
        "AP-4-10": mindustry_base_id + 33,
        "AP-4-11": mindustry_base_id + 34,
        "AP-4-12": mindustry_base_id + 35,

        "AP-5-1": mindustry_base_id + 36,

        "AP-6-1": mindustry_base_id + 37,
        "AP-6-2": mindustry_base_id + 38,
        "AP-6-3": mindustry_base_id + 39,
        "AP-6-4": mindustry_base_id + 40,
        "AP-6-5": mindustry_base_id + 41,
        "AP-6-6": mindustry_base_id + 42,

        "AP-7-1": mindustry_base_id + 43,
        "AP-7-2": mindustry_base_id + 44,

        "AP-8-1": mindustry_base_id + 45,

        "AP-9-1": mindustry_base_id + 46,

        "AP-10-1": mindustry_base_id + 47,
        "AP-10-2": mindustry_base_id + 48,
        "AP-10-3": mindustry_base_id + 49,
        "AP-10-4": mindustry_base_id + 50,
        "AP-10-5": mindustry_base_id + 51,
        "AP-10-6": mindustry_base_id + 52,

        "AP-11-1": mindustry_base_id + 53,
        "AP-11-2": mindustry_base_id + 54,
        "AP-11-3": mindustry_base_id + 55,
        "AP-11-4": mindustry_base_id + 56,
        "AP-11-5": mindustry_base_id + 57,
        "AP-11-6": mindustry_base_id + 58,
        "AP-11-7": mindustry_base_id + 59,
        "AP-11-8": mindustry_base_id + 60,

        "AP-12-1": mindustry_base_id + 61,
        "AP-12-2": mindustry_base_id + 62,
        "AP-12-3": mindustry_base_id + 63,
        "AP-12-4": mindustry_base_id + 64,
        "AP-12-5": mindustry_base_id + 64,
        "AP-12-6": mindustry_base_id + 65,
        "AP-12-7": mindustry_base_id + 66,
        "AP-12-8": mindustry_base_id + 67,
        "AP-12-9": mindustry_base_id + 68,

        "AP-13-1": mindustry_base_id + 69,

        "AP-14-1": mindustry_base_id + 70,

        "AP-15-1": mindustry_base_id + 71,

        "AP-16-1": mindustry_base_id + 72,
        "AP-16-2": mindustry_base_id + 73,
        "AP-16-3": mindustry_base_id + 74,

        "AP-17-1": mindustry_base_id + 75,
        "AP-17-2": mindustry_base_id + 76,

        "AP-18-1": mindustry_base_id + 77,
        "AP-18-2": mindustry_base_id + 78,
        "AP-18-3": mindustry_base_id + 79,
        "AP-18-4": mindustry_base_id + 80,
        "AP-18-5": mindustry_base_id + 81,
        "AP-18-6": mindustry_base_id + 82,
        "AP-18-7": mindustry_base_id + 83,

        "AP-19-1": mindustry_base_id + 84,
        "AP-19-2": mindustry_base_id + 85,
        "AP-19-3": mindustry_base_id + 86,
        "AP-19-4": mindustry_base_id + 87,
        "AP-19-5": mindustry_base_id + 88,
        "AP-19-6": mindustry_base_id + 89,

        "AP-20-1": mindustry_base_id + 90,
        "AP-20-2": mindustry_base_id + 91,

        "AP-21-1": mindustry_base_id + 92,

        "AP-22-1": mindustry_base_id + 93,
        "AP-22-2": mindustry_base_id + 94,
        "AP-22-3": mindustry_base_id + 95,
        "AP-22-4": mindustry_base_id + 96,
        "AP-22-5": mindustry_base_id + 97,
        "AP-22-6": mindustry_base_id + 98,
        "AP-22-7": mindustry_base_id + 99,
        "AP-22-8": mindustry_base_id + 100,
        "AP-22-9": mindustry_base_id + 101,
        "AP-22-10": mindustry_base_id + 102,
        "AP-22-11": mindustry_base_id + 103,
        "AP-22-13": mindustry_base_id + 104,
        "AP-22-14": mindustry_base_id + 105,

        "AP-23-1": mindustry_base_id + 106,
        "AP-23-2": mindustry_base_id + 107,
        "AP-23-3": mindustry_base_id + 108,
        "AP-23-4": mindustry_base_id + 109,
        "AP-23-5": mindustry_base_id + 110,
        "AP-23-6": mindustry_base_id + 111,
        "AP-23-7": mindustry_base_id + 112,
        "AP-23-8": mindustry_base_id + 113,

        "AP-24-1": mindustry_base_id + 114,
        "AP-24-2": mindustry_base_id + 115,
        "AP-24-3": mindustry_base_id + 116,
        "AP-24-4": mindustry_base_id + 117,
        "AP-24-5": mindustry_base_id + 118,
        "AP-24-6": mindustry_base_id + 119,
        "AP-24-7": mindustry_base_id + 120,
        "AP-24-8": mindustry_base_id + 120,
        "AP-24-9": mindustry_base_id + 121,
        "AP-24-10": mindustry_base_id + 122,

        "AP-25-1": mindustry_base_id + 123,

        "AP-26-1": mindustry_base_id + 124,
        "AP-26-2": mindustry_base_id + 125,
        "AP-26-3": mindustry_base_id + 126,
        "AP-26-4": mindustry_base_id + 127,
        "AP-26-5": mindustry_base_id + 128,
        "AP-26-6": mindustry_base_id + 129,
        "AP-26-7": mindustry_base_id + 130,
        "AP-26-8": mindustry_base_id + 131,
        "AP-26-9": mindustry_base_id + 132,
        "AP-26-10": mindustry_base_id + 133,
        "AP-26-11": mindustry_base_id + 134,
        "AP-26-12": mindustry_base_id + 135,
        "AP-26-13": mindustry_base_id + 136,
        "AP-26-14": mindustry_base_id + 137,
        "AP-26-15": mindustry_base_id + 138,

        "AP-27-1": mindustry_base_id + 139,

        "AP-28-1": mindustry_base_id + 140,
        "AP-28-2": mindustry_base_id + 141,
        "AP-28-3": mindustry_base_id + 142,
        "AP-28-4": mindustry_base_id + 143,
        "AP-28-5": mindustry_base_id + 144,
        "AP-28-6": mindustry_base_id + 145,
        "AP-28-7": mindustry_base_id + 146,
        "AP-28-8": mindustry_base_id + 147,
        "AP-28-9": mindustry_base_id + 148,
        "AP-28-10": mindustry_base_id + 149,

        "AP-29-1": mindustry_base_id + 150,

        "AP-30-1": mindustry_base_id + 151,
        "AP-30-2": mindustry_base_id + 152,
        "AP-30-3": mindustry_base_id + 153,
        "AP-30-4": mindustry_base_id + 154,
        "AP-30-5": mindustry_base_id + 155,
        "AP-30-6": mindustry_base_id + 156,
        "AP-30-7": mindustry_base_id + 157,
        "AP-30-8": mindustry_base_id + 158,
        "AP-30-9": mindustry_base_id + 159,

        "AP-31-1": mindustry_base_id + 160,
        "AP-31-2": mindustry_base_id + 161,
        "AP-31-3": mindustry_base_id + 162,
        "AP-31-4": mindustry_base_id + 163,

        "AP-32-1":mindustry_base_id + 164,
        "AP-32-2": mindustry_base_id + 165,
        "AP-32-3": mindustry_base_id + 166,
        "AP-32-4": mindustry_base_id + 167,
        "AP-32-5": mindustry_base_id + 168,
        "AP-32-6": mindustry_base_id + 169,
        "AP-32-7": mindustry_base_id + 170,
        "AP-32-8": mindustry_base_id + 171,
        "AP-32-9": mindustry_base_id + 172,
        "AP-32-10": mindustry_base_id + 173,
        "AP-32-11": mindustry_base_id + 174,
        "AP-32-12": mindustry_base_id + 175,
        "AP-32-13": mindustry_base_id + 176,
        "AP-32-14": mindustry_base_id + 177,
        "AP-32-15": mindustry_base_id + 178,
        "AP-32-16": mindustry_base_id + 179,
        "AP-32-17": mindustry_base_id + 180,
        "AP-32-18": mindustry_base_id + 181,
    }

location_table = {
    MindustryLocation.tech_tree_serpulo
}
