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

    tech_tree_serpulo = {
        "Node Conveyor": MINDUSTRY_BASE_ID + 0,
        "Node Junction": MINDUSTRY_BASE_ID + 1,
        "Node Router": MINDUSTRY_BASE_ID + 2,
        "Node Launch Pad": MINDUSTRY_BASE_ID + 3,
        "Node Distributor": MINDUSTRY_BASE_ID + 4,
        "Node Sorter": MINDUSTRY_BASE_ID + 5,
        "Node Inverted Sorter": MINDUSTRY_BASE_ID + 6,
        "Node Overflow Gate": MINDUSTRY_BASE_ID + 7,
        "Node Underflow gate": MINDUSTRY_BASE_ID + 8,
        "Node Container": MINDUSTRY_BASE_ID + 9,
        "Node Unloader": MINDUSTRY_BASE_ID + 10,
        "Node Vault": MINDUSTRY_BASE_ID + 11,
        "Node Bridge Conveyor": MINDUSTRY_BASE_ID + 12,
        "Node Titanium Conveyor": MINDUSTRY_BASE_ID + 13,
        "Node Phase Conveyor": MINDUSTRY_BASE_ID + 14,
        "Node Mass Driver": MINDUSTRY_BASE_ID + 15,
        "Node Payload Conveyor": MINDUSTRY_BASE_ID + 16,
        "Node Payload Router": MINDUSTRY_BASE_ID + 17,
        "Node Armored Conveyor": MINDUSTRY_BASE_ID + 18,
        "Node Plastanium Conveyor": MINDUSTRY_BASE_ID + 19,

        "Node Core: Foundation": MINDUSTRY_BASE_ID + 20,
        "Node Core: Nucleus": MINDUSTRY_BASE_ID + 21,

        "Node Mechanical Drill": MINDUSTRY_BASE_ID + 22,

        "Node Mechanical Pump": MINDUSTRY_BASE_ID + 23,
        "Node Conduit": MINDUSTRY_BASE_ID + 24,
        "Node Liquid Junction": MINDUSTRY_BASE_ID + 25,
        "Node Liquid Router": MINDUSTRY_BASE_ID + 26,
        "Node Liquid Container": MINDUSTRY_BASE_ID + 27,
        "Node Liquid Tank": MINDUSTRY_BASE_ID + 28,
        "Node Bridge Conduit": MINDUSTRY_BASE_ID + 29,
        "Node Pulse Conduit": MINDUSTRY_BASE_ID + 30,
        "Node Phase Conduit": MINDUSTRY_BASE_ID + 31,
        "Node Plated Conduit": MINDUSTRY_BASE_ID + 32,
        "Node Rotary Pump": MINDUSTRY_BASE_ID + 33,
        "Node Impulse Pump": MINDUSTRY_BASE_ID + 34,

        "Node Graphite Press": MINDUSTRY_BASE_ID + 35,

        "Node Pneumatic Drill": MINDUSTRY_BASE_ID + 36,
        "Node Cultivator": MINDUSTRY_BASE_ID + 37,
        "Node Laser Drill": MINDUSTRY_BASE_ID + 38,
        "Node Airblast Drill": MINDUSTRY_BASE_ID + 39,
        "Node Water Extractor": MINDUSTRY_BASE_ID + 40,
        "Node Oil Extractor": MINDUSTRY_BASE_ID + 41,

        "Node Pyratite Mixer": MINDUSTRY_BASE_ID + 42,
        "Node Blast Mixer": MINDUSTRY_BASE_ID + 43,

        "Node Silicon Smelter": MINDUSTRY_BASE_ID + 44,

        "Node Spore Press": MINDUSTRY_BASE_ID + 45,
        "Node Coal Centrifuge": MINDUSTRY_BASE_ID + 46,
        "Node Multi-Press": MINDUSTRY_BASE_ID + 47,
        "Node Silicon Crucible": MINDUSTRY_BASE_ID + 48,
        "Node Plastanium Compressor": MINDUSTRY_BASE_ID + 49,
        "Node Phase Weaver": MINDUSTRY_BASE_ID + 50,

        "Node Kiln": MINDUSTRY_BASE_ID + 51,
        "Node Pulveriser": MINDUSTRY_BASE_ID + 52,
        "Node Incinerator": MINDUSTRY_BASE_ID + 53,
        "Node Melter": MINDUSTRY_BASE_ID + 54,
        "Node Surge Smelter": MINDUSTRY_BASE_ID + 55,
        "Node Separator": MINDUSTRY_BASE_ID + 56,
        "Node Disassembler": MINDUSTRY_BASE_ID + 57,
        "Node Cryofluid Mixer": MINDUSTRY_BASE_ID + 58,

        "Node Micro Processor": MINDUSTRY_BASE_ID + 59,
        "Node Switch": MINDUSTRY_BASE_ID + 60,
        "Node Message": MINDUSTRY_BASE_ID + 61,
        "Node Logic Display": MINDUSTRY_BASE_ID + 62,
        "Node Large Logic Display": MINDUSTRY_BASE_ID + 63,
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
        "Node Meltdown": MINDUSTRY_BASE_ID + 121,
        "Node Foreshadow": MINDUSTRY_BASE_ID + 122,
        "Node Shock Mine": MINDUSTRY_BASE_ID + 123,

        "Node Ground Factory": MINDUSTRY_BASE_ID + 124,

        "Node Dagger": MINDUSTRY_BASE_ID + 125,
        "Node Mace": MINDUSTRY_BASE_ID + 126,
        "Node Fortress": MINDUSTRY_BASE_ID + 127,
        "Node Scepter": MINDUSTRY_BASE_ID + 128,
        "Node Reign": MINDUSTRY_BASE_ID + 129,
        "Node Nova": MINDUSTRY_BASE_ID + 130,
        "Node Pulsar": MINDUSTRY_BASE_ID + 131,
        "Node Quasar": MINDUSTRY_BASE_ID + 132,
        "Node Vela": MINDUSTRY_BASE_ID + 133,
        "Node Corvus": MINDUSTRY_BASE_ID + 134,
        "Node Crawler": MINDUSTRY_BASE_ID + 135,
        "Node Atrax": MINDUSTRY_BASE_ID + 136,
        "Node Spiroct": MINDUSTRY_BASE_ID + 137,
        "Node Arkyid": MINDUSTRY_BASE_ID + 138,
        "Node Toxopid": MINDUSTRY_BASE_ID + 139,

        "Node Air Factory": MINDUSTRY_BASE_ID + 140,

        "Node Flare": MINDUSTRY_BASE_ID + 141,
        "Node Horizon": MINDUSTRY_BASE_ID + 142,
        "Node Zenith": MINDUSTRY_BASE_ID + 143,
        "Node Antumbra": MINDUSTRY_BASE_ID + 144,
        "Node Eclipse": MINDUSTRY_BASE_ID + 145,
        "Node Mono": MINDUSTRY_BASE_ID + 146,
        "Node Poly": MINDUSTRY_BASE_ID + 147,
        "Node Mega": MINDUSTRY_BASE_ID + 148,
        "Node Quad": MINDUSTRY_BASE_ID + 149,
        "Node Oct": MINDUSTRY_BASE_ID + 150,

        "Node Naval Factory": MINDUSTRY_BASE_ID + 151,

        "Node Risso": MINDUSTRY_BASE_ID + 152,
        "Node Minke": MINDUSTRY_BASE_ID + 153,
        "Node Bryde": MINDUSTRY_BASE_ID + 154,
        "Node Sei": MINDUSTRY_BASE_ID + 155,
        "Node Omura": MINDUSTRY_BASE_ID + 156,
        "Node Retusa": MINDUSTRY_BASE_ID + 157,
        "Node Oxynoe": MINDUSTRY_BASE_ID + 158,
        "Node Cyerce": MINDUSTRY_BASE_ID + 159,
        "Node Aegires": MINDUSTRY_BASE_ID + 160,
        "Node Navanax": MINDUSTRY_BASE_ID + 161,

        "Node Additive Reconstructor": MINDUSTRY_BASE_ID + 162,
        "Node Multiplicative Reconstructor": MINDUSTRY_BASE_ID + 163,
        "Node Exponential Reconstructor": MINDUSTRY_BASE_ID + 164,
        "Node Tetrative Reconstructor": MINDUSTRY_BASE_ID + 165,

        "Node Frozen Forest": MINDUSTRY_BASE_ID + 166,
        "Node The Craters": MINDUSTRY_BASE_ID + 167,
        "Node Ruinous Shores": MINDUSTRY_BASE_ID + 168,
        "Node Windswept Islands": MINDUSTRY_BASE_ID + 169,
        "Node Tar Fields": MINDUSTRY_BASE_ID + 170,
        "Node Impact 0078": MINDUSTRY_BASE_ID + 171,
        "Node Desolate Rift": MINDUSTRY_BASE_ID + 172,
        "Node Planetary Launch Terminal": MINDUSTRY_BASE_ID + 173,
        "Node Extraction Outpost": MINDUSTRY_BASE_ID + 174,
        "Node Slat Flats": MINDUSTRY_BASE_ID + 175,
        "Node Coastline": MINDUSTRY_BASE_ID + 176,
        "Node Naval Fortress": MINDUSTRY_BASE_ID + 177,
        "Node Overgrowth": MINDUSTRY_BASE_ID + 178,
        "Node Biomass Synthesis Facility": MINDUSTRY_BASE_ID + 179,
        "Node Stained Mountains": MINDUSTRY_BASE_ID + 180,
        "Node Fungal Pass": MINDUSTRY_BASE_ID + 181,
        "Node Nuclear Production Complex": MINDUSTRY_BASE_ID + 182,
        "Node Lead": MINDUSTRY_BASE_ID + 183,
        "Node Titanium": MINDUSTRY_BASE_ID + 184,
        "Node Cryofluid": MINDUSTRY_BASE_ID + 185,
        "Node Thorium": MINDUSTRY_BASE_ID + 186,
        "Node Surge Alloy": MINDUSTRY_BASE_ID + 187,
        "Node Phase Fabric": MINDUSTRY_BASE_ID + 188,
        "Node Metaglass": MINDUSTRY_BASE_ID + 189,
        "Node Scrap": MINDUSTRY_BASE_ID + 190,
        "Node Slag": MINDUSTRY_BASE_ID + 191,
        "Node Coal": MINDUSTRY_BASE_ID + 192,
        "Node Graphite": MINDUSTRY_BASE_ID + 193,
        "Node Silicon": MINDUSTRY_BASE_ID + 194,
        "Node Pyratite": MINDUSTRY_BASE_ID + 195,
        "Node Blast Compound": MINDUSTRY_BASE_ID + 196,
        "Node Spore Pod": MINDUSTRY_BASE_ID + 197,
        "Node Oil": MINDUSTRY_BASE_ID + 198,
        "Node Plastanium": MINDUSTRY_BASE_ID + 199,
    }


location_table = {
    MindustryLocation.tech_tree_serpulo
}
