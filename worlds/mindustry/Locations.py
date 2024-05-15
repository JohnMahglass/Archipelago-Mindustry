from BaseClasses import Location
from Shared import MINDUSTRY_BASE_ID

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
        "Node Core: Shard": MINDUSTRY_BASE_ID + 0,

        "Node Conveyor": MINDUSTRY_BASE_ID + 1,
        "Node Junction": MINDUSTRY_BASE_ID + 2,
        "Node Router": MINDUSTRY_BASE_ID + 3,
        "Node Launch Pad": MINDUSTRY_BASE_ID + 4,
        "Node Distributor": MINDUSTRY_BASE_ID + 5,
        "Node Sorter": MINDUSTRY_BASE_ID + 6,
        "Node Inverted Sorter": MINDUSTRY_BASE_ID + 7,
        "Node Overflow Gate": MINDUSTRY_BASE_ID + 8,
        "Node Underflow gate": MINDUSTRY_BASE_ID + 9,
        "Node Container": MINDUSTRY_BASE_ID + 10,
        "Node Unloader": MINDUSTRY_BASE_ID + 11,
        "Node Vault": MINDUSTRY_BASE_ID + 12,
        "Node Bridge Conveyor": MINDUSTRY_BASE_ID + 13,
        "Node Titanium Conveyor": MINDUSTRY_BASE_ID + 14,
        "Node Phase Conveyor": MINDUSTRY_BASE_ID + 15,
        "Node Mass Driver": MINDUSTRY_BASE_ID + 16,
        "Node Payload Conveyor": MINDUSTRY_BASE_ID + 17,
        "Node Payload Router": MINDUSTRY_BASE_ID + 18,
        "Node Armored Conveyor": MINDUSTRY_BASE_ID + 19,
        "Node Plastanium Conveyor": MINDUSTRY_BASE_ID + 20,

        "Node Core: Foundation": MINDUSTRY_BASE_ID + 21,
        "Node Core: Nucleus": MINDUSTRY_BASE_ID + 22,

        "Node Mechanical Drill": MINDUSTRY_BASE_ID + 23,

        "Node Mechanical Pump": MINDUSTRY_BASE_ID + 24,
        "Node Conduit": MINDUSTRY_BASE_ID + 25,
        "Node Liquid Junction": MINDUSTRY_BASE_ID + 26,
        "Node Liquid Router": MINDUSTRY_BASE_ID + 27,
        "Node Liquid Container": MINDUSTRY_BASE_ID + 28,
        "Node Liquid Tank": MINDUSTRY_BASE_ID + 29,
        "Node Bridge Conduit": MINDUSTRY_BASE_ID + 30,
        "Node Pulse Conduit": MINDUSTRY_BASE_ID + 31,
        "Node Phase Conduit": MINDUSTRY_BASE_ID + 32,
        "Node Plated Conduit": MINDUSTRY_BASE_ID + 33,
        "Node Rotary Pump": MINDUSTRY_BASE_ID + 34,
        "Node Impulse Pump": MINDUSTRY_BASE_ID + 35,

        "Node Graphite Press": MINDUSTRY_BASE_ID + 36,

        "Node Pneumatic Drill": MINDUSTRY_BASE_ID + 37,
        "Node Cultivator": MINDUSTRY_BASE_ID + 38,
        "Node Laser Drill": MINDUSTRY_BASE_ID + 39,
        "Node Airblast": MINDUSTRY_BASE_ID + 40,
        "Node Water Extractor": MINDUSTRY_BASE_ID + 41,
        "Node Oil Extractor": MINDUSTRY_BASE_ID + 42,

        "Node Pyratite Mixer": MINDUSTRY_BASE_ID + 43,
        "Node Blast Mixer": MINDUSTRY_BASE_ID + 44,

        "Node Silicon Smelter": MINDUSTRY_BASE_ID + 45,

        "Node Spore Press": MINDUSTRY_BASE_ID + 46,
        "Node Coal Centrifuge": MINDUSTRY_BASE_ID + 47,
        "Node Multi-Press": MINDUSTRY_BASE_ID + 48,
        "Node Silicon Crucible": MINDUSTRY_BASE_ID + 49,
        "Node Plastanium Compressor": MINDUSTRY_BASE_ID + 50,
        "Node Phase Weaver": MINDUSTRY_BASE_ID + 51,

        "Node Kiln": MINDUSTRY_BASE_ID + 52,
        "Node Pulveriser": MINDUSTRY_BASE_ID + 53,
        "Node Incinerator": MINDUSTRY_BASE_ID + 54,
        "Node Melter": MINDUSTRY_BASE_ID + 55,
        "Node Surge Smelter": MINDUSTRY_BASE_ID + 56,
        "Node Separator": MINDUSTRY_BASE_ID + 57,
        "Node Disassembler": MINDUSTRY_BASE_ID + 58,
        "Node Cryofluid Mixer": MINDUSTRY_BASE_ID + 59,

        "Node Micro Processor": MINDUSTRY_BASE_ID + 60,
        "Node Switch": MINDUSTRY_BASE_ID + 61,
        "Node Message": MINDUSTRY_BASE_ID + 62,
        "Node Logic Display": MINDUSTRY_BASE_ID + 63,
        "Node Large Logic Display": MINDUSTRY_BASE_ID + 64,
        "Node Memory Cell": MINDUSTRY_BASE_ID + 64,
        "Node Memory Bank": MINDUSTRY_BASE_ID + 65,
        "Node Logic Processor": MINDUSTRY_BASE_ID + 66,
        "Node Hyper Processor": MINDUSTRY_BASE_ID + 67,

        "Node Illuminator": MINDUSTRY_BASE_ID + 68,

        "Node Combustion Generator": MINDUSTRY_BASE_ID + 69,

        "Node Power Node": MINDUSTRY_BASE_ID + 70,

        "Node Large Power Node": MINDUSTRY_BASE_ID + 71,
        "Node Battery Diode": MINDUSTRY_BASE_ID + 72,
        "Node Surge Tower": MINDUSTRY_BASE_ID + 73,

        "Node Battery": MINDUSTRY_BASE_ID + 74,
        "Node Large Battery": MINDUSTRY_BASE_ID + 75,

        "Node Mender": MINDUSTRY_BASE_ID + 76,
        "Node Mend Projector": MINDUSTRY_BASE_ID + 77,
        "Node Force Projector": MINDUSTRY_BASE_ID + 78,
        "Node Overdrive Projector": MINDUSTRY_BASE_ID + 79,
        "Node Overdrive Dome": MINDUSTRY_BASE_ID + 80,
        "Node Repair Point": MINDUSTRY_BASE_ID + 81,
        "Node Repair Turret": MINDUSTRY_BASE_ID + 82,

        "Node Steam Generator": MINDUSTRY_BASE_ID + 83,
        "Node Thermal Generator": MINDUSTRY_BASE_ID + 84,
        "Node Differential Generator": MINDUSTRY_BASE_ID + 85,
        "Node Thorium Reactor": MINDUSTRY_BASE_ID + 86,
        "Node Impact Reactor": MINDUSTRY_BASE_ID + 87,
        "Node RTG Generator": MINDUSTRY_BASE_ID + 88,

        "Node Solar Panel": MINDUSTRY_BASE_ID + 89,
        "Node Large Solar Panel": MINDUSTRY_BASE_ID + 90,

        "Node Duo": MINDUSTRY_BASE_ID + 91,

        "Node Copper Wall": MINDUSTRY_BASE_ID + 92,
        "Node Large Copper Wall": MINDUSTRY_BASE_ID + 93,
        "Node Titanium Wall": MINDUSTRY_BASE_ID + 94,
        "Node Large Titanium Wall": MINDUSTRY_BASE_ID + 95,
        "Node Door": MINDUSTRY_BASE_ID + 96,
        "Node Large Door": MINDUSTRY_BASE_ID + 97,
        "Node Plastanium Wall": MINDUSTRY_BASE_ID + 98,
        "Node Large Plastanium Wall": MINDUSTRY_BASE_ID + 99,
        "Node Thorium Wall": MINDUSTRY_BASE_ID + 100,
        "Node Large Thorium Wall": MINDUSTRY_BASE_ID + 101,
        "Node Surge Wall": MINDUSTRY_BASE_ID + 102,
        "Node Large Surge Wall": MINDUSTRY_BASE_ID + 103,
        "Node Phase Wall": MINDUSTRY_BASE_ID + 104,
        "Node Large Phase Wall": MINDUSTRY_BASE_ID + 105,

        "Node Scatter": MINDUSTRY_BASE_ID + 106,
        "Node Hail": MINDUSTRY_BASE_ID + 107,
        "Node Salvo": MINDUSTRY_BASE_ID + 108,
        "Node Swarmer": MINDUSTRY_BASE_ID + 109,
        "Node Cyclone": MINDUSTRY_BASE_ID + 110,
        "Node Spectre": MINDUSTRY_BASE_ID + 111,
        "Node Ripple": MINDUSTRY_BASE_ID + 112,
        "Node Fuse": MINDUSTRY_BASE_ID + 113,

        "Node Scorch": MINDUSTRY_BASE_ID + 114,
        "Node Arc": MINDUSTRY_BASE_ID + 115,
        "Node Wave": MINDUSTRY_BASE_ID + 116,
        "Node Parallax": MINDUSTRY_BASE_ID + 117,
        "Node Segment": MINDUSTRY_BASE_ID + 118,
        "Node Tsunami": MINDUSTRY_BASE_ID + 119,
        "Node Lancer": MINDUSTRY_BASE_ID + 120,
        "Node Meltdown": MINDUSTRY_BASE_ID + 120,
        "Node Foreshadow": MINDUSTRY_BASE_ID + 121,
        "Node Shock Mine": MINDUSTRY_BASE_ID + 122,

        "Node Ground Factory": MINDUSTRY_BASE_ID + 123,

        "Node Dagger": MINDUSTRY_BASE_ID + 124,
        "Node Mace": MINDUSTRY_BASE_ID + 125,
        "Node Fortress": MINDUSTRY_BASE_ID + 126,
        "Node Scepter": MINDUSTRY_BASE_ID + 127,
        "Node Reign": MINDUSTRY_BASE_ID + 128,
        "Node Nova": MINDUSTRY_BASE_ID + 129,
        "Node Pulsar": MINDUSTRY_BASE_ID + 130,
        "Node Quasar": MINDUSTRY_BASE_ID + 131,
        "Node Vela": MINDUSTRY_BASE_ID + 132,
        "Node Corvus": MINDUSTRY_BASE_ID + 133,
        "Node Crawler": MINDUSTRY_BASE_ID + 134,
        "Node Atrax": MINDUSTRY_BASE_ID + 135,
        "Node Spiroct": MINDUSTRY_BASE_ID + 136,
        "Node Arkyid": MINDUSTRY_BASE_ID + 137,
        "Node Toxopid": MINDUSTRY_BASE_ID + 138,

        "Node Air Factory": MINDUSTRY_BASE_ID + 139,

        "Node Flare": MINDUSTRY_BASE_ID + 140,
        "Node Horizon": MINDUSTRY_BASE_ID + 141,
        "Node Zenith": MINDUSTRY_BASE_ID + 142,
        "Node Antumbra": MINDUSTRY_BASE_ID + 143,
        "Node Eclipse": MINDUSTRY_BASE_ID + 144,
        "Node Mono": MINDUSTRY_BASE_ID + 145,
        "Node Poly": MINDUSTRY_BASE_ID + 146,
        "Node Mega": MINDUSTRY_BASE_ID + 147,
        "Node Quad": MINDUSTRY_BASE_ID + 148,
        "Node Oct": MINDUSTRY_BASE_ID + 149,

        "Node Naval Factory": MINDUSTRY_BASE_ID + 150,

        "Node Risso": MINDUSTRY_BASE_ID + 151,
        "Node Minke": MINDUSTRY_BASE_ID + 152,
        "Node Bryde": MINDUSTRY_BASE_ID + 153,
        "Node Sei": MINDUSTRY_BASE_ID + 154,
        "Node Omura": MINDUSTRY_BASE_ID + 155,
        "Node Retusa": MINDUSTRY_BASE_ID + 156,
        "Node Oxynoe": MINDUSTRY_BASE_ID + 157,
        "Node Cyerce": MINDUSTRY_BASE_ID + 158,
        "Node Aegires": MINDUSTRY_BASE_ID + 159,
        "Node Narvanax": MINDUSTRY_BASE_ID + 160,

        "Node Additive Reconstructor": MINDUSTRY_BASE_ID + 161,
        "Node Multiplicative Reconstructor": MINDUSTRY_BASE_ID + 162,
        "Node Exponential Reconstructor": MINDUSTRY_BASE_ID + 163,
        "Node Tetrative Reconstructor": MINDUSTRY_BASE_ID + 164,
    }

location_table = {
    MindustryLocation.tech_tree_serpulo
}
