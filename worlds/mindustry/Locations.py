from BaseClasses import Location
from worlds.mindustry.Shared import MINDUSTRY_BASE_ID

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

class MindustryLocations:

    serpulo_conveyor = {
        "Node Conveyor": MINDUSTRY_BASE_ID + 0,
    }
    serpulo_junction = {
        "Node Junction": MINDUSTRY_BASE_ID + 1,
    }
    serpulo_router = {
        "Node Router": MINDUSTRY_BASE_ID + 2,
    }
    serpulo_launch_pad = {
        "Node Launch Pad": MINDUSTRY_BASE_ID + 3,
    }
    serpulo_distributor = {
        "Node Distributor": MINDUSTRY_BASE_ID + 4,
    }
    serpulo_sorter = {
        "Node Sorter": MINDUSTRY_BASE_ID + 5,
    }
    serpulo_inverted_sorter = {
        "Node Inverted Sorter": MINDUSTRY_BASE_ID + 6,
    }
    serpulo_overflow_gate = {
        "Node Overflow Gate": MINDUSTRY_BASE_ID + 7,
    }
    serpulo_underflow_gate = {
        "Node Underflow gate": MINDUSTRY_BASE_ID + 8,
    }
    serpulo_container = {
        "Node Container": MINDUSTRY_BASE_ID + 9,
    }
    serpulo_unloader = {
        "Node Unloader": MINDUSTRY_BASE_ID + 10,
    }
    serpulo_vault = {
        "Node Vault": MINDUSTRY_BASE_ID + 11,
    }
    serpulo_bridge_conveyor = {
        "Node Bridge Conveyor": MINDUSTRY_BASE_ID + 12,
    }
    serpulo_titanium_conveyor = {
        "Node Titanium Conveyor": MINDUSTRY_BASE_ID + 13,
    }
    serpulo_phase_conveyor = {
        "Node Phase Conveyor": MINDUSTRY_BASE_ID + 14,
    }
    serpulo_mass_driver = {
        "Node Mass Driver": MINDUSTRY_BASE_ID + 15,
    }
    serpulo_payload_conveyor = {
        "Node Payload Conveyor": MINDUSTRY_BASE_ID + 16,
    }
    serpulo_payload_router = {
        "Node Payload Router": MINDUSTRY_BASE_ID + 17,
    }
    serpulo_armored_conveyor = {
        "Node Armored Conveyor": MINDUSTRY_BASE_ID + 18,
    }
    serpulo_plastanium_conveyor = {
        "Node Plastanium Conveyor": MINDUSTRY_BASE_ID + 19,
    }
    serpulo_core_foundation = {
        "Node Core: Foundation": MINDUSTRY_BASE_ID + 20,
    }
    serpulo_core_nucleus = {
        "Node Core: Nucleus": MINDUSTRY_BASE_ID + 21,
    }
    serpulo_mechanical_drill = {
        "Node Mechanical Drill": MINDUSTRY_BASE_ID + 22,
    }
    serpulo_mechanical_pump = {
        "Node Mechanical Pump": MINDUSTRY_BASE_ID + 23,
    }
    serpulo_conduit = {
        "Node Conduit": MINDUSTRY_BASE_ID + 24,
    }
    serpulo_liquid_junction = {
        "Node Liquid Junction": MINDUSTRY_BASE_ID + 25,
    }
    serpulo_liquid_router = {
        "Node Liquid Router": MINDUSTRY_BASE_ID + 26,
    }
    serpulo_liquid_container = {
        "Node Liquid Container": MINDUSTRY_BASE_ID + 27,
    }
    serpulo_liquid_tank = {
        "Node Liquid Tank": MINDUSTRY_BASE_ID + 28,
    }
    serpulo_bridge_conduit = {
        "Node Bridge Conduit": MINDUSTRY_BASE_ID + 29,
        }
    serpulo_pulse_conduit = {
        "Node Pulse Conduit": MINDUSTRY_BASE_ID + 30,
        }
    serpulo_phase_conduit = {
        "Node Phase Conduit": MINDUSTRY_BASE_ID + 31,
    }
    serpulo_plated_conduit = {
        "Node Plated Conduit": MINDUSTRY_BASE_ID + 32,
    }
    serpulo_rotary_pump = {
        "Node Rotary Pump": MINDUSTRY_BASE_ID + 33,
    }
    serpulo_impulse_pump = {
        "Node Impulse Pump": MINDUSTRY_BASE_ID + 34,
    }
    serpulo_graphite_press = {
        "Node Graphite Press": MINDUSTRY_BASE_ID + 35,
    }
    serpulo_pneumatic_drill = {
        "Node Pneumatic Drill": MINDUSTRY_BASE_ID + 36,
    }
    serpulo_cultivator = {
        "Node Cultivator": MINDUSTRY_BASE_ID + 37,
    }
    serpulo_laser_drill = {
        "Node Laser Drill": MINDUSTRY_BASE_ID + 38,
    }
    serpulo_airblast_drill = {
        "Node Airblast Drill": MINDUSTRY_BASE_ID + 39,
    }
    serpulo_water_extractor = {
        "Node Water Extractor": MINDUSTRY_BASE_ID + 40,
    }
    serpulo_oil_extractor = {
        "Node Oil Extractor": MINDUSTRY_BASE_ID + 41,
    }
    serpulo_pyratite_mixer = {
        "Node Pyratite Mixer": MINDUSTRY_BASE_ID + 42,
    }
    serpulo_blast_mixer = {
        "Node Blast Mixer": MINDUSTRY_BASE_ID + 43,
    }
    serpulo_silicon_smelter = {
        "Node Silicon Smelter": MINDUSTRY_BASE_ID + 44,
    }
    serpulo_spore_press = {
        "Node Spore Press": MINDUSTRY_BASE_ID + 45,
    }
    serpulo_coal_centrifuge = {
        "Node Coal Centrifuge": MINDUSTRY_BASE_ID + 46,
    }
    serpulo_multi_press = {
        "Node Multi-Press": MINDUSTRY_BASE_ID + 47,
    }
    serpulo_silicon_crucible = {
        "Node Silicon Crucible": MINDUSTRY_BASE_ID + 48,
    }
    serpulo_plastanium_compressor = {
        "Node Plastanium Compressor": MINDUSTRY_BASE_ID + 49,
    }
    serpulo_phase_weaver = {
        "Node Phase Weaver": MINDUSTRY_BASE_ID + 50,
    }
    serpulo_kiln = {
        "Node Kiln": MINDUSTRY_BASE_ID + 51,
    }
    serpulo_pulveriser = {
        "Node Pulveriser": MINDUSTRY_BASE_ID + 52,
    }
    serpulo_incinerator = {
        "Node Incinerator": MINDUSTRY_BASE_ID + 53,
    }
    serpulo_melter = {
        "Node Melter": MINDUSTRY_BASE_ID + 54,
    }
    serpulo_surge_smelter = {
        "Node Surge Smelter": MINDUSTRY_BASE_ID + 55,
    }
    serpulo_separator = {
        "Node Separator": MINDUSTRY_BASE_ID + 56,
    }
    serpulo_disassembler = {
        "Node Disassembler": MINDUSTRY_BASE_ID + 57,
    }
    serpulo_cryofluid_mixer = {
        "Node Cryofluid Mixer": MINDUSTRY_BASE_ID + 58,
    }
    serpulo_micro_processor = {
        "Node Micro Processor": MINDUSTRY_BASE_ID + 59,
    }
    serpulo_switch = {
        "Node Switch": MINDUSTRY_BASE_ID + 60,
    }
    serpulo_message = {
        "Node Message": MINDUSTRY_BASE_ID + 61,
    }
    serpulo_logic_display = {
        "Node Logic Display": MINDUSTRY_BASE_ID + 62,
    }
    serpulo_large_logic_display = {
        "Node Large Logic Display": MINDUSTRY_BASE_ID + 63,
    }
    serpulo_memory_cell = {
        "Node Memory Cell": MINDUSTRY_BASE_ID + 64,
    }
    serpulo_memory_bank = {
        "Node Memory Bank": MINDUSTRY_BASE_ID + 65,
    }
    serpulo_logic_processor = {
        "Node Logic Processor": MINDUSTRY_BASE_ID + 66,
    }
    serpulo_hyper_processor = {
        "Node Hyper Processor": MINDUSTRY_BASE_ID + 67,
    }
    serpulo_illuminator = {
        "Node Illuminator": MINDUSTRY_BASE_ID + 68,
    }
    serpulo_combustion_generator = {
        "Node Combustion Generator": MINDUSTRY_BASE_ID + 69,
    }
    serpulo_power_node = {
        "Node Power Node": MINDUSTRY_BASE_ID + 70,
    }
    serpulo_large_power_node = {
        "Node Large Power Node": MINDUSTRY_BASE_ID + 71,
    }
    serpulo_battery_diode = {
        "Node Battery Diode": MINDUSTRY_BASE_ID + 72,
    }
    serpulo_surge_tower = {
        "Node Surge Tower": MINDUSTRY_BASE_ID + 73,
    }
    serpulo_battery = {
        "Node Battery": MINDUSTRY_BASE_ID + 74,
    }
    serpulo_large_battery = {
        "Node Large Battery": MINDUSTRY_BASE_ID + 75,
    }
    serpulo_mender = {
        "Node Mender": MINDUSTRY_BASE_ID + 76,
    }
    serpulo_mend_projector = {
        "Node Mend Projector": MINDUSTRY_BASE_ID + 77,
    }
    serpulo_force_projector = {
        "Node Force Projector": MINDUSTRY_BASE_ID + 78,
    }
    serpulo_overdrive_projector = {
        "Node Overdrive Projector": MINDUSTRY_BASE_ID + 79,
    }
    serpulo_overdrive_dome = {
        "Node Overdrive Dome": MINDUSTRY_BASE_ID + 80,
    }
    serpulo_repair_point = {
        "Node Repair Point": MINDUSTRY_BASE_ID + 81,
    }
    serpulo_repair_turret = {
        "Node Repair Turret": MINDUSTRY_BASE_ID + 82,
    }
    serpulo_steam_generator = {
        "Node Steam Generator": MINDUSTRY_BASE_ID + 83,
    }
    serpulo_thermal_generator = {
        "Node Thermal Generator": MINDUSTRY_BASE_ID + 84,
    }
    serpulo_differential_generator = {
        "Node Differential Generator": MINDUSTRY_BASE_ID + 85,
    }
    serpulo_thorium_reactor = {
        "Node Thorium Reactor": MINDUSTRY_BASE_ID + 86,
    }
    serpulo_impact_reactor = {
        "Node Impact Reactor": MINDUSTRY_BASE_ID + 87,
    }
    serpulo_rtg_generator = {
        "Node RTG Generator": MINDUSTRY_BASE_ID + 88,
    }
    serpulo_solar_panel = {
        "Node Solar Panel": MINDUSTRY_BASE_ID + 89,
    }
    serpulo_large_solar_panel = {
        "Node Large Solar Panel": MINDUSTRY_BASE_ID + 90,
    }
    serpulo_duo = {
        "Node Duo": MINDUSTRY_BASE_ID + 91,
    }
    serpulo_copper_wall = {
        "Node Copper Wall": MINDUSTRY_BASE_ID + 92,
    }
    serpulo_large_copper_wall = {
        "Node Large Copper Wall": MINDUSTRY_BASE_ID + 93,
    }
    serpulo_titanium_wall = {
        "Node Titanium Wall": MINDUSTRY_BASE_ID + 94,
    }
    serpulo_large_titanium_wall = {
        "Node Large Titanium Wall": MINDUSTRY_BASE_ID + 95,
    }
    serpulo_door = {
        "Node Door": MINDUSTRY_BASE_ID + 96,
    }
    serpulo_large_door = {
        "Node Large Door": MINDUSTRY_BASE_ID + 97,
    }
    serpulo_plastanium_wall = {
        "Node Plastanium Wall": MINDUSTRY_BASE_ID + 98,
    }
    serpulo_large_plastanium_wall = {
        "Node Large Plastanium Wall": MINDUSTRY_BASE_ID + 99,
    }
    serpulo_thorium_wall = {
        "Node Thorium Wall": MINDUSTRY_BASE_ID + 100,
    }
    serpulo_large_thorium_wall = {
        "Node Large Thorium Wall": MINDUSTRY_BASE_ID + 101,
    }
    serpulo_surge_wall = {
        "Node Surge Wall": MINDUSTRY_BASE_ID + 102,
    }
    serpulo_large_surge_wall = {
        "Node Large Surge Wall": MINDUSTRY_BASE_ID + 103,
    }
    serpulo_phase_wall = {
        "Node Phase Wall": MINDUSTRY_BASE_ID + 104,
    }
    serpulo_large_phase_wall = {
        "Node Large Phase Wall": MINDUSTRY_BASE_ID + 105,
    }
    serpulo_scatter = {
        "Node Scatter": MINDUSTRY_BASE_ID + 106,
    }
    serpulo_hail = {
        "Node Hail": MINDUSTRY_BASE_ID + 107,
    }
    serpulo_salvo = {
        "Node Salvo": MINDUSTRY_BASE_ID + 108,
    }
    serpulo_swarmer = {
        "Node Swarmer": MINDUSTRY_BASE_ID + 109,
    }
    serpulo_cyclone = {
        "Node Cyclone": MINDUSTRY_BASE_ID + 110,
    }
    serpulo_spectre = {
        "Node Spectre": MINDUSTRY_BASE_ID + 111,
    }
    serpulo_ripple = {
        "Node Ripple": MINDUSTRY_BASE_ID + 112,
    }
    serpulo_fuse = {
        "Node Fuse": MINDUSTRY_BASE_ID + 113,
    }
    serpulo_scorch = {
        "Node Scorch": MINDUSTRY_BASE_ID + 114,
    }
    serpulo_arc = {
        "Node Arc": MINDUSTRY_BASE_ID + 115,
    }
    serpulo_wave = {
        "Node Wave": MINDUSTRY_BASE_ID + 116,
    }
    serpulo_parallax = {
        "Node Parallax": MINDUSTRY_BASE_ID + 117,
    }
    serpulo_segment = {
        "Node Segment": MINDUSTRY_BASE_ID + 118,
    }
    serpulo_tsunami = {
        "Node Tsunami": MINDUSTRY_BASE_ID + 119,
    }
    serpulo_lancer = {
        "Node Lancer": MINDUSTRY_BASE_ID + 120,
    }
    serpulo_meltdown = {
        "Node Meltdown": MINDUSTRY_BASE_ID + 121,
    }
    serpulo_foreshadow = {
        "Node Foreshadow": MINDUSTRY_BASE_ID + 122,
    }
    serpulo_shock_mine = {
        "Node Shock Mine": MINDUSTRY_BASE_ID + 123,
    }
    serpulo_ground_factory = {
        "Node Ground Factory": MINDUSTRY_BASE_ID + 124,
    }
    serpulo_dagger = {
        "Node Dagger": MINDUSTRY_BASE_ID + 125,
    }
    serpulo_mace = {
        "Node Mace": MINDUSTRY_BASE_ID + 126,
    }
    serpulo_fortress = {
        "Node Fortress": MINDUSTRY_BASE_ID + 127,
    }
    serpulo_scepter = {
        "Node Scepter": MINDUSTRY_BASE_ID + 128,
    }
    serpulo_reign = {
        "Node Reign": MINDUSTRY_BASE_ID + 129,
    }
    serpulo_nova = {
        "Node Nova": MINDUSTRY_BASE_ID + 130,
    }
    serpulo_pulsar = {
        "Node Pulsar": MINDUSTRY_BASE_ID + 131,
    }
    serpulo_quasar = {
        "Node Quasar": MINDUSTRY_BASE_ID + 132,
    }
    serpulo_vela = {
        "Node Vela": MINDUSTRY_BASE_ID + 133,
    }
    serpulo_corvus = {
        "Node Corvus": MINDUSTRY_BASE_ID + 134,
    }
    serpulo_crawler = {
        "Node Crawler": MINDUSTRY_BASE_ID + 135,
    }
    serpulo_atrax = {
        "Node Atrax": MINDUSTRY_BASE_ID + 136,
    }
    serpulo_spiroct = {
        "Node Spiroct": MINDUSTRY_BASE_ID + 137,
    }
    serpulo_arkyid = {
        "Node Arkyid": MINDUSTRY_BASE_ID + 138,
    }
    serpulo_toxopid = {
        "Node Toxopid": MINDUSTRY_BASE_ID + 139,
    }
    serpulo_air_factory = {
        "Node Air Factory": MINDUSTRY_BASE_ID + 140,
    }
    serpulo_flare = {
        "Node Flare": MINDUSTRY_BASE_ID + 141,
    }
    serpulo_horizon = {
        "Node Horizon": MINDUSTRY_BASE_ID + 142,
    }
    serpulo_zenith = {
        "Node Zenith": MINDUSTRY_BASE_ID + 143,
    }
    serpulo_antumbra = {
        "Node Antumbra": MINDUSTRY_BASE_ID + 144,
    }
    serpulo_eclipse = {
        "Node Eclipse": MINDUSTRY_BASE_ID + 145,
    }
    serpulo_mono = {
        "Node Mono": MINDUSTRY_BASE_ID + 146,
    }
    serpulo_poly = {
        "Node Poly": MINDUSTRY_BASE_ID + 147,
    }
    serpulo_mega = {
        "Node Mega": MINDUSTRY_BASE_ID + 148,
    }
    serpulo_quad = {
        "Node Quad": MINDUSTRY_BASE_ID + 149,
    }
    serpulo_oct = {
        "Node Oct": MINDUSTRY_BASE_ID + 150,
    }
    serpulo_naval_factory = {
        "Node Naval Factory": MINDUSTRY_BASE_ID + 151,
    }
    serpulo_risso = {
        "Node Risso": MINDUSTRY_BASE_ID + 152,
    }
    serpulo_minke = {
        "Node Minke": MINDUSTRY_BASE_ID + 153,
    }
    serpulo_bryde = {
        "Node Bryde": MINDUSTRY_BASE_ID + 154,
    }
    serpulo_sei = {
        "Node Sei": MINDUSTRY_BASE_ID + 155,
    }
    serpulo_omura = {
        "Node Omura": MINDUSTRY_BASE_ID + 156,
    }
    serpulo_retusa = {
        "Node Retusa": MINDUSTRY_BASE_ID + 157,
    }
    serpulo_oxynoe = {
        "Node Oxynoe": MINDUSTRY_BASE_ID + 158,
    }
    serpulo_cyerce = {
        "Node Cyerce": MINDUSTRY_BASE_ID + 159,
    }
    serpulo_aegires = {
        "Node Aegires": MINDUSTRY_BASE_ID + 160,
    }
    serpulo_navanax = {
        "Node Navanax": MINDUSTRY_BASE_ID + 161,
    }
    serpulo_additive_reconstructor = {
        "Node Additive Reconstructor": MINDUSTRY_BASE_ID + 162,
    }
    serpulo_multiplicative_reconstructor = {
        "Node Multiplicative Reconstructor": MINDUSTRY_BASE_ID + 163,
    }
    serpulo_exponential_reconstructor = {
        "Node Exponential Reconstructor": MINDUSTRY_BASE_ID + 164,
    }
    serpulo_tetrative_reconstructor = {
        "Node Tetrative Reconstructor": MINDUSTRY_BASE_ID + 165,
    }
    #serpulo_frozen_forest = {
    #    "Node Frozen Forest": MINDUSTRY_BASE_ID + 166,
    #}
    #serpulo_the_craters = {
    #    "Node The Craters": MINDUSTRY_BASE_ID + 167,
    #}
    #serpulo_ruinous_shores = {
    #    "Node Ruinous Shores": MINDUSTRY_BASE_ID + 168,
    #}
    #serpulo_windswept_islands = {
    #    "Node Windswept Islands": MINDUSTRY_BASE_ID + 169,
    #}
    #serpulo_tar_fields = {
    #    "Node Tar Fields": MINDUSTRY_BASE_ID + 170,
    #}
    #serpulo_impact_0078 = {
    #    "Node Impact 0078": MINDUSTRY_BASE_ID + 171,
    #}
    #serpulo_desolate_rift = {
    #    "Node Desolate Rift": MINDUSTRY_BASE_ID + 172,
    #}
    #serpulo_planetary_launch_terminal = {
    #    "Node Planetary Launch Terminal": MINDUSTRY_BASE_ID + 173,
    #}
    #serpulo_extraction_outpost = {
    #    "Node Extraction Outpost": MINDUSTRY_BASE_ID + 174,
    #}
    #serpulo_salt_flats = {
    #    "Node Slat Flats": MINDUSTRY_BASE_ID + 175,
    #}
    #serpulo_coastline = {
    #    "Node Coastline": MINDUSTRY_BASE_ID + 176,
    #}
    #serpulo_naval_fortress = {
    #    "Node Naval Fortress": MINDUSTRY_BASE_ID + 177,
    #}
    #serpulo_overgrowth = {
    #    "Node Overgrowth": MINDUSTRY_BASE_ID + 178,
    #}
    #serpulo_biomass_synthesis_facility = {
    #    "Node Biomass Synthesis Facility": MINDUSTRY_BASE_ID + 179,
    #}
    #serpulo_stained_mountains = {
    #    "Node Stained Mountains": MINDUSTRY_BASE_ID + 180,
    #}
    #serpulo_fungal_pass = {
    #    "Node Fungal Pass": MINDUSTRY_BASE_ID + 181,
    #}
    #serpulo_nuclear_production_complex = {
    #    "Node Nuclear Production Complex": MINDUSTRY_BASE_ID + 182,
    #}
    #serpulo_lead = {
    #    "Node Lead": MINDUSTRY_BASE_ID + 183,
    #}
    #serpulo_titanium = {
    #    "Node Titanium": MINDUSTRY_BASE_ID + 184,
    #}
    #serpulo_cryofluid = {
    #    "Node Cryofluid": MINDUSTRY_BASE_ID + 185,
    #}
    #serpulo_thorium = {
    #    "Node Thorium": MINDUSTRY_BASE_ID + 186,
    #}
    #serpulo_surge_alloy = {
    #    "Node Surge Alloy": MINDUSTRY_BASE_ID + 187,
    #}
    #serpulo_phase_fabric = {
    #    "Node Phase Fabric": MINDUSTRY_BASE_ID + 188,
    #}
    #serpulo_metaglass = {
    #    "Node Metaglass": MINDUSTRY_BASE_ID + 189,
    #}
    #serpulo_scrap = {
    #    "Node Scrap": MINDUSTRY_BASE_ID + 190,
    #}
    #serpulo_slag = {
    #    "Node Slag": MINDUSTRY_BASE_ID + 191,
    #}
    #serpulo_coal = {
    #    "Node Coal": MINDUSTRY_BASE_ID + 192,
    #}
    #serpulo_graphite = {
    #    "Node Graphite": MINDUSTRY_BASE_ID + 193,
    #}
    #serpulo_silicon = {
    #    "Node Silicon": MINDUSTRY_BASE_ID + 194,
    #}
    #serpulo_pyratite = {
    #    "Node Pyratite": MINDUSTRY_BASE_ID + 195,
    #}
    #serpulo_blast_compound = {
    #    "Node Blast Compound": MINDUSTRY_BASE_ID + 196,
    #}
    #serpulo_spore_pod = {
    #    "Node Spore Pod": MINDUSTRY_BASE_ID + 197,
    #}
    #serpulo_oil = {
    #    "Node Oil": MINDUSTRY_BASE_ID + 198,
    #}
    #serpulo_plastanium = {
    #    "Node Plastanium": MINDUSTRY_BASE_ID + 199,
    #}

location_table = {
    **MindustryLocations.serpulo_conveyor,
    **MindustryLocations.serpulo_junction,
    **MindustryLocations.serpulo_router,
    **MindustryLocations.serpulo_launch_pad,
    **MindustryLocations.serpulo_distributor,
    **MindustryLocations.serpulo_sorter,
    **MindustryLocations.serpulo_inverted_sorter,
    **MindustryLocations.serpulo_overflow_gate,
    **MindustryLocations.serpulo_underflow_gate,
    **MindustryLocations.serpulo_container,
    **MindustryLocations.serpulo_unloader,
    **MindustryLocations.serpulo_vault,
    **MindustryLocations.serpulo_bridge_conveyor,
    **MindustryLocations.serpulo_titanium_conveyor,
    **MindustryLocations.serpulo_phase_conveyor,
    **MindustryLocations.serpulo_mass_driver,
    **MindustryLocations.serpulo_payload_conveyor,
    **MindustryLocations.serpulo_payload_router,
    **MindustryLocations.serpulo_armored_conveyor,
    **MindustryLocations.serpulo_plastanium_conveyor,
    **MindustryLocations.serpulo_core_foundation,
    **MindustryLocations.serpulo_core_nucleus,
    **MindustryLocations.serpulo_mechanical_drill,
    **MindustryLocations.serpulo_mechanical_pump,
    **MindustryLocations.serpulo_conduit,
    **MindustryLocations.serpulo_liquid_junction,
    **MindustryLocations.serpulo_liquid_router,
    **MindustryLocations.serpulo_liquid_container,
    **MindustryLocations.serpulo_liquid_tank,
    **MindustryLocations.serpulo_bridge_conduit,
    **MindustryLocations.serpulo_pulse_conduit,
    **MindustryLocations.serpulo_phase_conduit,
    **MindustryLocations.serpulo_plated_conduit,
    **MindustryLocations.serpulo_rotary_pump,
    **MindustryLocations.serpulo_impulse_pump,
    **MindustryLocations.serpulo_graphite_press,
    **MindustryLocations.serpulo_pneumatic_drill,
    **MindustryLocations.serpulo_cultivator,
    **MindustryLocations.serpulo_laser_drill,
    **MindustryLocations.serpulo_airblast_drill,
    **MindustryLocations.serpulo_water_extractor,
    **MindustryLocations.serpulo_oil_extractor,
    **MindustryLocations.serpulo_pyratite_mixer,
    **MindustryLocations.serpulo_blast_mixer,
    **MindustryLocations.serpulo_silicon_smelter,
    **MindustryLocations.serpulo_spore_press,
    **MindustryLocations.serpulo_coal_centrifuge,
    **MindustryLocations.serpulo_multi_press,
    **MindustryLocations.serpulo_silicon_crucible,
    **MindustryLocations.serpulo_plastanium_compressor,
    **MindustryLocations.serpulo_phase_weaver,
    **MindustryLocations.serpulo_kiln,
    **MindustryLocations.serpulo_pulveriser,
    **MindustryLocations.serpulo_incinerator,
    **MindustryLocations.serpulo_melter,
    **MindustryLocations.serpulo_surge_smelter,
    **MindustryLocations.serpulo_separator,
    **MindustryLocations.serpulo_disassembler,
    **MindustryLocations.serpulo_cryofluid_mixer,
    **MindustryLocations.serpulo_micro_processor,
    **MindustryLocations.serpulo_switch,
    **MindustryLocations.serpulo_message,
    **MindustryLocations.serpulo_logic_display,
    **MindustryLocations.serpulo_large_logic_display,
    **MindustryLocations.serpulo_memory_cell,
    **MindustryLocations.serpulo_memory_bank,
    **MindustryLocations.serpulo_logic_processor,
    **MindustryLocations.serpulo_hyper_processor,
    **MindustryLocations.serpulo_illuminator,
    **MindustryLocations.serpulo_combustion_generator,
    **MindustryLocations.serpulo_power_node,
    **MindustryLocations.serpulo_large_power_node,
    **MindustryLocations.serpulo_battery_diode,
    **MindustryLocations.serpulo_surge_tower,
    **MindustryLocations.serpulo_battery,
    **MindustryLocations.serpulo_large_battery,
    **MindustryLocations.serpulo_mender,
    **MindustryLocations.serpulo_mend_projector,
    **MindustryLocations.serpulo_force_projector,
    **MindustryLocations.serpulo_overdrive_projector,
    **MindustryLocations.serpulo_overdrive_dome,
    **MindustryLocations.serpulo_repair_point,
    **MindustryLocations.serpulo_repair_turret,
    **MindustryLocations.serpulo_steam_generator,
    **MindustryLocations.serpulo_thermal_generator,
    **MindustryLocations.serpulo_differential_generator,
    **MindustryLocations.serpulo_thorium_reactor,
    **MindustryLocations.serpulo_impact_reactor,
    **MindustryLocations.serpulo_rtg_generator,
    **MindustryLocations.serpulo_solar_panel,
    **MindustryLocations.serpulo_large_solar_panel,
    **MindustryLocations.serpulo_duo,
    **MindustryLocations.serpulo_copper_wall,
    **MindustryLocations.serpulo_large_copper_wall,
    **MindustryLocations.serpulo_titanium_wall,
    **MindustryLocations.serpulo_large_titanium_wall,
    **MindustryLocations.serpulo_door,
    **MindustryLocations.serpulo_large_door,
    **MindustryLocations.serpulo_plastanium_wall,
    **MindustryLocations.serpulo_large_plastanium_wall,
    **MindustryLocations.serpulo_thorium_wall,
    **MindustryLocations.serpulo_large_thorium_wall,
    **MindustryLocations.serpulo_surge_wall,
    **MindustryLocations.serpulo_large_surge_wall,
    **MindustryLocations.serpulo_phase_wall,
    **MindustryLocations.serpulo_large_phase_wall,
    **MindustryLocations.serpulo_scatter,
    **MindustryLocations.serpulo_hail,
    **MindustryLocations.serpulo_salvo,
    **MindustryLocations.serpulo_swarmer,
    **MindustryLocations.serpulo_cyclone,
    **MindustryLocations.serpulo_spectre,
    **MindustryLocations.serpulo_ripple,
    **MindustryLocations.serpulo_fuse,
    **MindustryLocations.serpulo_scorch,
    **MindustryLocations.serpulo_arc,
    **MindustryLocations.serpulo_wave,
    **MindustryLocations.serpulo_parallax,
    **MindustryLocations.serpulo_segment,
    **MindustryLocations.serpulo_tsunami,
    **MindustryLocations.serpulo_lancer,
    **MindustryLocations.serpulo_meltdown,
    **MindustryLocations.serpulo_foreshadow,
    **MindustryLocations.serpulo_shock_mine,
    **MindustryLocations.serpulo_ground_factory,
    **MindustryLocations.serpulo_dagger,
    **MindustryLocations.serpulo_mace,
    **MindustryLocations.serpulo_fortress,
    **MindustryLocations.serpulo_scepter,
    **MindustryLocations.serpulo_reign,
    **MindustryLocations.serpulo_nova,
    **MindustryLocations.serpulo_pulsar,
    **MindustryLocations.serpulo_quasar,
    **MindustryLocations.serpulo_vela,
    **MindustryLocations.serpulo_corvus,
    **MindustryLocations.serpulo_crawler,
    **MindustryLocations.serpulo_atrax,
    **MindustryLocations.serpulo_spiroct,
    **MindustryLocations.serpulo_arkyid,
    **MindustryLocations.serpulo_toxopid,
    **MindustryLocations.serpulo_air_factory,
    **MindustryLocations.serpulo_flare,
    **MindustryLocations.serpulo_horizon,
    **MindustryLocations.serpulo_zenith,
    **MindustryLocations.serpulo_antumbra,
    **MindustryLocations.serpulo_eclipse,
    **MindustryLocations.serpulo_mono,
    **MindustryLocations.serpulo_poly,
    **MindustryLocations.serpulo_mega,
    **MindustryLocations.serpulo_quad,
    **MindustryLocations.serpulo_oct,
    **MindustryLocations.serpulo_naval_factory,
    **MindustryLocations.serpulo_risso,
    **MindustryLocations.serpulo_minke,
    **MindustryLocations.serpulo_bryde,
    **MindustryLocations.serpulo_sei,
    **MindustryLocations.serpulo_omura,
    **MindustryLocations.serpulo_retusa,
    **MindustryLocations.serpulo_oxynoe,
    **MindustryLocations.serpulo_cyerce,
    **MindustryLocations.serpulo_aegires,
    **MindustryLocations.serpulo_navanax,
    **MindustryLocations.serpulo_additive_reconstructor,
    **MindustryLocations.serpulo_multiplicative_reconstructor,
    **MindustryLocations.serpulo_exponential_reconstructor,
    **MindustryLocations.serpulo_tetrative_reconstructor,
    #**MindustryLocations.serpulo_frozen_forest,
    #**MindustryLocations.serpulo_the_craters,
    #**MindustryLocations.serpulo_ruinous_shores,
    #**MindustryLocations.serpulo_windswept_islands,
    #**MindustryLocations.serpulo_tar_fields,
    #**MindustryLocations.serpulo_impact_0078,
    #**MindustryLocations.serpulo_desolate_rift,
    #**MindustryLocations.serpulo_planetary_launch_terminal,
    #**MindustryLocations.serpulo_extraction_outpost,
    #**MindustryLocations.serpulo_salt_flats,
    #**MindustryLocations.serpulo_coastline,
    #**MindustryLocations.serpulo_naval_fortress,
    #**MindustryLocations.serpulo_overgrowth,
    #**MindustryLocations.serpulo_biomass_synthesis_facility,
    #**MindustryLocations.serpulo_stained_mountains,
    #**MindustryLocations.serpulo_fungal_pass,
    #**MindustryLocations.serpulo_nuclear_production_complex,
    #**MindustryLocations.serpulo_lead,
    #**MindustryLocations.serpulo_titanium,
    #**MindustryLocations.serpulo_cryofluid,
    #**MindustryLocations.serpulo_thorium,
    #**MindustryLocations.serpulo_surge_alloy,
    #**MindustryLocations.serpulo_phase_fabric,
    #**MindustryLocations.serpulo_metaglass,
    #**MindustryLocations.serpulo_scrap,
    #**MindustryLocations.serpulo_slag,
    #**MindustryLocations.serpulo_coal,
    #**MindustryLocations.serpulo_graphite,
    #**MindustryLocations.serpulo_silicon,
    #**MindustryLocations.serpulo_pyratite,
    #**MindustryLocations.serpulo_blast_compound,
    #**MindustryLocations.serpulo_spore_pod,
    #**MindustryLocations.serpulo_oil,
    #**MindustryLocations.serpulo_plastanium,
}
