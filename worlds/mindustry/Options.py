from dataclasses import dataclass
from Options import DefaultOnToggle, Choice, Toggle, PerGameCommonOptions


class TutorialSkip(Toggle):
    """Remove the need to complete the tutorial and unlock tutorial related tech."""
    display_name = "Tutorial skip"

class CampaignChoice(Choice):
    """Select Serpulo, Erekir or both for the randomized campaign."""
    display_name = "Campaign choice"
    option_serpulo_only = 0
    option_erekir_only = 1
    option_all_planets = 2
    default = 0

class SectorBehavior(Choice):
    """Add sectors to Mindustry locations and item list"""
    display_name = "Sector behavior"
    option_vanilla = 0
    option_sector_are_items = 1
    option_numbered_sector_are_items = 2
    default = 0

class RessourceBehavior(Choice):
    """Add ressources to Mindustry locations and item list"""
    display_name = "Sector behavior"
    option_vanilla = 0
    option_ressource_are_items = 1
    default = 0

class DisableInvasions(Toggle):
    """Disable invasions and prevent losing progress."""
    display_name = "Disable invasions"


@dataclass
class MindustryOptions(PerGameCommonOptions):
    """
    Options for Mindustry randomizer.
    """
    tutorial_skip: TutorialSkip
    campaign_choice: CampaignChoice
    sector_behavior: SectorBehavior
    ressource_behavior: RessourceBehavior
    disable_invasions: DisableInvasions
