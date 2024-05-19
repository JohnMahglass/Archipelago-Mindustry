import json

from BaseClasses import Region, MultiWorld, Entrance, CollectionState, ItemClassification
from .Items import MindustryItem
from .Options import MindustryOptions
from .Locations import MindustryLocation
from typing import Optional
from worlds.generic.Rules import set_rule

def _has_frozen_forest(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Frozen Forest", player)

def _has_the_craters(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("The Craters", player)

def _has_ruinous_shores(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Ruinous Shores", player)

def _has_windswept_islands(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Windswept Islands", player)

def _has_tar_field(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Tar Field", player)

def _has_impact_0078(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Impact 0078", player)

def _has_desolate_rift(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Desolate Rift", player)

def _has_planetary_launch_terminal(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Planetary Launch Terminal", player)

def _has_extraction_outpost(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Extraction Outpost", player)

def _has_salt_flats(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Salt Flats", player)

def _has_coastline(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Coastline", player)

def _has_naval_fortress(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Naval Fortress", player)

def _has_overgrowth(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Overgrowth", player)

def _has_biomass_synthesis_facility(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Biomass Synthesis Facility", player)

def _has_stained_mountains(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Stained Mountains", player)

def _has_fungal_pass(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Fungal Pass", player)

def _has_nuclear_production_complex(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Nuclear Production Complex", player)

def _has_lead(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Lead", player)

def _has_titanium(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Titanium", player)

def _has_cryofluid(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Cryofluid", player)

def _has_thorium(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Thorium", player)

def _has_surge_alloy(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Surge Alloy", player)

def _has_phase_fabric(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Phase Fabric", player)

def _has_metaglass(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Metaglass", player)

def _has_scrap(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Scrap", player)

def _has_slag(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Slag", player)

def _has_coal(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Coal", player)

def _has_graphite(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Graphite", player)

def _has_silicon(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Silicon", player)

def _has_pyratite(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Pyratite", player)

def _has_blast_compound(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Blast Compound", player)

def _has_spore_pod(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Spore Pod", player)

def _has_oil(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Oil", player)

def _has_plastanium(state:CollectionState, player: int) -> bool:
    """If the player has target in state"""
    return state.has("Plastanium", player)

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
        #if self.options.campaign_choice == 0:
            #self.__connect_serpulo_campaign()
        #elif self.options.campaign_choice == 1:
            #self.__connect_erekir_campaign()
        #elif self.options.campaign_choice == 2:
            #self.__connect_all_campaign()
        #else:
            #raise ValueError("Invalid campaign choice")
        self.__connect_serpulo_campaign()

    def add_regions_to_world(self) -> None:
        """
        Add every region to the `world`
        """
        self.__add_serpulo_regions_to_world()

    def add_event_locations(self) -> None:
        """
        Add every event (locations and items) to the `world`
        """
        self.__add_event_location(self.final_room_end, "Objective complete",
                                  "Victory")


    def initialise_rules(self, options: MindustryOptions) -> None:
        """Initialise rules"""
        pass


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
        location.place_locked_item(MindustryItem(event_name,
                                               ItemClassification.progression,
                                               None,
                                               self.player))


    def __add_serpulo_regions_to_world(self):
        pass


    def __create_campaign(self, campaign: int):
        """
        Create region for selected campaign
        """
        self.menu = self.__add_region("Menu", None)
        self.victory = self.__add_region("Victory", None)
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


    def __connect_serpulo_campaign(self):
        """
        Connect region related to Serpulo's campaign
        """
        self.__connect_regions(self.menu, self.serpulo)
        self.__connect_regions(self.menu, self.victory)
        self.__connect_regions(self.serpulo, self.node_core_shard)

        self.__connect_regions(self.node_core_shard, self.node_conveyor)
        self.__connect_regions(self.node_conveyor, self.node_junction)
        self.__connect_regions(self.node_junction, self.node_router)
        self.__connect_regions(self.node_router, self.node_launch_pad,
                               lambda state: _has_extraction_outpost(state, self.player) and
                                                _has_silicon(state, self.player) and
                                                _has_lead(state, self.player) and
                                                _has_titanium(state, self.player))
        self.__connect_regions(self.node_router, self.node_distributor,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_router, self.node_sorter,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_sorter, self.node_inverted_sorter,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_sorter, self.node_overflow_gate,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_overflow_gate, self.node_underflow_gate,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_router, self.node_container,
                               lambda state: _has_biomass_synthesis_facility(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_container, self.node_unloader,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_container, self.node_vault,
                               lambda state: _has_stained_mountains(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_router, self.node_bridge_conveyor,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_bridge_conveyor, self.node_titanium_conveyor,
                               lambda state: _has_the_craters(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_titanium_conveyor, self.node_phase_conveyor,
                               lambda state: _has_lead(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_phase_conveyor, self.node_mass_driver,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_titanium_conveyor, self.node_payload_conveyor,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_payload_conveyor, self.node_payload_router,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_titanium_conveyor, self.node_armored_conveyor,
                               lambda state: _has_plastanium(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_armored_conveyor, self.node_plastanium_conveyor,
                               lambda state: _has_plastanium(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player))

        self.__connect_regions(self.node_core_shard, self.node_core_foundation,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_core_foundation, self.node_core_nucleus,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_thorium(state, self.player))

        self.__connect_regions(self.node_core_shard, self.node_mechanical_drill)
        self.__connect_regions(self.node_mechanical_drill, self.node_mechanical_pump,
                               lambda state: _has_metaglass(state, self.player))

        self.__connect_regions(self.node_mechanical_pump, self.node_conduit,
                               lambda state: _has_metaglass(state, self.player))
        self.__connect_regions(self.node_conduit, self.node_liquid_junction,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_liquid_junction, self.node_liquid_router,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_liquid_router, self.node_liquid_container,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_liquid_container, self.node_liquid_tank,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_liquid_router, self.node_bridge_conduit,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_liquid_router, self.node_pulse_conduit,
                               lambda state: _has_windswept_islands(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_pulse_conduit, self.node_phase_conduit,
                               lambda state: _has_phase_fabric(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_metaglass(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_pulse_conduit, self.node_plated_conduit,
                               lambda state: _has_thorium(state, self.player) and
                                            _has_metaglass(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_pulse_conduit, self.node_rotary_pump,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_rotary_pump, self.node_impulse_pump,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_thorium(state, self.player))

        self.__connect_regions(self.node_mechanical_drill, self.node_graphite_press,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_graphite_press, self.node_pneumatic_drill,
                               lambda state: _has_frozen_forest(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_pneumatic_drill, self.node_cultivator,
                               lambda state: _has_biomass_synthesis_facility(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_pneumatic_drill, self.node_laser_drill,
                               lambda state: _has_nuclear_production_complex(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_laser_drill, self.node_airblast_drill,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_laser_drill, self.node_water_extractor,
                               lambda state: _has_salt_flats(state, self.player) and
                                            _has_metaglass(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_water_extractor, self.node_oil_extractor,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_graphite_press, self.node_pyratite_mixer,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_pyratite_mixer, self.node_blast_mixer,
                               lambda state: _has_lead(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_graphite_press, self.node_silicon_smelter,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_silicon_smelter, self.node_spore_press,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_spore_press, self.node_coal_centrifuge,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_coal_centrifuge, self.node_multi_press,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_multi_press, self.node_silicon_crucible,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_spore_press, self.node_plastanium_compressor,
                               lambda state: _has_windswept_islands(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_plastanium_compressor, self.node_phase_weaver,
                               lambda state: _has_tar_field(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_silicon_smelter, self.node_kiln,
                               lambda state: _has_the_craters(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_kiln, self.node_pulveriser,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_pulveriser, self.node_incinerator,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_incinerator, self.node_melter,
                               lambda state: _has_lead(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_melter, self.node_surge_smelter,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_melter, self.node_separator,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_separator, self.node_disassembler,
                               lambda state: _has_plastanium(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_melter, self.node_cryofluid_mixer,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_silicon_smelter, self.node_micro_processor,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_micro_processor, self.node_switch,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_switch, self.node_message,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_message, self.node_logic_display,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_logic_display, self.node_large_logic_display,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_metaglass(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_message, self.node_memory_cell,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_memory_cell, self.node_memory_bank,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_switch, self.node_logic_processor,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_logic_processor, self.node_hyper_processor,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_silicon_smelter, self.node_illuminator,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_lead(state, self.player))

        self.__connect_regions(self.node_mechanical_drill, self.node_combustion_generator,
                               lambda state: _has_coal(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_combustion_generator, self.node_power_node,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_large_power_node,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_large_power_node, self.node_battery_diode,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_battery_diode, self.node_surge_tower,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_battery,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_battery, self.node_large_battery,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_mender,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_mender, self.node_mend_projector,
                               lambda state: _has_lead(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_mend_projector, self.node_force_projector,
                               lambda state: _has_impact_0078(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_force_projector, self.node_overdrive_projector,
                               lambda state: _has_impact_0078(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_overdrive_projector, self.node_overdrive_dome,
                               lambda state: _has_impact_0078(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_mend_projector, self.node_repair_point,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_repair_point, self.node_repair_turret,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_steam_generator,
                               lambda state: _has_the_craters(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_steam_generator, self.node_thermal_generator,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_thermal_generator, self.node_differential_generator,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_differential_generator, self.node_thorium_reactor,
                               lambda state: _has_cryofluid(state, self.player))
        self.__connect_regions(self.node_thorium_reactor, self.node_impact_reactor,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_differential_generator, self.node_rtg_generator,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_phase_fabric(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_power_node, self.node_solar_panel,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_solar_panel, self.node_large_solar_panel,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_phase_fabric(state, self.player))

        self.__connect_regions(self.node_core_shard, self.node_duo)
        self.__connect_regions(self.node_duo, self.node_copper_wall)
        self.__connect_regions(self.node_copper_wall, self.node_large_copper_wall)
        self.__connect_regions(self.node_large_copper_wall, self.node_titanium_wall,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_titanium_wall, self.node_large_titanium_wall,
                               lambda state: _has_titanium(state, self.player))
        self.__connect_regions(self.node_titanium_wall, self.node_door,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_door, self.node_large_door,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_titanium_wall, self.node_plastanium_wall,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_plastanium_wall, self.node_large_plastanium_wall,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_titanium_wall, self.node_thorium_wall,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_thorium_wall, self.node_large_thorium_wall,
                               lambda state: _has_thorium(state, self.player))
        self.__connect_regions(self.node_titanium_wall, self.node_surge_wall,
                               lambda state: _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_surge_wall, self.node_large_surge_wall,
                               lambda state: _has_surge_alloy(state, self.player))
        self.__connect_regions(self.node_surge_wall, self.node_phase_wall,
                               lambda state: _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_phase_wall, self.node_large_phase_wall,
                               lambda state: _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_duo, self.node_scatter,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_scatter, self.node_hail,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_hail, self.node_salvo,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_salvo, self.node_swarmer,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_swarmer, self.node_cyclone,
                               lambda state: _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_cyclone, self.node_spectre,
                               lambda state: _has_nuclear_production_complex(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_salvo, self.node_ripple,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_ripple, self.node_fuse,
                               lambda state: _has_graphite(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_duo, self.node_scorch,
                               lambda state: _has_graphite(state, self.player))
        self.__connect_regions(self.node_scorch, self.node_arc,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_arc, self.node_wave,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_wave, self.node_parallax,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_parallax, self.node_segment,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_phase_fabric(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_wave, self.node_tsunami,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_arc, self.node_lancer,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_lancer, self.node_meltdown,
                               lambda state: _has_lead(state, self.player) and
                                            _has_graphite(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_meltdown, self.node_foreshadow,
                               lambda state: _has_metaglass(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_lancer, self.node_shock_mine,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))

        self.__connect_regions(self.node_core_shard, self.node_ground_factory,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_ground_factory, self.node_dagger,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_dagger, self.node_mace,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_mace, self.node_fortress,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_metaglass(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_fortress, self.node_scepter,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_scepter, self.node_reign,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_dagger, self.node_nova,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_nova, self.node_pulsar,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_pulsar, self.node_quasar,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_quasar, self.node_vela,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_vela, self.node_corvus,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_dagger, self.node_crawler,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_coal(state, self.player))
        self.__connect_regions(self.node_crawler, self.node_atrax,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_atrax, self.node_spiroct,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_spiroct, self.node_arkyid,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_arkyid, self.node_toxopid,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_ground_factory, self.node_air_factory,
                               lambda state: _has_lead(state, self.player))
        self.__connect_regions(self.node_air_factory, self.node_flare,
                               lambda state: _has_silicon(state, self.player))
        self.__connect_regions(self.node_flare, self.node_horizon,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_horizon, self.node_zenith,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_zenith, self.node_antumbra,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_antumbra, self.node_eclipse,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_flare, self.node_mono,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_lead(state, self.player))
        self.__connect_regions(self.node_mono, self.node_poly,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_poly, self.node_mega,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_mega, self.node_quad,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_quad, self.node_oct,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_air_factory, self.node_naval_factory,
                               lambda state: _has_ruinous_shores(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_naval_factory, self.node_risso,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_risso, self.node_minke,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_minke, self.node_bryde,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_bryde, self.node_sei,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_sei, self.node_omura,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_surge_alloy(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_risso, self.node_retusa,
                               lambda state: _has_windswept_islands(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_metaglass(state, self.player) and
                                            _has_titanium(state, self.player))
        self.__connect_regions(self.node_retusa, self.node_oxynoe,
                               lambda state: _has_coastline(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_graphite(state, self.player))
        self.__connect_regions(self.node_oxynoe, self.node_cyerce,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_metaglass(state, self.player))
        self.__connect_regions(self.node_cyerce, self.node_aegires,
                               lambda state: _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_plastanium(state, self.player))
        self.__connect_regions(self.node_aegires, self.node_navanax,
                               lambda state: _has_naval_fortress(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_phase_fabric(state, self.player) and
                                            _has_surge_alloy(state, self.player))

        self.__connect_regions(self.node_ground_factory, self.node_additive_reconstructor,
                               lambda state: _has_biomass_synthesis_facility(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_silicon(state, self.player))
        self.__connect_regions(self.node_additive_reconstructor, self.node_multiplicative_reconstructor,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_thorium(state, self.player))
        self.__connect_regions(self.node_multiplicative_reconstructor, self.node_exponential_reconstructor,
                               lambda state: _has_overgrowth(state, self.player) and
                                            _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_titanium(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_phase_fabric(state, self.player))
        self.__connect_regions(self.node_exponential_reconstructor, self.node_tetrative_reconstructor,
                               lambda state: _has_lead(state, self.player) and
                                            _has_silicon(state, self.player) and
                                            _has_thorium(state, self.player) and
                                            _has_plastanium(state, self.player) and
                                            _has_phase_fabric(state, self.player) and
                                            _has_surge_alloy(state, self.player))


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


    def __add_region(self, hint: str, locations: Optional):
        """Create a new region."""
        region: Region = Region(hint, self.player, self.multiworld, hint)
        if locations is not None:
            region.add_locations(locations, MindustryLocation)
        return region


    def __connect_regions(self, source_region: Region, target_region: Region, rule = None) -> None:
        """
        Connect regions between themselves
        """
        entrance = Entrance(source_region.player, source_region.name + " -> " + target_region.name, source_region)
        source_region.exits.append(entrance)
        entrance.connect(target_region)

        entrance_reverse = Entrance(target_region.player, target_region.name + " -> " + source_region.name, target_region)
        target_region.exits.append(entrance_reverse)
        entrance_reverse.connect(source_region)

        if rule is not None:
            set_rule(entrance, rule)


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
        self.node_airblast_drill = self.__add_region("Airblast Drill", MindustryLocation.tech_tree_serpulo.get("Node Airblast Drill"))
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
        self.node_navanax = self.__add_region("Narvanax", MindustryLocation.tech_tree_serpulo.get("Node Narvanax"))
        self.node_additive_reconstructor = self.__add_region("Additive Reconstructor", MindustryLocation.tech_tree_serpulo.get("Node Additive Reconstructor"))
        self.node_multiplicative_reconstructor = self.__add_region("Multiplicative Reconstructor", MindustryLocation.tech_tree_serpulo.get("Node Multiplicative Reconstructor"))
        self.node_exponential_reconstructor = self.__add_region("Exponential Reconstructor", MindustryLocation.tech_tree_serpulo.get("Node Exponential Reconstructor"))
        self.node_tetrative_reconstructor = self.__add_region("Tetrative Reconstructor", MindustryLocation.tech_tree_serpulo.get("Node Tetrative Reconstructor"))
