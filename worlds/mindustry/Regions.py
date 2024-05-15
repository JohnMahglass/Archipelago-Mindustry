import json

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
    node_core_shard: Region
    node_conveyor: Region
    node_junction: Region
    node_router: Region
    node_launch_pad: Region
    node_distributor: Region
    node_sorter: Region
    node_inverted_sorter: Region
    node_overflow_gate: Region
    node_underflow_gate: Region
    node_container: Region
    node_unloader: Region
    node_vault: Region
    node_bridge_conveyor: Region
    node_titanium_conveyor: Region
    node_phase_conveyor: Region
    node_mass_driver: Region
    node_payload_conveyor: Region
    node_payload_router: Region
    node_armored_conveyor: Region
    node_plastanium_conveyor: Region
    node_core_foundation: Region
    node_core_nucleus: Region
    node_mechanical_drill: Region
    node_mechanical_pump: Region
    node_conduit: Region
    node_liquid_junction: Region
    node_liquid_router: Region
    node_liquid_container: Region
    node_liquid_tank: Region
    node_bridge_conduit: Region
    node_pulse_conduit: Region
    node_phase_conduit: Region
    node_plated_conduit: Region
    node_rotary_pump: Region
    node_impulse_pump: Region
    node_graphite_press: Region
    node_pneumatic_drill: Region
    node_cultivator: Region
    node_laser_drill: Region
    node_airblast: Region
    node_water_extractor: Region
    node_oil_extractor: Region
    node_pyratite_mixer: Region
    node_blast_mixer: Region
    node_silicon_smelter: Region
    node_spore_press: Region
    node_coal_centrifuge: Region
    node_multi_press: Region
    node_silicon_crucible: Region
    node_plastanium_compressor: Region
    node_phase_weaver: Region
    node_kiln: Region
    node_pulveriser: Region
    node_incinerator: Region
    node_melter: Region
    node_surge_smelter: Region
    node_separator: Region
    node_disassembler: Region
    node_cryofluid_mixer: Region
    node_micro_processor: Region
    node_switch: Region
    node_message: Region
    node_logic_display: Region
    node_large_logic_display: Region
    node_memory_cell: Region
    node_memory_bank: Region
    node_logic_processor: Region
    node_hyper_processor: Region
    node_illuminator: Region
    node_combustion_generator: Region
    node_power_node: Region
    node_large_power_node: Region
    node_battery_diode: Region
    node_surge_tower: Region
    node_battery: Region
    node_large_battery: Region
    node_mender: Region
    node_mend_projector: Region
    node_force_projector: Region
    node_overdrive_projector: Region
    node_overdrive_dome: Region
    node_repair_point: Region
    node_repair_turret: Region
    node_steam_generator: Region
    node_thermal_generator: Region
    node_differential_generator: Region
    node_thorium_reactor: Region
    node_impact_reactor: Region
    node_rtg_generator: Region
    node_solar_panel: Region
    node_large_solar_panel: Region
    node_duo: Region
    node_copper_wall: Region
    node_large_copper_wall: Region
    node_titanium_wall: Region
    node_large_titanium_wall: Region
    node_door: Region
    node_large_door: Region
    node_plastanium_wall: Region
    node_large_plastanium_wall: Region
    node_thorium_wall: Region
    node_large_thorium_wall: Region
    node_surge_wall: Region
    node_large_surge_wall: Region
    node_phase_wall: Region
    node_large_phase_wall: Region
    node_scatter: Region
    node_hail: Region
    node_salvo: Region
    node_swarmer: Region
    node_cyclone: Region
    node_spectre: Region
    node_ripple: Region
    node_fuse: Region
    node_scorch: Region
    node_arc: Region
    node_wave: Region
    node_parallax: Region
    node_segment: Region
    node_tsunami: Region
    node_lancer: Region
    node_meltdown: Region
    node_foreshadow: Region
    node_shock_mine: Region
    node_ground_factory: Region
    node_dagger: Region
    node_mace: Region
    node_fortress: Region
    node_scepter: Region
    node_reign: Region
    node_nova: Region
    node_pulsar: Region
    node_quasar: Region
    node_vela: Region
    node_corvus: Region
    node_crawler: Region
    node_atrax: Region
    node_spiroct: Region
    node_arkyid: Region
    node_toxopid: Region
    node_air_factory: Region
    node_flare: Region
    node_horizon: Region
    node_zenith: Region
    node_antumbra: Region
    node_eclipse: Region
    node_mono: Region
    node_poly: Region
    node_mega: Region
    node_quad: Region
    node_oct: Region
    node_naval_factory: Region
    node_risso: Region
    node_minke: Region
    node_bryde: Region
    node_sei: Region
    node_omura: Region
    node_retusa: Region
    node_oxynoe: Region
    node_cyerce: Region
    node_aegires: Region
    node_narvanax: Region
    node_additive_reconstructor: Region
    node_multiplicative_reconstructor: Region
    node_exponential_reconstructor: Region
    node_tetrative_reconstructor: Region




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
        """
        self.serpulo: Region = self.__add_region("Serpulo", None)
        self.node_core_shard = self.__add_region("Core: Shard", None)
        self.node_conveyor = self.__add_region("Conveyor", None)
        self.node_junction = self.__add_region("Junction", None)
        self.node_router = self.__add_region("Router", None)
        self.node_launch_pad = self.__add_region("Launch Pad", None)
        self.node_distributor = self.__add_region("Distributor", None)
        self.node_sorter = self.__add_region("Sorter", None)
        self.node_inverted_sorter = self.__add_region("Inverted Sorter", None)
        self.node_overflow_gate = self.__add_region("Overflow Gate", None)
        self.node_underflow_gate = self.__add_region("Underflow Gate", None)
        self.node_container = self.__add_region("Container", None)
        self.node_unloader = self.__add_region("Unloader", None)
        self.node_vault = self.__add_region("Vault", None)
        self.node_bridge_conveyor = self.__add_region("Bridge Conveyor", None)
        self.node_titanium_conveyor = self.__add_region("Titanium Conveyor", None)
        self.node_phase_conveyor = self.__add_region("Phase Conveyor", None)
        self.node_mass_driver = self.__add_region("Mass Driver", None)
        self.node_payload_conveyor = self.__add_region("Payload Conveyor", None)
        self.node_payload_router = self.__add_region("Payload Router", None)
        self.node_armored_conveyor = self.__add_region("Armored Conveyor", None)
        self.node_plastanium_conveyor = self.__add_region("Plastanium Conveyor", None)
        self.node_core_foundation = self.__add_region("Core: Foundation", None)
        self.node_core_nucleus = self.__add_region("Core: Nucleus", None)
        self.node_mechanical_drill = self.__add_region("Mechanical Drill", None)
        self.node_mechanical_pump = self.__add_region("Mechanical Pump", None)
        self.node_conduit = self.__add_region("Conduit", None)
        self.node_liquid_junction = self.__add_region("Liquid Junction", None)
        self.node_liquid_router = self.__add_region("Liquid Router", None)
        self.node_liquid_container = self.__add_region("Liquid Container", None)
        self.node_liquid_tank = self.__add_region("Liquid Tank", None)
        self.node_bridge_conduit = self.__add_region("Bridge Conduit", None)
        self.node_pulse_conduit = self.__add_region("Pulse Conduit", None)
        self.node_phase_conduit =  self.__add_region("Phase Conduit", None)
        self.node_plated_conduit = self.__add_region("Plated Conduit", None)
        self.node_rotary_pump = self.__add_region("Rotary Pump", None)
        self.node_impulse_pump = self.__add_region("Impulse Pump", None)
        self.node_graphite_press = self.__add_region("Graphite Press", None)
        self.node_pneumatic_drill = self.__add_region("Pneumatic Drill", None)
        self.node_cultivator = self.__add_region("Cultivator", None)
        self.node_laser_drill = self.__add_region("Laser Drill", None)
        self.node_airblast = self.__add_region("Airblast", None)
        self.node_water_extractor = self.__add_region("Water Extractor", None)
        self.node_oil_extractor = self.__add_region("Oil Extractor", None)
        self.node_pyratite_mixer = self.__add_region("Pyrate Mixer", None)
        self.node_blast_mixer = self.__add_region("Blast Mixer", None)
        self.node_silicon_smelter = self.__add_region("Silicon Smelter", None)
        self.node_spore_press = self.__add_region("Spore Press", None)
        self.node_coal_centrifuge = self.__add_region("Coal Centrifuge", None)
        self.node_multi_press = self.__add_region("Multi Press", None)
        self.node_silicon_crucible = self.__add_region("Silicon Crucible", None)
        self.node_plastanium_compressor = self.__add_region("Plastanium Compressor", None)
        self.node_phase_weaver = self.__add_region("Phase Weaver", None)
        self.node_kiln = self.__add_region("Kiln", None)
        self.node_pulveriser = self.__add_region("Pulveriser", None)
        self.node_incinerator = self.__add_region("Incinerator", None)
        self.node_melter = self.__add_region("Melter", None)
        self.node_surge_smelter = self.__add_region("Surge Smelter", None)
        self.node_separator = self.__add_region("Separator", None)
        self.node_disassembler = self.__add_region("Disassembler", None)
        self.node_cryofluid_mixer = self.__add_region("Cryofluid Mixer", None)
        self.node_micro_processor = self.__add_region("Micro Processor", None)
        self.node_switch = self.__add_region("Switch", None)
        self.node_message = self.__add_region("Message", None)
        self.node_logic_display = self.__add_region("Logic Display", None)
        self.node_large_logic_display = self.__add_region("Large Logic Display", None)
        self.node_memory_cell = self.__add_region("Memory Cell", None)
        self.node_memory_bank = self.__add_region("Memory Bank", None)
        self.node_logic_processor = self.__add_region("Logic Processor", None)
        self.node_hyper_processor = self.__add_region("Hyper Processor", None)
        self.node_illuminator = self.__add_region("Illuminator", None)
        self.node_combustion_generator = self.__add_region("Combustion Generator", None)
        self.node_power_node = self.__add_region("Power Node", None)
        self.node_large_power_node = self.__add_region("Large Power Node", None)
        self.node_battery_diode = self.__add_region("Battery Diode", None)
        self.node_surge_tower = self.__add_region("Surge Tower", None)
        self.node_battery = self.__add_region("Battery", None)
        self.node_large_battery = self.__add_region("Large Battery", None)
        self.node_mender = self.__add_region("Mender", None)
        self.node_mend_projector = self.__add_region("Mend Projector", None)
        self.node_force_projector = self.__add_region("Forced Projector", None)
        self.node_overdrive_projector = self.__add_region("Overdrive Projector", None)
        self.node_overdrive_dome = self.__add_region("Overdrive Dome", None)
        self.node_repair_point = self.__add_region("Repair Point", None)
        self.node_repair_turret = self.__add_region("Repair Turret", None)
        self.node_steam_generator = self.__add_region("Steam Generator", None)
        self.node_thermal_generator = self.__add_region("Thermal Generator", None)
        self.node_impact_reactor = self.__add_region("Impact Reactor", None)
        self.node_rtg_generator = self.__add_region("RTG Generator", None)
        self.node_solar_panel = self.__add_region("Solar Panel", None)
        self.node_large_solar_panel = self.__add_region("Large Solar Panel", None)
        self.node_duo = self.__add_region("Duo", None)
        self.node_copper_wall = self.__add_region("Copper Wall", None)
        self.node_large_copper_wall = self.__add_region("Large Copper Wall", None)
        self.node_titanium_wall = self.__add_region("Titanium Wall", None)
        self.node_large_titanium_wall = self.__add_region("Large Titanium Wall", None)
        self.node_door = self.__add_region("Door", None)
        self.node_large_door = self.__add_region("Large Door", None)
        self.node_plastanium_wall = self.__add_region("Plastanium Wall", None)
        self.node_large_plastanium_wall = self.__add_region("Large Plastanium Wall", None)
        self.node_thorium_wall = self.__add_region("Thorium Wall", None)
        self.node_large_thorium_wall = self.__add_region("Large Thorium Wall", None)
        self.node_surge_wall = self.__add_region("Surge Wall", None)
        self.node_large_surge_wall = self.__add_region("Large Surge Wall", None)
        self.node_phase_wall = self.__add_region("Phase Wall", None)
        self.node_large_phase_wall = self.__add_region("Large Phase Wall", None)
        self.node_scatter = self.__add_region("Scatter", None)
        self.node_hail = self.__add_region("Hail", None)
        self.node_salvo = self.__add_region("Salvo", None)
        self.node_swarmer = self.__add_region("Swarmer", None)
        self.node_cyclone = self.__add_region("Cyclone", None)
        self.node_spectre = self.__add_region("Spectre", None)
        self.node_ripple = self.__add_region("Ripple", None)
        self.node_fuse = self.__add_region("Fuse", None)
        self.node_scorch = self.__add_region("Scorch", None)
        self.node_arc = self.__add_region("Arc", None)
        self.node_wave = self.__add_region("Wave", None)
        self.node_parallax = self.__add_region("Parallax", None)
        self.node_segment = self.__add_region("Segment", None)
        self.node_tsunami = self.__add_region("Tsunami", None)
        self.node_lancer = self.__add_region("Lancer", None)
        self.node_meltdown = self.__add_region("Meltdown", None)
        self.node_foreshadow = self.__add_region("Foreshadow", None)
        self.node_shock_mine = self.__add_region("Shock Mine", None)
        self.node_ground_factory = self.__add_region("Ground Factory", None)
        self.node_dagger = self.__add_region("Dagger", None)
        self.node_mace = self.__add_region("Mace", None)
        self.node_fortress = self.__add_region("Fortress", None)
        self.node_scepter = self.__add_region("Scepter", None)
        self.node_reign = self.__add_region("Reign", None)
        self.node_nova = self.__add_region("Nova", None)
        self.node_pulsar = self.__add_region("Pulsar", None)
        self.node_quasar = self.__add_region("Quasar", None)
        self.node_vela = self.__add_region("Vela", None)
        self.node_corvus = self.__add_region("Corvus", None)
        self.node_crawler = self.__add_region("Crawler", None)
        self.node_atrax = self.__add_region("Atrax", None)
        self.node_spiroct = self.__add_region("Spiroct", None)
        self.node_arkyid = self.__add_region("Arkyid", None)
        self.node_toxopid = self.__add_region("Toxopid", None)
        self.node_air_factory = self.__add_region("Air Factory", None)
        self.node_flare = self.__add_region("Flare", None)
        self.node_horizon = self.__add_region("Horizon", None)
        self.node_zenith = self.__add_region("Zenith", None)
        self.node_antumbra = self.__add_region("Antumbra", None)
        self.node_eclipse = self.__add_region("Eclipse", None)
        self.node_mono = self.__add_region("Mono", None)
        self.node_poly = self.__add_region("Poly", None)
        self.node_mega = self.__add_region("Mega", None)
        self.node_quad = self.__add_region("Quad", None)
        self.node_oct = self.__add_region("Oct", None)
        self.node_naval_factory = self.__add_region("Naval Factory", None)
        self.node_risso = self.__add_region("Risso", None)
        self.node_minke = self.__add_region("Minke", None)
        self.node_bryde = self.__add_region("Bryde", None)
        self.node_sei = self.__add_region("Sei", None)
        self.node_omura = self.__add_region("Omura", None)
        self.node_retusa = self.__add_region("Retusa", None)
        self.node_oxynoe = self.__add_region("Oxynoe", None)
        self.node_cyerce = self.__add_region("Cyerce", None)
        self.node_aegires = self.__add_region("Aegires", None)
        self.node_narvanax = self.__add_region("Narvanax", None)
        self.node_additive_reconstructor = self.__add_region("Additive Reconstructor", None)
        self.node_multiplicative_reconstructor = self.__add_region("Multiplicative Reconstructor", None)
        self.node_exponential_reconstructor = self.__add_region("Exponential Reconstructor", None)
        self.node_tetrative_reconstructor = self.__add_region("Tetrative Reconstructor", None)





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
            case 0:
                self.__create_serpulo_campaign()
                self.__connect_serpulo_campaign()
            case 1:
                self.__create_erekir_campaign()
            case 2:
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
        self.options = MindustryOptions()
        self.__create_campaign(self.options.campaign_choice)

