import json

from BaseClasses import Region, MultiWorld, Entrance
from .Options import MindustryOptions
from .Locations import MindustryLocation
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

    def connect_regions(self) -> None:
        if self.options.campaign_choice == 0:
            self.__connect_serpulo_campaign()
        elif self.options.campaign_choice == 1:
            self.__connect_erekir_campaign()
        elif self.options.campaign_choice == 2:
            self.__connect_all_campaign()
        else:
            raise ValueError("Invalid campaign choice")



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
        self.node_core_shard = self.__add_region("Core: Shard", MindustryLocation.tech_tree_serpulo.get("Node Core: Shard"))
        self.node_conveyor = self.__add_region("Conveyor", MindustryLocation.tech_tree_serpulo.get("Node Conveyor"))
        self.node_junction = self.__add_region("Junction", MindustryLocation.tech_tree_serpulo.get("Node Junction"))
        self.node_router = self.__add_region("Router", MindustryLocation.tech_tree_serpulo.get("Node Router"))
        self.node_launch_pad = self.__add_region("Launch Pad", MindustryLocation.tech_tree_serpulo.get("Node Launch Pad"))
        self.node_distributor = self.__add_region("Distributor", MindustryLocation.tech_tree_serpulo.get("Node Distributor"))
        self.node_sorter = self.__add_region("Sorter", MindustryLocation.tech_tree_serpulo.get("Node Sorter"))
        self.node_inverted_sorter = self.__add_region("Inverted Sorter", MindustryLocation.tech_tree_serpulo.get("Node Inverted Sorter"))
        self.node_overflow_gate = self.__add_region("Overflow Gate", MindustryLocation.tech_tree_serpulo.get("Node Overflow Gate"))
        self.node_underflow_gate = self.__add_region("Underflow Gate", MindustryLocation.tech_tree_serpulo.get("Node Underflow Gate"))
        self.node_container = self.__add_region("Container", MindustryLocation.tech_tree_serpulo.get("Node Container"))
        self.node_unloader = self.__add_region("Unloader", MindustryLocation.tech_tree_serpulo.get("Node Unloader"))
        self.node_vault = self.__add_region("Vault", MindustryLocation.tech_tree_serpulo.get("Node Vault"))
        self.node_bridge_conveyor = self.__add_region("Bridge Conveyor", MindustryLocation.tech_tree_serpulo.get("Node Bridge Conveyor"))
        self.node_titanium_conveyor = self.__add_region("Titanium Conveyor", MindustryLocation.tech_tree_serpulo.get("Node Titanium Conveyor"))
        self.node_phase_conveyor = self.__add_region("Phase Conveyor", MindustryLocation.tech_tree_serpulo.get("Node Phase Conveyor"))
        self.node_mass_driver = self.__add_region("Mass Driver", MindustryLocation.tech_tree_serpulo.get("Node Mass Driver"))
        self.node_payload_conveyor = self.__add_region("Payload Conveyor", MindustryLocation.tech_tree_serpulo.get("Node Payload Conveyor"))
        self.node_payload_router = self.__add_region("Payload Router", MindustryLocation.tech_tree_serpulo.get("Node Payload Router"))
        self.node_armored_conveyor = self.__add_region("Armored Conveyor", MindustryLocation.tech_tree_serpulo.get("Node Armored Conveyor"))
        self.node_plastanium_conveyor = self.__add_region("Plastanium Conveyor", MindustryLocation.tech_tree_serpulo.get("Node Plastanium Conveyor"))
        self.node_core_foundation = self.__add_region("Core: Foundation", MindustryLocation.tech_tree_serpulo.get("Node Core: Foundation"))
        self.node_core_nucleus = self.__add_region("Core: Nucleus", MindustryLocation.tech_tree_serpulo.get("Node Core: Nucleus"))
        self.node_mechanical_drill = self.__add_region("Mechanical Drill", MindustryLocation.tech_tree_serpulo.get("Node Mechanical Drill"))
        self.node_mechanical_pump = self.__add_region("Mechanical Pump", MindustryLocation.tech_tree_serpulo.get("Node Mechanical Pump"))
        self.node_conduit = self.__add_region("Conduit", MindustryLocation.tech_tree_serpulo.get("Node Conduit"))
        self.node_liquid_junction = self.__add_region("Liquid Junction", MindustryLocation.tech_tree_serpulo.get("Node Liquid Junction"))
        self.node_liquid_router = self.__add_region("Liquid Router", MindustryLocation.tech_tree_serpulo.get("Node Liquid Router"))
        self.node_liquid_container = self.__add_region("Liquid Container", MindustryLocation.tech_tree_serpulo.get("Node Liquid Container"))
        self.node_liquid_tank = self.__add_region("Liquid Tank", MindustryLocation.tech_tree_serpulo.get("Node Liquid Tank"))
        self.node_bridge_conduit = self.__add_region("Bridge Conduit", MindustryLocation.tech_tree_serpulo.get("Node Bridge Conduit"))
        self.node_pulse_conduit = self.__add_region("Pulse Conduit", MindustryLocation.tech_tree_serpulo.get("Node Pulse Conduit"))
        self.node_phase_conduit =  self.__add_region("Phase Conduit", MindustryLocation.tech_tree_serpulo.get("Node Phase Conduit"))
        self.node_plated_conduit = self.__add_region("Plated Conduit", MindustryLocation.tech_tree_serpulo.get("Node Plated Conduit"))
        self.node_rotary_pump = self.__add_region("Rotary Pump", MindustryLocation.tech_tree_serpulo.get("Node Rotary Pump"))
        self.node_impulse_pump = self.__add_region("Impulse Pump", MindustryLocation.tech_tree_serpulo.get("Node Impulse Pump"))
        self.node_graphite_press = self.__add_region("Graphite Press", MindustryLocation.tech_tree_serpulo.get("Node Graphite Press"))
        self.node_pneumatic_drill = self.__add_region("Pneumatic Drill", MindustryLocation.tech_tree_serpulo.get("Node Pneumatic Drill"))
        self.node_cultivator = self.__add_region("Cultivator", MindustryLocation.tech_tree_serpulo.get("Node Cultivator"))
        self.node_laser_drill = self.__add_region("Laser Drill", MindustryLocation.tech_tree_serpulo.get("Node Laser Drill"))
        self.node_airblast = self.__add_region("Airblast", MindustryLocation.tech_tree_serpulo.get("Node Airblast"))
        self.node_water_extractor = self.__add_region("Water Extractor", MindustryLocation.tech_tree_serpulo.get("Node Water Extractor"))
        self.node_oil_extractor = self.__add_region("Oil Extractor", MindustryLocation.tech_tree_serpulo.get("Node Oil Extractor"))
        self.node_pyratite_mixer = self.__add_region("Pyrate Mixer", MindustryLocation.tech_tree_serpulo.get("Node Pyrate Mixer"))
        self.node_blast_mixer = self.__add_region("Blast Mixer", MindustryLocation.tech_tree_serpulo.get("Node Blast Mixer"))
        self.node_silicon_smelter = self.__add_region("Silicon Smelter", MindustryLocation.tech_tree_serpulo.get("Node Silicon Smelter"))
        self.node_spore_press = self.__add_region("Spore Press", MindustryLocation.tech_tree_serpulo.get("Node Spore Press"))
        self.node_coal_centrifuge = self.__add_region("Coal Centrifuge", MindustryLocation.tech_tree_serpulo.get("Node Coal Centrifuge"))
        self.node_multi_press = self.__add_region("Multi Press", MindustryLocation.tech_tree_serpulo.get("Node Multi Press"))
        self.node_silicon_crucible = self.__add_region("Silicon Crucible", MindustryLocation.tech_tree_serpulo.get("Node Silicon Crucible"))
        self.node_plastanium_compressor = self.__add_region("Plastanium Compressor", MindustryLocation.tech_tree_serpulo.get("Node Plastanium Compressor"))
        self.node_phase_weaver = self.__add_region("Phase Weaver", MindustryLocation.tech_tree_serpulo.get("Node Phase Weaver"))
        self.node_kiln = self.__add_region("Kiln", MindustryLocation.tech_tree_serpulo.get("Node Kiln"))
        self.node_pulveriser = self.__add_region("Pulveriser", MindustryLocation.tech_tree_serpulo.get("Node Pulveriser"))
        self.node_incinerator = self.__add_region("Incinerator", MindustryLocation.tech_tree_serpulo.get("Node Incinerator"))
        self.node_melter = self.__add_region("Melter", MindustryLocation.tech_tree_serpulo.get("Node Melter"))
        self.node_surge_smelter = self.__add_region("Surge Smelter", MindustryLocation.tech_tree_serpulo.get("Node Surge Smelter"))
        self.node_separator = self.__add_region("Separator", MindustryLocation.tech_tree_serpulo.get("Node Separator"))
        self.node_disassembler = self.__add_region("Disassembler", MindustryLocation.tech_tree_serpulo.get("Node Disassembler"))
        self.node_cryofluid_mixer = self.__add_region("Cryofluid Mixer", MindustryLocation.tech_tree_serpulo.get("Node Cryofluid Mixer"))
        self.node_micro_processor = self.__add_region("Micro Processor", MindustryLocation.tech_tree_serpulo.get("Node Micro Processor"))
        self.node_switch = self.__add_region("Switch", MindustryLocation.tech_tree_serpulo.get("Node Switch"))
        self.node_message = self.__add_region("Message", MindustryLocation.tech_tree_serpulo.get("Node Message"))
        self.node_logic_display = self.__add_region("Logic Display", MindustryLocation.tech_tree_serpulo.get("Node Logic Display"))
        self.node_large_logic_display = self.__add_region("Large Logic Display", MindustryLocation.tech_tree_serpulo.get("Node Large logic Display"))
        self.node_memory_cell = self.__add_region("Memory Cell", MindustryLocation.tech_tree_serpulo.get("Node Memory Cell"))
        self.node_memory_bank = self.__add_region("Memory Bank", MindustryLocation.tech_tree_serpulo.get("Node Memory Bank"))
        self.node_logic_processor = self.__add_region("Logic Processor", MindustryLocation.tech_tree_serpulo.get("Node Logic Processor"))
        self.node_hyper_processor = self.__add_region("Hyper Processor", MindustryLocation.tech_tree_serpulo.get("Node Hyper Processor"))
        self.node_illuminator = self.__add_region("Illuminator", MindustryLocation.tech_tree_serpulo.get("Node Illuminator"))
        self.node_combustion_generator = self.__add_region("Combustion Generator", MindustryLocation.tech_tree_serpulo.get("Node Combustion Generator"))
        self.node_power_node = self.__add_region("Power Node", MindustryLocation.tech_tree_serpulo.get("Node Power Node"))
        self.node_large_power_node = self.__add_region("Large Power Node", MindustryLocation.tech_tree_serpulo.get("Node Large Power Node"))
        self.node_battery_diode = self.__add_region("Battery Diode", MindustryLocation.tech_tree_serpulo.get("Node Battery Diode"))
        self.node_surge_tower = self.__add_region("Surge Tower", MindustryLocation.tech_tree_serpulo.get("Node Surge Tower"))
        self.node_battery = self.__add_region("Battery", MindustryLocation.tech_tree_serpulo.get("Node Battery"))
        self.node_large_battery = self.__add_region("Large Battery", MindustryLocation.tech_tree_serpulo.get("Node Large Battery"))
        self.node_mender = self.__add_region("Mender", MindustryLocation.tech_tree_serpulo.get("Node Mender"))
        self.node_mend_projector = self.__add_region("Mend Projector", MindustryLocation.tech_tree_serpulo.get("Node Mend Projector"))
        self.node_force_projector = self.__add_region("Forced Projector", MindustryLocation.tech_tree_serpulo.get("Node Force Projector"))
        self.node_overdrive_projector = self.__add_region("Overdrive Projector", MindustryLocation.tech_tree_serpulo.get("Node Overdrive Projector"))
        self.node_overdrive_dome = self.__add_region("Overdrive Dome", MindustryLocation.tech_tree_serpulo.get("Node Overdrive Dome"))
        self.node_repair_point = self.__add_region("Repair Point", MindustryLocation.tech_tree_serpulo.get("Node Repair Point"))
        self.node_repair_turret = self.__add_region("Repair Turret", MindustryLocation.tech_tree_serpulo.get("Node Repair Turret"))
        self.node_steam_generator = self.__add_region("Steam Generator", MindustryLocation.tech_tree_serpulo.get("Node Steam Generator"))
        self.node_thermal_generator = self.__add_region("Thermal Generator", MindustryLocation.tech_tree_serpulo.get("Node Thermal Generator"))
        self.node_impact_reactor = self.__add_region("Impact Reactor", MindustryLocation.tech_tree_serpulo.get("Node Impact Reactor"))
        self.node_rtg_generator = self.__add_region("RTG Generator", MindustryLocation.tech_tree_serpulo.get("Node RTG Generator"))
        self.node_solar_panel = self.__add_region("Solar Panel", MindustryLocation.tech_tree_serpulo.get("Node Solar Panel"))
        self.node_large_solar_panel = self.__add_region("Large Solar Panel", MindustryLocation.tech_tree_serpulo.get("Node Large Solar Panel"))
        self.node_duo = self.__add_region("Duo", MindustryLocation.tech_tree_serpulo.get("Node Duo"))
        self.node_copper_wall = self.__add_region("Copper Wall", MindustryLocation.tech_tree_serpulo.get("Node Copper Wall"))
        self.node_large_copper_wall = self.__add_region("Large Copper Wall", MindustryLocation.tech_tree_serpulo.get("Node Large Copper Wall"))
        self.node_titanium_wall = self.__add_region("Titanium Wall", MindustryLocation.tech_tree_serpulo.get("Node Titanium Wall"))
        self.node_large_titanium_wall = self.__add_region("Large Titanium Wall", MindustryLocation.tech_tree_serpulo.get("Node Large Titanium Wall"))
        self.node_door = self.__add_region("Door", MindustryLocation.tech_tree_serpulo.get("Node Door"))
        self.node_large_door = self.__add_region("Large Door", MindustryLocation.tech_tree_serpulo.get("Node Large Door"))
        self.node_plastanium_wall = self.__add_region("Plastanium Wall", MindustryLocation.tech_tree_serpulo.get("Node Plastanium Wall"))
        self.node_large_plastanium_wall = self.__add_region("Large Plastanium Wall", MindustryLocation.tech_tree_serpulo.get("Node Large Plastanium Wall"))
        self.node_thorium_wall = self.__add_region("Thorium Wall", MindustryLocation.tech_tree_serpulo.get("Node Thorium Wall"))
        self.node_large_thorium_wall = self.__add_region("Large Thorium Wall", MindustryLocation.tech_tree_serpulo.get("Node Large Thorium Wall"))
        self.node_surge_wall = self.__add_region("Surge Wall", MindustryLocation.tech_tree_serpulo.get("Node Surge Wall"))
        self.node_large_surge_wall = self.__add_region("Large Surge Wall", MindustryLocation.tech_tree_serpulo.get("Node Large Surge Wall"))
        self.node_phase_wall = self.__add_region("Phase Wall", MindustryLocation.tech_tree_serpulo.get("Node Phase Wall"))
        self.node_large_phase_wall = self.__add_region("Large Phase Wall", MindustryLocation.tech_tree_serpulo.get("Node Large Phase Wall"))
        self.node_scatter = self.__add_region("Scatter", MindustryLocation.tech_tree_serpulo.get("Node Scatter"))
        self.node_hail = self.__add_region("Hail", MindustryLocation.tech_tree_serpulo.get("Node Hail"))
        self.node_salvo = self.__add_region("Salvo", MindustryLocation.tech_tree_serpulo.get("Node Salvo"))
        self.node_swarmer = self.__add_region("Swarmer", MindustryLocation.tech_tree_serpulo.get("Node Swarmer"))
        self.node_cyclone = self.__add_region("Cyclone", MindustryLocation.tech_tree_serpulo.get("Node Cyclone"))
        self.node_spectre = self.__add_region("Spectre", MindustryLocation.tech_tree_serpulo.get("Node Spectre"))
        self.node_ripple = self.__add_region("Ripple", MindustryLocation.tech_tree_serpulo.get("Node Ripple"))
        self.node_fuse = self.__add_region("Fuse", MindustryLocation.tech_tree_serpulo.get("Node Fuse"))
        self.node_scorch = self.__add_region("Scorch", MindustryLocation.tech_tree_serpulo.get("Node Scorch"))
        self.node_arc = self.__add_region("Arc", MindustryLocation.tech_tree_serpulo.get("Node Arc"))
        self.node_wave = self.__add_region("Wave", MindustryLocation.tech_tree_serpulo.get("Node Wave"))
        self.node_parallax = self.__add_region("Parallax", MindustryLocation.tech_tree_serpulo.get("Node Parallax"))
        self.node_segment = self.__add_region("Segment", MindustryLocation.tech_tree_serpulo.get("Node Segment"))
        self.node_tsunami = self.__add_region("Tsunami", MindustryLocation.tech_tree_serpulo.get("Node Tsunami"))
        self.node_lancer = self.__add_region("Lancer", MindustryLocation.tech_tree_serpulo.get("Node Lancer"))
        self.node_meltdown = self.__add_region("Meltdown", MindustryLocation.tech_tree_serpulo.get("Node Meltdown"))
        self.node_foreshadow = self.__add_region("Foreshadow", MindustryLocation.tech_tree_serpulo.get("Node Foreshadow"))
        self.node_shock_mine = self.__add_region("Shock Mine", MindustryLocation.tech_tree_serpulo.get("Node Shock Mine"))
        self.node_ground_factory = self.__add_region("Ground Factory", MindustryLocation.tech_tree_serpulo.get("Node Ground Factory"))
        self.node_dagger = self.__add_region("Dagger", MindustryLocation.tech_tree_serpulo.get("Node Dagger"))
        self.node_mace = self.__add_region("Mace", MindustryLocation.tech_tree_serpulo.get("Node Mace"))
        self.node_fortress = self.__add_region("Fortress", MindustryLocation.tech_tree_serpulo.get("Node Fortress"))
        self.node_scepter = self.__add_region("Scepter", MindustryLocation.tech_tree_serpulo.get("Node Scepter"))
        self.node_reign = self.__add_region("Reign", MindustryLocation.tech_tree_serpulo.get("Node Reign"))
        self.node_nova = self.__add_region("Nova", MindustryLocation.tech_tree_serpulo.get("Node Nova"))
        self.node_pulsar = self.__add_region("Pulsar", MindustryLocation.tech_tree_serpulo.get("Node Pulsar"))
        self.node_quasar = self.__add_region("Quasar", MindustryLocation.tech_tree_serpulo.get("Node Quasar"))
        self.node_vela = self.__add_region("Vela", MindustryLocation.tech_tree_serpulo.get("Node Vela"))
        self.node_corvus = self.__add_region("Corvus", MindustryLocation.tech_tree_serpulo.get("Node Corvus"))
        self.node_crawler = self.__add_region("Crawler", MindustryLocation.tech_tree_serpulo.get("Node Crawler"))
        self.node_atrax = self.__add_region("Atrax", MindustryLocation.tech_tree_serpulo.get("Node Atrax"))
        self.node_spiroct = self.__add_region("Spiroct", MindustryLocation.tech_tree_serpulo.get("Node Spiroct"))
        self.node_arkyid = self.__add_region("Arkyid", MindustryLocation.tech_tree_serpulo.get("Node Arkyid"))
        self.node_toxopid = self.__add_region("Toxopid", MindustryLocation.tech_tree_serpulo.get("Node Toxopid"))
        self.node_air_factory = self.__add_region("Air Factory", MindustryLocation.tech_tree_serpulo.get("Node Air Factory"))
        self.node_flare = self.__add_region("Flare", MindustryLocation.tech_tree_serpulo.get("Node Flare"))
        self.node_horizon = self.__add_region("Horizon", MindustryLocation.tech_tree_serpulo.get("Node Horizon"))
        self.node_zenith = self.__add_region("Zenith", MindustryLocation.tech_tree_serpulo.get("Node Zenith"))
        self.node_antumbra = self.__add_region("Antumbra", MindustryLocation.tech_tree_serpulo.get("Node Antumbra"))
        self.node_eclipse = self.__add_region("Eclipse", MindustryLocation.tech_tree_serpulo.get("Node Eclipse"))
        self.node_mono = self.__add_region("Mono", MindustryLocation.tech_tree_serpulo.get("Node Mono"))
        self.node_poly = self.__add_region("Poly", MindustryLocation.tech_tree_serpulo.get("Node Poly"))
        self.node_mega = self.__add_region("Mega", MindustryLocation.tech_tree_serpulo.get("Node Mega"))
        self.node_quad = self.__add_region("Quad", MindustryLocation.tech_tree_serpulo.get("Node Quad"))
        self.node_oct = self.__add_region("Oct", MindustryLocation.tech_tree_serpulo.get("Node Oct"))
        self.node_naval_factory = self.__add_region("Naval Factory", MindustryLocation.tech_tree_serpulo.get("Node Naval Factory"))
        self.node_risso = self.__add_region("Risso", MindustryLocation.tech_tree_serpulo.get("Node Risso"))
        self.node_minke = self.__add_region("Minke", MindustryLocation.tech_tree_serpulo.get("Node Minke"))
        self.node_bryde = self.__add_region("Bryde", MindustryLocation.tech_tree_serpulo.get("Node Bryde"))
        self.node_sei = self.__add_region("Sei", MindustryLocation.tech_tree_serpulo.get("Node Sei"))
        self.node_omura = self.__add_region("Omura", MindustryLocation.tech_tree_serpulo.get("Node Omura"))
        self.node_retusa = self.__add_region("Retusa", MindustryLocation.tech_tree_serpulo.get("Node Retusa"))
        self.node_oxynoe = self.__add_region("Oxynoe", MindustryLocation.tech_tree_serpulo.get("Node Oxynoe"))
        self.node_cyerce = self.__add_region("Cyerce", MindustryLocation.tech_tree_serpulo.get("Node Cyerce"))
        self.node_aegires = self.__add_region("Aegires", MindustryLocation.tech_tree_serpulo.get("Node Aegires"))
        self.node_narvanax = self.__add_region("Narvanax", MindustryLocation.tech_tree_serpulo.get("Node Narvanax"))
        self.node_additive_reconstructor = self.__add_region("Additive Reconstructor", MindustryLocation.tech_tree_serpulo.get("Node Additive Reconstructor"))
        self.node_multiplicative_reconstructor = self.__add_region("Multiplicative Reconstructor", MindustryLocation.tech_tree_serpulo.get("Node Multiplicative Reconstructor"))
        self.node_exponential_reconstructor = self.__add_region("Exponential Reconstructor", MindustryLocation.tech_tree_serpulo.get("Node Exponential Reconstructor"))
        self.node_tetrative_reconstructor = self.__add_region("Tetrative Reconstructor", MindustryLocation.tech_tree_serpulo.get("Node Tetrative Reconstructor"))


    def __connect_serpulo_campaign(self):
        """
        Connect region related to Serpulo's campaign
        """
        self.__connect_regions(self.menu, self.serpulo)
        self.__connect_regions(self.serpulo, self.node_core_shard)

        self.__connect_region(self.node_core_shard, self.node_conveyor)
        self.__connect_regions(self.node_conveyor, self.node_junction)
        self.__connect_regions(self.node_junction, self.node_router)
        self.__connect_regions(self.node_router, self.node_launch_pad)
        self.__connect_regions(self.node_router, self.node_distributor)
        self.__connect_regions(self.node_router, self.node_sorter)
        self.__connect_regions(self.node_sorter, self.node_inverted_sorter)
        self.__connect_regions(self.node_sorter, self.node_overflow_gate)
        self.__connect_regions(self.node_overflow_gate, self.node_underflow_gate)
        self.__connect_regions(self.node_router, self.node_container)
        self.__connect_regions(self.node_container, self.node_unloader)
        self.__connect_regions(self.node_container, self.node_vault)
        self.__connect_regions(self.node_router, self.node_bridge_conveyor)
        self.__connect_regions(self.node_bridge_conveyor, self.node_titanium_conveyor)
        self.__connect_regions(self.node_titanium_conveyor, self.node_phase_conveyor)
        self.__connect_regions(self.node_phase_conveyor, self.node_mass_driver)
        self.__connect_regions(self.node_titanium_conveyor, self.node_payload_conveyor)
        self.__connect_regions(self.node_payload_conveyor, self.node_payload_router)
        self.__connect_regions(self.node_titanium_conveyor, self.node_armored_conveyor)
        self.__connect_regions(self.node_armored_conveyor, self.node_plastanium_conveyor)

        self.__connect_regions(self.node_core_shard, self.node_core_foundation)
        self.__connect_regions(self.node_core_foundation, self.node_core_nucleus)

        self.__connect_regions(self.node_core_shard, self.node_mechanical_drill)
        self.__connect_regions(self.node_mechanical_drill, self.node_mechanical_pump)

        self.__connect_regions(self.node_mechanical_pump, self.node_conduit)


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
                raise ValueError("Invalid campaign choice")



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

