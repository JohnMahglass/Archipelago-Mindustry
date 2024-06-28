import json

from BaseClasses import Region, MultiWorld, Entrance, CollectionState, ItemClassification
from .Items import MindustryItem
from .Options import MindustryOptions
from .Locations import MindustryLocations, MindustryLocation
from typing import Optional, Dict
from worlds.generic.Rules import set_rule, add_rule


def _has_frozen_forest(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Frozen Forest Captured", player)

def _has_the_craters(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("The Craters Captured", player)

def _has_ruinous_shores(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Ruinous Shores Captured", player)

def _has_windswept_islands(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Windswept Islands Captured", player)

def _has_tar_field(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Tar Fields Captured", player)

def _has_impact_0078(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Impact 0078 Captured", player)

def _has_desolate_rift(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Desolate Rift Captured", player)

def _has_planetary_launch_terminal(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Planetary Launch Terminal Captured", player)

def _has_extraction_outpost(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Extraction Outpost Captured", player)

def _has_salt_flats(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Salt Flats Captured", player)

def _has_coastline(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Coastline Captured", player)

def _has_naval_fortress(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Naval Fortress Captured", player)

def _has_overgrowth(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Overgrowth Captured", player)

def _has_biomass_synthesis_facility(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Biomass Synthesis Facility Captured", player)

def _has_stained_mountains(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Stained Mountains Captured", player)

def _has_fungal_pass(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Fungal Pass Captured", player)

def _has_nuclear_production_complex(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Nuclear Production Complex Captured", player)

def _has_titanium(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Titanium Produced", player)

def _has_cryofluid(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Cryofluid Produced", player)

def _has_thorium(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Thorium Produced", player)

def _has_surge_alloy(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Surge Alloy Produced", player)

def _has_phase_fabric(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Phase Fabric Produced", player)

def _has_metaglass(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Metaglass Produced", player)

def _has_coal(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Coal Produced", player)

def _has_graphite(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Graphite Produced", player)

def _has_silicon(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Silicon Produced", player)

def _has_pyratite(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Pyratite Produced", player)

def _has_blast_compound(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Blast Compound Produced", player)

def _has_spore_pod(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Spore Pod Produced", player)

def _has_oil(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Oil Produced", player)

def _has_plastanium(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Plastanium Produced", player)

def _has_electricity(state:CollectionState, player: int) -> bool:
    """If the player has acces to electricity"""
    return state.has("Electricity", player)

class MindustryRegions:
    """
    Class used to create region for Mindustry
    """
    menu: Region
    victory: Region
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
    node_airblast_drill: Region
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
    node_navanax: Region
    node_additive_reconstructor: Region
    node_multiplicative_reconstructor: Region
    node_exponential_reconstructor: Region
    node_tetrative_reconstructor: Region
    node_ground_zero: Region
    node_frozen_forest: Region
    node_the_craters: Region
    node_ruinous_shores: Region
    node_windswept_islands: Region
    node_tar_fields: Region
    node_impact_0078: Region
    node_desolate_rift: Region
    node_planetary_launch_terminal: Region
    node_extraction_outpost: Region
    node_salt_flats: Region
    node_coastline: Region
    node_naval_fortress: Region
    node_overgrowth: Region
    node_biomass_synthesis_facility: Region
    node_stained_mountains: Region
    node_fungal_pass: Region
    node_nuclear_production_complex: Region
    node_copper: Region
    node_water: Region
    node_sand: Region
    node_lead: Region
    node_titanium: Region
    node_cryofluid: Region
    node_thorium: Region
    node_surge_alloy: Region
    node_phase_fabric: Region
    node_metaglass: Region
    node_scrap: Region
    node_slag: Region
    node_coal: Region
    node_graphite: Region
    node_silicon: Region
    node_pyratite: Region
    node_blast_compound: Region
    node_spore_pod: Region
    node_oil: Region
    node_plastanium: Region


    multiworld: MultiWorld
    """
    Current Multiworld game
    """

    player: int
    """
    Player Id
    """


    def connect_regions(self) -> None:
        self.__connect_serpulo_campaign()

    def add_regions_to_world(self) -> None:
        """
        Add every region to the `world`
        """
        pass

    def add_event_locations(self) -> None:
        """
        Add every event (locations and items) to the `world`
        """
        self.__add_event_location(self.victory, "Objective complete",
                                  "Victory")
        self.__add_serpulo_events()


    def initialise_rules(self, options: MindustryOptions) -> None:
        """Initialise rules"""
        self.__initialise_serpulo_rules()


    def __init__(self, multiworld: MultiWorld, player: int):
        """
        Initialisation of the regions
        """
        self.multiworld = multiworld
        self.player = player
        self.__create_campaign(0)


    def __add_event_location(self, region: Region, name: str, event_name: str) -> None:
        """
        Add an event to the `region` with the name `name` and the item
        `event_name`
        """
        location: MindustryLocation = MindustryLocation(
            self.player, name, None, region
        )
        region.locations.append(location)
        location.place_locked_item(MindustryItem(event_name, ItemClassification.progression, None, self.player))


    def __create_campaign(self, campaign: int):
        """
        Create region for selected campaign
        """
        self.menu = self.__add_region("Menu", None)
        self.victory = self.__add_region("Victory", None)
        match campaign:
            case 0:
                self.__create_serpulo_campaign()
            case 1:
                self.__create_erekir_campaign()
            case 2:
                self.__create_all_campaign()
            case _:
                raise ValueError("Invalid campaign choice")


    def __connect_serpulo_campaign(self):
        """
        Connect region related to Serpulo's campaign
        """
        self.__connect_regions(self.menu, self.serpulo)
        self.__connect_regions(self.menu, self.victory,
                               lambda state: _has_frozen_forest(state, self.player) and
                                            _has_the_craters(state, self.player) and
                                            _has_ruinous_shores(state, self.player) and
                                            _has_windswept_islands(state, self.player) and
                                            _has_tar_field(state, self.player) and
                                            _has_impact_0078(state, self.player) and
                                            _has_desolate_rift(state, self.player) and
                                            _has_planetary_launch_terminal(state, self.player) and
                                            _has_extraction_outpost(state, self.player) and
                                            _has_salt_flats(state, self.player) and
                                            _has_coastline(state, self.player) and
                                            _has_naval_fortress(state, self.player) and
                                            _has_overgrowth(state, self.player) and
                                            _has_biomass_synthesis_facility(state, self.player) and
                                            _has_stained_mountains(state, self.player) and
                                            _has_fungal_pass(state, self.player) and
                                            _has_nuclear_production_complex(state, self.player))
        self.__connect_regions(self.serpulo, self.node_core_shard)

        self.__connect_regions(self.node_core_shard, self.node_conveyor)
        self.__connect_regions(self.node_conveyor, self.node_junction)
        self.__connect_regions(self.node_junction, self.node_router)
        self.__connect_regions(self.node_router, self.node_launch_pad,
                               lambda state: _has_extraction_outpost(state, self.player) and
                                                _has_silicon(state, self.player) and
                                                _has_titanium(state, self.player))
        self.__connect_regions(self.node_router, self.node_distributor)
        self.__connect_regions(self.node_router, self.node_sorter)
        self.__connect_regions(self.node_sorter, self.node_inverted_sorter)
        self.__connect_regions(self.node_sorter, self.node_overflow_gate)
        self.__connect_regions(self.node_overflow_gate, self.node_underflow_gate)
        self.__connect_regions(self.node_router, self.node_container,
                               lambda state: _has_biomass_synthesis_facility(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_container, self.node_unloader,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_container, self.node_vault,
                               lambda state: _has_stained_mountains(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_router, self.node_bridge_conveyor)
        self.__connect_regions(self.node_bridge_conveyor, self.node_titanium_conveyor,
                               lambda state: _has_the_craters(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_titanium_conveyor, self.node_phase_conveyor,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_phase_conveyor, self.node_mass_driver,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_titanium_conveyor, self.node_payload_conveyor,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_payload_conveyor, self.node_payload_router)
        self.__connect_regions(self.node_titanium_conveyor, self.node_armored_conveyor,
                               lambda state: _has_plastanium(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_armored_conveyor, self.node_plastanium_conveyor,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player))

        self.__connect_regions(self.node_core_shard, self.node_core_foundation,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_core_foundation, self.node_core_nucleus,
                               lambda state: _has_thorium(state, self.player))

        self.__connect_regions(self.node_core_shard, self.node_mechanical_drill)
        self.__connect_regions(self.node_mechanical_drill, self.node_mechanical_pump,
                               lambda state: _has_metaglass(state, self.player))

        self.__connect_regions(self.node_mechanical_pump, self.node_conduit)
        self.__connect_regions(self.node_conduit, self.node_liquid_junction,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_liquid_junction, self.node_liquid_router)
        self.__connect_regions(self.node_liquid_router, self.node_liquid_container,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_liquid_container, self.node_liquid_tank)
        self.__connect_regions(self.node_liquid_router, self.node_bridge_conduit)
        self.__connect_regions(self.node_liquid_router, self.node_pulse_conduit,
                               lambda state: _has_windswept_islands(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_pulse_conduit, self.node_phase_conduit,
                               lambda state: _has_phase_fabric(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_pulse_conduit, self.node_plated_conduit,
                               lambda state: _has_thorium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_pulse_conduit, self.node_rotary_pump,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_rotary_pump, self.node_impulse_pump,
                               lambda state: _has_thorium(state, self.player))

        self.__connect_regions(self.node_mechanical_drill, self.node_graphite_press,
                               lambda state: _has_coal(state, self.player))
        self.__connect_regions(self.node_graphite_press, self.node_pneumatic_drill,
                               lambda state: _has_frozen_forest(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_pneumatic_drill, self.node_cultivator,
                               lambda state: _has_biomass_synthesis_facility(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_pneumatic_drill, self.node_laser_drill,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_laser_drill, self.node_airblast_drill,
                               lambda state: _has_thorium(state, self.player) and
                                            _has_nuclear_production_complex(state, self.player))
        self.__connect_regions(self.node_laser_drill, self.node_water_extractor,
                               lambda state: _has_salt_flats(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_water_extractor, self.node_oil_extractor,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_graphite_press, self.node_pyratite_mixer)
        self.__connect_regions(self.node_pyratite_mixer, self.node_blast_mixer,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_pyratite(state, self.player) and
                                            _has_spore_pod(state, self.player))
        self.__connect_regions(self.node_graphite_press, self.node_silicon_smelter)
        self.__connect_regions(self.node_silicon_smelter, self.node_spore_press,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_spore_press, self.node_coal_centrifuge,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_oil(state, self.player))
        self.__connect_regions(self.node_coal_centrifuge, self.node_multi_press)
        self.__connect_regions(self.node_multi_press, self.node_silicon_crucible,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_pyratite(state, self.player))
        self.__connect_regions(self.node_spore_press, self.node_plastanium_compressor,
                               lambda state: _has_windswept_islands(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_plastanium_compressor, self.node_phase_weaver,
                               lambda state: _has_tar_field(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_silicon_smelter, self.node_kiln,
                               lambda state: _has_the_craters(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_kiln, self.node_pulveriser)
        self.__connect_regions(self.node_pulveriser, self.node_incinerator)
        self.__connect_regions(self.node_incinerator, self.node_melter)
        self.__connect_regions(self.node_melter, self.node_surge_smelter,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_melter, self.node_separator,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_separator, self.node_disassembler,
                               lambda state: _has_plastanium(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_melter, self.node_cryofluid_mixer,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_silicon_smelter, self.node_micro_processor,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_micro_processor, self.node_switch,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_switch, self.node_message)
        self.__connect_regions(self.node_message, self.node_logic_display,
                               lambda state: _has_metaglass(state, self.player))
        self.__connect_regions(self.node_logic_display, self.node_large_logic_display,
                               lambda state: _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_message, self.node_memory_cell)
        self.__connect_regions(self.node_memory_cell, self.node_memory_bank,
                               lambda state: _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_switch, self.node_logic_processor,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_logic_processor, self.node_hyper_processor,
                               lambda state: _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_silicon_smelter, self.node_illuminator,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player))

        self.__connect_regions(self.node_mechanical_drill, self.node_combustion_generator,
                               lambda state: _has_coal(state, self.player))
        self.__connect_regions(self.node_combustion_generator, self.node_power_node)
        self.__connect_regions(self.node_power_node, self.node_large_power_node,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_large_power_node, self.node_battery_diode,
                               lambda state: _has_plastanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_battery_diode, self.node_surge_tower,
                               lambda state: _has_surge_alloy(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_battery)
        self.__connect_regions(self.node_battery, self.node_large_battery,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_mender)
        self.__connect_regions(self.node_mender, self.node_mend_projector,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_mend_projector, self.node_force_projector,
                               lambda state: _has_impact_0078(state, self.player))
        self.__connect_regions(self.node_force_projector, self.node_overdrive_projector,
                               lambda state: _has_plastanium(state, self.player))
        self.__connect_regions(self.node_overdrive_projector, self.node_overdrive_dome,
                               lambda state: _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_mend_projector, self.node_repair_point)
        self.__connect_regions(self.node_repair_point, self.node_repair_turret,
                               lambda state: _has_thorium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_steam_generator,
                               lambda state: _has_the_craters(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_coal(state, self.player))
        self.__connect_regions(self.node_steam_generator, self.node_thermal_generator,
                               lambda state: _has_metaglass(state, self.player))
        self.__connect_regions(self.node_thermal_generator, self.node_differential_generator,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_pyratite(state, self.player) and
                                            _has_cryofluid(state, self.player))
        self.__connect_regions(self.node_differential_generator, self.node_thorium_reactor,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_thorium_reactor, self.node_impact_reactor,
                               lambda state: _has_blast_compound(state, self.player) and
                                            _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_thorium_reactor, self.node_rtg_generator,
                               lambda state: _has_phase_fabric(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_solar_panel,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_solar_panel, self.node_large_solar_panel,
                               lambda state: _has_phase_fabric(state, self.player))

        self.__connect_regions(self.node_core_shard, self.node_duo)
        self.__connect_regions(self.node_duo, self.node_copper_wall)
        self.__connect_regions(self.node_copper_wall, self.node_large_copper_wall)
        self.__connect_regions(self.node_large_copper_wall, self.node_titanium_wall,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_titanium_wall, self.node_large_titanium_wall)
        self.__connect_regions(self.node_titanium_wall, self.node_door,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_door, self.node_large_door)
        self.__connect_regions(self.node_titanium_wall, self.node_plastanium_wall,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_plastanium_wall, self.node_large_plastanium_wall)
        self.__connect_regions(self.node_titanium_wall, self.node_thorium_wall,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_thorium_wall, self.node_large_thorium_wall)
        self.__connect_regions(self.node_titanium_wall, self.node_surge_wall,
                               lambda state: _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_surge_wall, self.node_large_surge_wall)
        self.__connect_regions(self.node_surge_wall, self.node_phase_wall,
                               lambda state: _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_phase_wall, self.node_large_phase_wall)
        self.__connect_regions(self.node_duo, self.node_scatter)
        self.__connect_regions(self.node_scatter, self.node_hail,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_the_craters(state, self.player))
        self.__connect_regions(self.node_hail, self.node_salvo,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_salvo, self.node_swarmer,
                               lambda state: _has_plastanium(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_pyratite(state, self.player))
        self.__connect_regions(self.node_swarmer, self.node_cyclone)
        self.__connect_regions(self.node_cyclone, self.node_spectre,
                               lambda state: _has_nuclear_production_complex(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_salvo, self.node_ripple)
        self.__connect_regions(self.node_ripple, self.node_fuse,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_duo, self.node_scorch,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_coal(state, self.player))
        self.__connect_regions(self.node_scorch, self.node_arc)
        self.__connect_regions(self.node_arc, self.node_wave,
                               lambda state: _has_metaglass(state, self.player))
        self.__connect_regions(self.node_wave, self.node_parallax,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_parallax, self.node_segment,
                               lambda state: _has_thorium(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_wave, self.node_tsunami,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_arc, self.node_lancer,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_lancer, self.node_meltdown,
                               lambda state: _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_meltdown, self.node_foreshadow,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_lancer, self.node_shock_mine)

        self.__connect_regions(self.node_core_shard, self.node_ground_factory,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_ground_factory, self.node_dagger)
        self.__connect_regions(self.node_dagger, self.node_mace,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_mace, self.node_fortress,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_fortress, self.node_scepter,
                               lambda state: _has_plastanium(state, self.player))
        self.__connect_regions(self.node_scepter, self.node_reign,
                               lambda state: _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_dagger, self.node_nova,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_nova, self.node_pulsar,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_pulsar, self.node_quasar,
                               lambda state: _has_metaglass(state, self.player))
        self.__connect_regions(self.node_quasar, self.node_vela,
                               lambda state: _has_plastanium(state, self.player))
        self.__connect_regions(self.node_vela, self.node_corvus,
                               lambda state: _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_dagger, self.node_crawler,
                               lambda state: _has_coal(state, self.player))
        self.__connect_regions(self.node_crawler, self.node_atrax,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_atrax, self.node_spiroct,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_spiroct, self.node_arkyid,
                               lambda state: _has_plastanium(state, self.player))
        self.__connect_regions(self.node_arkyid, self.node_toxopid,
                               lambda state: _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_ground_factory, self.node_air_factory)
        self.__connect_regions(self.node_air_factory, self.node_flare)
        self.__connect_regions(self.node_flare, self.node_horizon,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_horizon, self.node_zenith,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_zenith, self.node_antumbra,
                               lambda state: _has_plastanium(state, self.player))
        self.__connect_regions(self.node_antumbra, self.node_eclipse,
                               lambda state: _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_flare, self.node_mono)
        self.__connect_regions(self.node_mono, self.node_poly,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_poly, self.node_mega,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_mega, self.node_quad,
                               lambda state: _has_plastanium(state, self.player))
        self.__connect_regions(self.node_quad, self.node_oct,
                               lambda state: _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_air_factory, self.node_naval_factory,
                               lambda state: _has_ruinous_shores(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_naval_factory, self.node_risso)
        self.__connect_regions(self.node_risso, self.node_minke,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_minke, self.node_bryde,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_bryde, self.node_sei,
                               lambda state: _has_plastanium(state, self.player))
        self.__connect_regions(self.node_sei, self.node_omura,
                               lambda state: _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_risso, self.node_retusa,
                               lambda state: _has_windswept_islands(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_retusa, self.node_oxynoe,
                               lambda state: _has_coastline(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_oxynoe, self.node_cyerce)
        self.__connect_regions(self.node_cyerce, self.node_aegires,
                               lambda state: _has_plastanium(state, self.player))
        self.__connect_regions(self.node_aegires, self.node_navanax,
                               lambda state: _has_phase_fabric(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_naval_fortress(state, self.player))

        self.__connect_regions(self.node_ground_factory, self.node_additive_reconstructor,
                               lambda state: _has_biomass_synthesis_facility(state, self.player))
        self.__connect_regions(self.node_additive_reconstructor, self.node_multiplicative_reconstructor,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_multiplicative_reconstructor, self.node_exponential_reconstructor,
                               lambda state: _has_overgrowth(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_exponential_reconstructor, self.node_tetrative_reconstructor,
                               lambda state: _has_surge_alloy(state, self.player))

        self.__connect_regions(self.node_core_shard, self.node_ground_zero)
        self.__connect_regions(self.node_ground_zero, self.node_frozen_forest)
        self.__connect_regions(self.node_frozen_forest, self.node_the_craters,
                              lambda state: _has_frozen_forest(state, self.player))
        self.__connect_regions(self.node_the_craters, self.node_ruinous_shores,
                              lambda state: _has_the_craters(state, self.player))
        self.__connect_regions(self.node_ruinous_shores, self.node_windswept_islands,
                              lambda state: _has_ruinous_shores(state, self.player))
        self.__connect_regions(self.node_windswept_islands, self.node_tar_fields,
                              lambda state: _has_windswept_islands(state, self.player))
        self.__connect_regions(self.node_tar_fields, self.node_impact_0078,
                              lambda state: _has_tar_field(state, self.player))
        self.__connect_regions(self.node_impact_0078, self.node_desolate_rift,
                              lambda state: _has_impact_0078(state, self.player))
        self.__connect_regions(self.node_desolate_rift, self.node_planetary_launch_terminal,
                              lambda state: _has_desolate_rift(state, self.player))
        self.__connect_regions(self.node_windswept_islands, self.node_extraction_outpost,
                               lambda state: _has_windswept_islands(state, self.player))
        self.__connect_regions(self.node_windswept_islands, self.node_salt_flats,
                               lambda state: _has_windswept_islands(state, self.player))
        self.__connect_regions(self.node_salt_flats, self.node_coastline,
                               lambda state: _has_salt_flats(state, self.player))
        self.__connect_regions(self.node_coastline, self.node_naval_fortress,
                               lambda state: _has_coastline(state, self.player))
        self.__connect_regions(self.node_the_craters, self.node_overgrowth,
                               lambda state: _has_the_craters(state, self.player))
        self.__connect_regions(self.node_frozen_forest, self.node_biomass_synthesis_facility,
                               lambda state: _has_frozen_forest(state, self.player))
        self.__connect_regions(self.node_biomass_synthesis_facility, self.node_stained_mountains,
                               lambda state: _has_biomass_synthesis_facility(state, self.player))
        self.__connect_regions(self.node_stained_mountains, self.node_fungal_pass,
                               lambda state: _has_stained_mountains(state, self.player))
        self.__connect_regions(self.node_fungal_pass, self.node_nuclear_production_complex,
                               lambda state: _has_fungal_pass(state, self.player))
        self.__connect_regions(self.node_core_shard, self.node_copper)
        self.__connect_regions(self.node_copper, self.node_water)
        self.__connect_regions(self.node_copper, self.node_lead)
        self.__connect_regions(self.node_lead, self.node_titanium)
        self.__connect_regions(self.node_titanium, self.node_cryofluid,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_titanium, self.node_thorium,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_thorium, self.node_surge_alloy,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_thorium, self.node_phase_fabric,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_lead, self.node_metaglass)
        self.__connect_regions(self.node_copper, self.node_sand)
        self.__connect_regions(self.node_sand, self.node_scrap)
        self.__connect_regions(self.node_scrap, self.node_slag)
        self.__connect_regions(self.node_sand, self.node_coal)
        self.__connect_regions(self.node_coal, self.node_graphite,
                               lambda state: _has_coal(state, self.player))
        self.__connect_regions(self.node_graphite, self.node_silicon,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_coal, self.node_pyratite,
                               lambda state: _has_coal(state, self.player))
        self.__connect_regions(self.node_pyratite, self.node_blast_compound,
                               lambda state: _has_pyratite(state, self.player))
        self.__connect_regions(self.node_coal, self.node_spore_pod,
                               lambda state: _has_coal(state, self.player))
        self.__connect_regions(self.node_coal, self.node_oil,
                               lambda state: _has_coal(state, self.player))
        self.__connect_regions(self.node_oil, self.node_plastanium,
                               lambda state: _has_oil(state, self.player))


    def __create_erekir_campaign(self):
        """
        Create region related to the erekir campaign.
        Method not implemented
        """
        pass


    def __connect_erekir_campaign(self):
        """
        Connect region related to Erekir's campaign
        Method not implemented
        """
        pass

    def __create_all_campaign(self):
        """
        Create region related to the all campaigns.
        Method not implemented
        """
        pass


    def __connect_all_campaign(self):
        """
        Connect region related to all campaigns
        Method not implemented
        """
        pass

    def __add_region(self, hint: str,
                     locations: Optional[Dict[str, Optional[int]]]) -> Region:
        """Create a new region."""
        region: Region = Region(hint, self.player, self.multiworld, hint)
        if locations is not None:
            region.add_locations(locations, MindustryLocation)
        self.multiworld.regions.append(region)
        return region

    def __initialise_serpulo_rules(self):
        """Initialise rules for Serpulo location"""
        add_rule(self.multiworld.get_location("Node Launch Pad", self.player),
                 lambda state: _has_extraction_outpost(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Container", self.player),
                 lambda state: _has_biomass_synthesis_facility(state, self.player))
        add_rule(self.multiworld.get_location("Node Unloader", self.player),
                 lambda state: _has_biomass_synthesis_facility(state, self.player))
        add_rule(self.multiworld.get_location("Node Vault", self.player),
                 lambda state: _has_biomass_synthesis_facility(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Titanium Conveyor", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Phase Conveyor", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Mass Driver", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Payload Conveyor", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Payload Router", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Armored Conveyor", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Plastanium Conveyor", self.player),
                 lambda state: _has_the_craters(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Pulse Conduit", self.player),
                 lambda state: _has_windswept_islands(state, self.player))
        add_rule(self.multiworld.get_location("Node Phase Conduit", self.player),
                 lambda state: _has_windswept_islands(state, self.player))
        add_rule(self.multiworld.get_location("Node Plated Conduit", self.player),
                 lambda state: _has_windswept_islands(state, self.player))
        add_rule(self.multiworld.get_location("Node Rotary Pump", self.player),
                 lambda state: _has_windswept_islands(state, self.player))
        add_rule(self.multiworld.get_location("Node Impulse Pump", self.player),
                 lambda state: _has_windswept_islands(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Pneumatic Drill", self.player),
                 lambda state: _has_frozen_forest(state, self.player))
        add_rule(self.multiworld.get_location("Node Cultivator", self.player),
                 lambda state: _has_frozen_forest(state, self.player) and
                                _has_biomass_synthesis_facility(state, self.player))
        add_rule(self.multiworld.get_location("Node Laser Drill", self.player),
                 lambda state: _has_frozen_forest(state, self.player))
        add_rule(self.multiworld.get_location("Node Airblast Drill", self.player),
                 lambda state: _has_frozen_forest(state, self.player) and
                                _has_nuclear_production_complex(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Water Extractor", self.player),
                 lambda state: _has_frozen_forest(state, self.player) and
                                _has_salt_flats(state, self.player))
        add_rule(self.multiworld.get_location("Node Oil Extractor", self.player),
                 lambda state: _has_frozen_forest(state, self.player) and
                               _has_salt_flats(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Plastanium Compressor", self.player),
                 lambda state: _has_windswept_islands(state, self.player))
        add_rule(self.multiworld.get_location("Node Phase Weaver", self.player),
                 lambda state: _has_windswept_islands(state, self.player) and
                               _has_tar_field(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Kiln", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Pulveriser", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Incinerator", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Melter", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Surge Smelter", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Separator", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Disassembler", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Cryofluid Mixer", self.player),
                 lambda state: _has_the_craters(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Hail", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Salvo", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Swarmer", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Cyclone", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Spectre", self.player),
                 lambda state: _has_the_craters(state, self.player) and
                                _has_nuclear_production_complex(state, self.player))
        add_rule(self.multiworld.get_location("Node Ripple", self.player),
                 lambda state: _has_the_craters(state, self.player))
        add_rule(self.multiworld.get_location("Node Fuse", self.player),
                 lambda state: _has_the_craters(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Naval Factory", self.player),
                 lambda state: _has_ruinous_shores(state, self.player))
        add_rule(self.multiworld.get_location("Node Risso", self.player),
                 lambda state: _has_ruinous_shores(state, self.player))
        add_rule(self.multiworld.get_location("Node Minke", self.player),
                 lambda state: _has_ruinous_shores(state, self.player))
        add_rule(self.multiworld.get_location("Node Bryde", self.player),
                 lambda state: _has_ruinous_shores(state, self.player))
        add_rule(self.multiworld.get_location("Node Sei", self.player),
                 lambda state: _has_ruinous_shores(state, self.player))
        add_rule(self.multiworld.get_location("Node Omura", self.player),
                 lambda state: _has_ruinous_shores(state, self.player))
        add_rule(self.multiworld.get_location("Node Retusa", self.player),
                 lambda state: _has_ruinous_shores(state, self.player) and
                                _has_windswept_islands(state, self.player))
        add_rule(self.multiworld.get_location("Node Oxynoe", self.player),
                 lambda state: _has_ruinous_shores(state, self.player) and
                               _has_windswept_islands(state, self.player) and
                                _has_coastline(state, self.player))
        add_rule(self.multiworld.get_location("Node Cyerce", self.player),
                 lambda state: _has_ruinous_shores(state, self.player) and
                               _has_windswept_islands(state, self.player) and
                               _has_coastline(state, self.player))
        add_rule(self.multiworld.get_location("Node Aegires", self.player),
                 lambda state: _has_ruinous_shores(state, self.player) and
                               _has_windswept_islands(state, self.player) and
                               _has_coastline(state, self.player))
        add_rule(self.multiworld.get_location("Node Navanax", self.player),
                 lambda state: _has_ruinous_shores(state, self.player) and
                               _has_windswept_islands(state, self.player) and
                               _has_coastline(state, self.player) and
                                _has_naval_fortress(state, self.player))
#
        add_rule(self.multiworld.get_location("Node Additive Reconstructor", self.player),
                 lambda state: _has_biomass_synthesis_facility(state, self.player))
        add_rule(self.multiworld.get_location("Node Multiplicative Reconstructor", self.player),
                 lambda state: _has_biomass_synthesis_facility(state, self.player))
        add_rule(self.multiworld.get_location("Node Exponential Reconstructor", self.player),
                 lambda state: _has_biomass_synthesis_facility(state, self.player) and
                                _has_overgrowth(state, self.player))
        add_rule(self.multiworld.get_location("Node Tetrative Reconstructor", self.player),
                 lambda state: _has_biomass_synthesis_facility(state, self.player) and
                                _has_overgrowth(state, self.player))


    def __connect_regions(self, source_region: Region, target_region: Region, rule = None) -> None:
        """
        Connect regions between themselves
        """
        entrance = Entrance(source_region.player, source_region.name + " -> " + target_region.name, source_region)
        source_region.exits.append(entrance)
        entrance.connect(target_region)

        if rule is not None:
            set_rule(entrance, rule)


    def __create_serpulo_campaign(self):
        """
        Create region related to the serpulo campaign.
        """
        self.serpulo: Region = self.__add_region("Serpulo", None)
        self.node_core_shard = self.__add_region("Core: Shard", None)
        self.node_conveyor = self.__add_region("Conveyor", None)
        self.node_junction = self.__add_region("Junction", MindustryLocations.serpulo_junction)
        self.node_router = self.__add_region("Router", MindustryLocations.serpulo_router)
        self.node_launch_pad = self.__add_region("Launch Pad", MindustryLocations.serpulo_launch_pad)
        self.node_distributor = self.__add_region("Distributor", MindustryLocations.serpulo_distributor)
        self.node_sorter = self.__add_region("Sorter", MindustryLocations.serpulo_sorter)
        self.node_inverted_sorter = self.__add_region("Inverted Sorter", MindustryLocations.serpulo_inverted_sorter)
        self.node_overflow_gate = self.__add_region("Overflow Gate", MindustryLocations.serpulo_overflow_gate)
        self.node_underflow_gate = self.__add_region("Underflow Gate", MindustryLocations.serpulo_underflow_gate)
        self.node_container = self.__add_region("Container", MindustryLocations.serpulo_container)
        self.node_unloader = self.__add_region("Unloader", MindustryLocations.serpulo_unloader)
        self.node_vault = self.__add_region("Vault", MindustryLocations.serpulo_vault)
        self.node_bridge_conveyor = self.__add_region("Bridge Conveyor", MindustryLocations.serpulo_bridge_conveyor)
        self.node_titanium_conveyor = self.__add_region("Titanium Conveyor", MindustryLocations.serpulo_titanium_conveyor)
        self.node_phase_conveyor = self.__add_region("Phase Conveyor", MindustryLocations.serpulo_phase_conveyor)
        self.node_mass_driver = self.__add_region("Mass Driver", MindustryLocations.serpulo_mass_driver)
        self.node_payload_conveyor = self.__add_region("Payload Conveyor", MindustryLocations.serpulo_payload_conveyor)
        self.node_payload_router = self.__add_region("Payload Router", MindustryLocations.serpulo_payload_router)
        self.node_armored_conveyor = self.__add_region("Armored Conveyor", MindustryLocations.serpulo_armored_conveyor)
        self.node_plastanium_conveyor = self.__add_region("Plastanium Conveyor", MindustryLocations.serpulo_plastanium_conveyor)
        self.node_core_foundation = self.__add_region("Core: Foundation", MindustryLocations.serpulo_core_foundation)
        self.node_core_nucleus = self.__add_region("Core: Nucleus", MindustryLocations.serpulo_core_nucleus)
        self.node_mechanical_drill = self.__add_region("Mechanical Drill", None)
        self.node_mechanical_pump = self.__add_region("Mechanical Pump", MindustryLocations.serpulo_mechanical_pump)
        self.node_conduit = self.__add_region("Conduit", MindustryLocations.serpulo_conduit)
        self.node_liquid_junction = self.__add_region("Liquid Junction", MindustryLocations.serpulo_liquid_junction)
        self.node_liquid_router = self.__add_region("Liquid Router", MindustryLocations.serpulo_liquid_router)
        self.node_liquid_container = self.__add_region("Liquid Container", MindustryLocations.serpulo_liquid_container)
        self.node_liquid_tank = self.__add_region("Liquid Tank", MindustryLocations.serpulo_liquid_tank)
        self.node_bridge_conduit = self.__add_region("Bridge Conduit", MindustryLocations.serpulo_bridge_conduit)
        self.node_pulse_conduit = self.__add_region("Pulse Conduit", MindustryLocations.serpulo_pulse_conduit)
        self.node_phase_conduit =  self.__add_region("Phase Conduit", MindustryLocations.serpulo_phase_conduit)
        self.node_plated_conduit = self.__add_region("Plated Conduit", MindustryLocations.serpulo_plated_conduit)
        self.node_rotary_pump = self.__add_region("Rotary Pump", MindustryLocations.serpulo_rotary_pump)
        self.node_impulse_pump = self.__add_region("Impulse Pump", MindustryLocations.serpulo_impulse_pump)
        self.node_graphite_press = self.__add_region("Graphite Press", MindustryLocations.serpulo_graphite_press)
        self.node_pneumatic_drill = self.__add_region("Pneumatic Drill", MindustryLocations.serpulo_pneumatic_drill)
        self.node_cultivator = self.__add_region("Cultivator", MindustryLocations.serpulo_cultivator)
        self.node_laser_drill = self.__add_region("Laser Drill", MindustryLocations.serpulo_laser_drill)
        self.node_airblast_drill = self.__add_region("Airblast Drill", MindustryLocations.serpulo_airblast_drill)
        self.node_water_extractor = self.__add_region("Water Extractor", MindustryLocations.serpulo_water_extractor)
        self.node_oil_extractor = self.__add_region("Oil Extractor", MindustryLocations.serpulo_oil_extractor)
        self.node_pyratite_mixer = self.__add_region("Pyrate Mixer", MindustryLocations.serpulo_pyratite_mixer)
        self.node_blast_mixer = self.__add_region("Blast Mixer", MindustryLocations.serpulo_blast_mixer)
        self.node_silicon_smelter = self.__add_region("Silicon Smelter", MindustryLocations.serpulo_silicon_smelter)
        self.node_spore_press = self.__add_region("Spore Press", MindustryLocations.serpulo_spore_press)
        self.node_coal_centrifuge = self.__add_region("Coal Centrifuge", MindustryLocations.serpulo_coal_centrifuge)
        self.node_multi_press = self.__add_region("Multi Press", MindustryLocations.serpulo_multi_press)
        self.node_silicon_crucible = self.__add_region("Silicon Crucible", MindustryLocations.serpulo_silicon_crucible)
        self.node_plastanium_compressor = self.__add_region("Plastanium Compressor", MindustryLocations.serpulo_plastanium_compressor)
        self.node_phase_weaver = self.__add_region("Phase Weaver", MindustryLocations.serpulo_phase_weaver)
        self.node_kiln = self.__add_region("Kiln", MindustryLocations.serpulo_kiln)
        self.node_pulveriser = self.__add_region("Pulveriser", MindustryLocations.serpulo_pulveriser)
        self.node_incinerator = self.__add_region("Incinerator", MindustryLocations.serpulo_incinerator)
        self.node_melter = self.__add_region("Melter", MindustryLocations.serpulo_melter)
        self.node_surge_smelter = self.__add_region("Surge Smelter", MindustryLocations.serpulo_surge_smelter)
        self.node_separator = self.__add_region("Separator", MindustryLocations.serpulo_separator)
        self.node_disassembler = self.__add_region("Disasembler", MindustryLocations.serpulo_disassembler)
        self.node_cryofluid_mixer = self.__add_region("Cryofluid Mixer", MindustryLocations.serpulo_cryofluid_mixer)
        self.node_micro_processor = self.__add_region("Micro Processor", MindustryLocations.serpulo_micro_processor)
        self.node_switch = self.__add_region("Switch", MindustryLocations.serpulo_switch)
        self.node_message = self.__add_region("Message", MindustryLocations.serpulo_message)
        self.node_logic_display = self.__add_region("Logic Display", MindustryLocations.serpulo_logic_display)
        self.node_large_logic_display = self.__add_region("Large Logic Display", MindustryLocations.serpulo_large_logic_display)
        self.node_memory_cell = self.__add_region("Memory Cell", MindustryLocations.serpulo_memory_cell)
        self.node_memory_bank = self.__add_region("Memory Bank", MindustryLocations.serpulo_memory_bank)
        self.node_logic_processor = self.__add_region("Logic Processor", MindustryLocations.serpulo_logic_processor)
        self.node_hyper_processor = self.__add_region("Hyper Processor", MindustryLocations.serpulo_hyper_processor)
        self.node_illuminator = self.__add_region("Illuminator", MindustryLocations.serpulo_illuminator)
        self.node_combustion_generator = self.__add_region("Combustion Generator", MindustryLocations.serpulo_combustion_generator)
        self.node_power_node = self.__add_region("Power Node", MindustryLocations.serpulo_power_node)
        self.node_large_power_node = self.__add_region("Large Power Node", MindustryLocations.serpulo_large_power_node)
        self.node_battery_diode = self.__add_region("Battery Diode", MindustryLocations.serpulo_battery_diode)
        self.node_surge_tower = self.__add_region("Surge Tower", MindustryLocations.serpulo_surge_tower)
        self.node_battery = self.__add_region("Battery", MindustryLocations.serpulo_battery)
        self.node_large_battery = self.__add_region("Large Battery", MindustryLocations.serpulo_large_battery)
        self.node_mender = self.__add_region("Mender", MindustryLocations.serpulo_mender)
        self.node_mend_projector = self.__add_region("Mend Projector", MindustryLocations.serpulo_mend_projector)
        self.node_force_projector = self.__add_region("Forced Projector", MindustryLocations.serpulo_force_projector)
        self.node_overdrive_projector = self.__add_region("Overdrive Projector", MindustryLocations.serpulo_overdrive_projector)
        self.node_overdrive_dome = self.__add_region("Overdrive Dome", MindustryLocations.serpulo_overdrive_dome)
        self.node_repair_point = self.__add_region("Repair Point", MindustryLocations.serpulo_repair_point)
        self.node_repair_turret = self.__add_region("Repair Turret", MindustryLocations.serpulo_repair_turret)
        self.node_steam_generator = self.__add_region("Steam Generator", MindustryLocations.serpulo_steam_generator)
        self.node_thermal_generator = self.__add_region("Thermal Generator", MindustryLocations.serpulo_thermal_generator)
        self.node_differential_generator = self.__add_region("Differiential Generator", MindustryLocations.serpulo_differential_generator)
        self.node_thorium_reactor = self.__add_region("Thorium Reactor", MindustryLocations.serpulo_thorium_reactor)
        self.node_impact_reactor = self.__add_region("Impact Reactor", MindustryLocations.serpulo_impact_reactor)
        self.node_rtg_generator = self.__add_region("RTG Generator", MindustryLocations.serpulo_rtg_generator)
        self.node_solar_panel = self.__add_region("Solar Panel", MindustryLocations.serpulo_solar_panel)
        self.node_large_solar_panel = self.__add_region("Large Solar Panel", MindustryLocations.serpulo_large_solar_panel)
        self.node_duo = self.__add_region("Duo", None)
        self.node_copper_wall = self.__add_region("Copper Wall", None)
        self.node_large_copper_wall = self.__add_region("Large Copper Wall", MindustryLocations.serpulo_large_copper_wall)
        self.node_titanium_wall = self.__add_region("Titanium Wall", MindustryLocations.serpulo_titanium_wall)
        self.node_large_titanium_wall = self.__add_region("Large Titanium Wall", MindustryLocations.serpulo_large_titanium_wall)
        self.node_door = self.__add_region("Door", MindustryLocations.serpulo_door)
        self.node_large_door = self.__add_region("Large Door", MindustryLocations.serpulo_large_door)
        self.node_plastanium_wall = self.__add_region("Plastanium Wall", MindustryLocations.serpulo_plastanium_wall)
        self.node_large_plastanium_wall = self.__add_region("Large Plastanium Wall", MindustryLocations.serpulo_large_plastanium_wall)
        self.node_thorium_wall = self.__add_region("Thorium Wall", MindustryLocations.serpulo_thorium_wall)
        self.node_large_thorium_wall = self.__add_region("Large Thorium Wall", MindustryLocations.serpulo_large_thorium_wall)
        self.node_surge_wall = self.__add_region("Surge Wall", MindustryLocations.serpulo_surge_wall)
        self.node_large_surge_wall = self.__add_region("Large Surge Wall", MindustryLocations.serpulo_large_surge_wall)
        self.node_phase_wall = self.__add_region("Phase Wall", MindustryLocations.serpulo_phase_wall)
        self.node_large_phase_wall = self.__add_region("Large Phase Wall", MindustryLocations.serpulo_large_phase_wall)
        self.node_scatter = self.__add_region("Scatter", None)
        self.node_hail = self.__add_region("Hail", MindustryLocations.serpulo_hail)
        self.node_salvo = self.__add_region("Salvo", MindustryLocations.serpulo_salvo)
        self.node_swarmer = self.__add_region("Swarmer", MindustryLocations.serpulo_swarmer)
        self.node_cyclone = self.__add_region("Cyclone", MindustryLocations.serpulo_cyclone)
        self.node_spectre = self.__add_region("Spectre", MindustryLocations.serpulo_spectre)
        self.node_ripple = self.__add_region("Ripple", MindustryLocations.serpulo_ripple)
        self.node_fuse = self.__add_region("Fuse", MindustryLocations.serpulo_fuse)
        self.node_scorch = self.__add_region("Scorch", MindustryLocations.serpulo_scorch)
        self.node_arc = self.__add_region("Arc", MindustryLocations.serpulo_arc)
        self.node_wave = self.__add_region("Wave", MindustryLocations.serpulo_wave)
        self.node_parallax = self.__add_region("Parallax", MindustryLocations.serpulo_parallax)
        self.node_segment = self.__add_region("Segment", MindustryLocations.serpulo_segment)
        self.node_tsunami = self.__add_region("Tsunami", MindustryLocations.serpulo_tsunami)
        self.node_lancer = self.__add_region("Lancer", MindustryLocations.serpulo_lancer)
        self.node_meltdown = self.__add_region("Meltdown", MindustryLocations.serpulo_meltdown)
        self.node_foreshadow = self.__add_region("Foreshadow", MindustryLocations.serpulo_foreshadow)
        self.node_shock_mine = self.__add_region("Shock Mine", MindustryLocations.serpulo_shock_mine)
        self.node_ground_factory = self.__add_region("Ground Factory", MindustryLocations.serpulo_ground_factory)
        self.node_dagger = self.__add_region("Dagger", MindustryLocations.serpulo_dagger)
        self.node_mace = self.__add_region("Mace", MindustryLocations.serpulo_mace)
        self.node_fortress = self.__add_region("Fortress", MindustryLocations.serpulo_fortress)
        self.node_scepter = self.__add_region("Scepter", MindustryLocations.serpulo_scepter)
        self.node_reign = self.__add_region("Reign", MindustryLocations.serpulo_reign)
        self.node_nova = self.__add_region("Nova", MindustryLocations.serpulo_nova)
        self.node_pulsar = self.__add_region("Pulsar", MindustryLocations.serpulo_pulsar)
        self.node_quasar = self.__add_region("Quasar", MindustryLocations.serpulo_quasar)
        self.node_vela = self.__add_region("Vela", MindustryLocations.serpulo_vela)
        self.node_corvus = self.__add_region("Corvus", MindustryLocations.serpulo_corvus)
        self.node_crawler = self.__add_region("Crawler", MindustryLocations.serpulo_crawler)
        self.node_atrax = self.__add_region("Atrax", MindustryLocations.serpulo_atrax)
        self.node_spiroct = self.__add_region("Spiroct", MindustryLocations.serpulo_spiroct)
        self.node_arkyid = self.__add_region("Arkyid", MindustryLocations.serpulo_arkyid)
        self.node_toxopid = self.__add_region("Toxopid", MindustryLocations.serpulo_toxopid)
        self.node_air_factory = self.__add_region("Air Factory", MindustryLocations.serpulo_air_factory)
        self.node_flare = self.__add_region("Flare", MindustryLocations.serpulo_flare)
        self.node_horizon = self.__add_region("Horizon", MindustryLocations.serpulo_horizon)
        self.node_zenith = self.__add_region("Zenith", MindustryLocations.serpulo_zenith)
        self.node_antumbra = self.__add_region("Antumbra", MindustryLocations.serpulo_antumbra)
        self.node_eclipse = self.__add_region("Eclipse", MindustryLocations.serpulo_eclipse)
        self.node_mono = self.__add_region("Mono", MindustryLocations.serpulo_mono)
        self.node_poly = self.__add_region("Poly", MindustryLocations.serpulo_poly)
        self.node_mega = self.__add_region("Mega", MindustryLocations.serpulo_mega)
        self.node_quad = self.__add_region("Quad", MindustryLocations.serpulo_quad)
        self.node_oct = self.__add_region("Oct", MindustryLocations.serpulo_oct)
        self.node_naval_factory = self.__add_region("Naval Factory", MindustryLocations.serpulo_naval_factory)
        self.node_risso = self.__add_region("Risso", MindustryLocations.serpulo_risso)
        self.node_minke = self.__add_region("Minke", MindustryLocations.serpulo_minke)
        self.node_bryde = self.__add_region("Bryde", MindustryLocations.serpulo_bryde)
        self.node_sei = self.__add_region("Sei", MindustryLocations.serpulo_sei)
        self.node_omura = self.__add_region("Omura", MindustryLocations.serpulo_omura)
        self.node_retusa = self.__add_region("Retusa", MindustryLocations.serpulo_retusa)
        self.node_oxynoe = self.__add_region("Oxynoe", MindustryLocations.serpulo_oxynoe)
        self.node_cyerce = self.__add_region("Cyerce", MindustryLocations.serpulo_cyerce)
        self.node_aegires = self.__add_region("Aegires", MindustryLocations.serpulo_aegires)
        self.node_navanax = self.__add_region("Navanax", MindustryLocations.serpulo_navanax)
        self.node_additive_reconstructor = self.__add_region("Additive Reconstructor", MindustryLocations.serpulo_additive_reconstructor)
        self.node_multiplicative_reconstructor = self.__add_region("Multiplicative Reconstructor", MindustryLocations.serpulo_multiplicative_reconstructor)
        self.node_exponential_reconstructor = self.__add_region("Exponential Reconstructor", MindustryLocations.serpulo_exponential_reconstructor)
        self.node_tetrative_reconstructor = self.__add_region("Tetrative Reconstructor", MindustryLocations.serpulo_tetrative_reconstructor)
        self.node_ground_zero = self.__add_region("Ground Zero", None)
        self.node_frozen_forest = self.__add_region("Frozen Forest", None)
        self.node_the_craters = self.__add_region("The Craters", None)
        self.node_ruinous_shores = self.__add_region("Ruinous Shores", None)
        self.node_windswept_islands = self.__add_region("Windswept Islands", None)
        self.node_tar_fields = self.__add_region("Tar Fields", None)
        self.node_impact_0078 = self.__add_region("Impact 0078", None)
        self.node_desolate_rift = self.__add_region("Desolate Rift", None)
        self.node_planetary_launch_terminal = self.__add_region("Planetary Launch Terminal", None)
        self.node_extraction_outpost = self.__add_region("Extraction Outpost", None)
        self.node_salt_flats = self.__add_region("Salt Flats", None)
        self.node_coastline = self.__add_region("Coastline", None)
        self.node_naval_fortress = self.__add_region("Naval Fortress", None)
        self.node_overgrowth = self.__add_region("Overgrowth", None)
        self.node_biomass_synthesis_facility = self.__add_region("Biomass Synthesis Facility", None)
        self.node_stained_mountains = self.__add_region("Stained Mountains", None)
        self.node_fungal_pass = self.__add_region("Fungal Pass", None)
        self.node_nuclear_production_complex = self.__add_region("Nuclear Production Complex", None)
        self.node_copper = self.__add_region("Copper", None)
        self.node_water = self.__add_region("Water", None)
        self.node_sand = self.__add_region("Sand", None)
        self.node_lead = self.__add_region("Lead", None)
        self.node_titanium = self.__add_region("Titanium", None)
        self.node_cryofluid = self.__add_region("Cryofluid", None)
        self.node_thorium = self.__add_region("Thorium", None)
        self.node_surge_alloy = self.__add_region("Surge Alloy", None)
        self.node_phase_fabric = self.__add_region("Phase Fabric", None)
        self.node_metaglass = self.__add_region("Metaglass", None)
        self.node_scrap = self.__add_region("Scrap", None)
        self.node_slag = self.__add_region("Slag", None)
        self.node_coal = self.__add_region("Coal", None)
        self.node_graphite = self.__add_region("Graphite", None)
        self.node_silicon = self.__add_region("Silicon", None)
        self.node_pyratite = self.__add_region("Pyratite", None)
        self.node_blast_compound = self.__add_region("Blast Compound", None)
        self.node_spore_pod = self.__add_region("Spore Pod", None)
        self.node_oil = self.__add_region("Oil", None)
        self.node_plastanium = self.__add_region("Plastanium", None)

    def __add_serpulo_events(self):
        self.__add_event_location(self.node_frozen_forest, "Capture Frozen Forest", "Frozen Forest Captured")
        self.__add_event_location(self.node_the_craters, "Capture The Craters", "The Craters Captured")
        self.__add_event_location(self.node_ruinous_shores, "Capture Ruinous Shores", "Ruinous Shores Captured")
        self.__add_event_location(self.node_windswept_islands, "Capture Windswept Islands", "Windswept Islands Captured")
        self.__add_event_location(self.node_tar_fields, "Capture Tar Fields", "Tar Fields Captured")
        self.__add_event_location(self.node_impact_0078, "Capture Impact 0078", "Impact 0078 Captured")
        self.__add_event_location(self.node_desolate_rift, "Capture Desolate Rift", "Desolate Rift Captured")
        self.__add_event_location(self.node_planetary_launch_terminal, "Capture Planetary Launch Terminal", "Planetary Launch Terminal Captured")
        self.__add_event_location(self.node_extraction_outpost, "Capture Extraction Outpost", "Extraction Outpost Captured")
        self.__add_event_location(self.node_salt_flats, "Capture Salt Flats", "Salt Flats Captured")
        self.__add_event_location(self.node_coastline, "Capture Coastline", "Coastline Captured")
        self.__add_event_location(self.node_naval_fortress, "Capture Naval Fortress", "Naval Fortress Captured")
        self.__add_event_location(self.node_overgrowth, "Capture Overgrowth", "Overgrowth Captured")
        self.__add_event_location(self.node_biomass_synthesis_facility, "Capture Biomass Synthesis Facility", "Biomass Synthesis Facility Captured")
        self.__add_event_location(self.node_stained_mountains, "Capture Stained Mountains", "Stained Mountains Captured")
        self.__add_event_location(self.node_fungal_pass, "Capture Fungal Pass", "Fungal Pass Captured")
        self.__add_event_location(self.node_nuclear_production_complex, "Capture Nuclear Production Complex", "Nuclear Production Complex Captured")
        self.__add_event_location(self.node_titanium, "Produce Titanium", "Titanium Produced")
        self.__add_event_location(self.node_cryofluid, "Produce Cryofluid", "Cryofluid Produced")
        self.__add_event_location(self.node_thorium, "Produce Thorium", "Thorium Produced")
        self.__add_event_location(self.node_surge_alloy, "Produce Surge Alloy", "Surge Alloy Produced")
        self.__add_event_location(self.node_phase_fabric, "Produce Phase Fabric", "Phase Fabric Produced")
        self.__add_event_location(self.node_metaglass, "Produce Metaglass", "Metaglass Produced")
        self.__add_event_location(self.node_coal, "Produce Coal", "Coal Produced")
        self.__add_event_location(self.node_graphite, "Produce Graphite", "Graphite Produced")
        self.__add_event_location(self.node_silicon, "Produce Silicon", "Silicon Produced")
        self.__add_event_location(self.node_pyratite, "Produce Pyratite", "Pyratite Produced")
        self.__add_event_location(self.node_blast_compound, "Produce Blast Compound", "Blast Compound Produced")
        self.__add_event_location(self.node_spore_pod, "Produce Spore Pod", "Spore Pod Produced")
        self.__add_event_location(self.node_oil, "Produce Oil", "Plastanium Produced")
