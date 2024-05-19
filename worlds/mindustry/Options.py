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

class NumberedSectorAreLocation(Toggle):
    """Add numbered sector to Mindustry locations"""
    display_name = "Numbered sector location"

class AllowPause(DefaultOnToggle):
    """Allow pause (space bar not ESC pause)."""
    display_name = "Allow pause"

class DisableInvasions(Toggle):
    """Disable invasions and prevent losing progress."""
    display_name = "Disable invasions"

class EarlyRessources(Toggle):
    """Place Lead and Coal earlier in the generation to prevent being stuck too early"""
    display_name = "Early ressources"

@dataclass
class MindustryOptions(PerGameCommonOptions):
    """
    Options for Mindustry randomizer.
    """
    tutorial_skip: TutorialSkip
    campaign_choice: CampaignChoice
    numbered_sector_are_location: NumberedSectorAreLocation
    allow_pause: AllowPause
    disable_invasions: DisableInvasions
    early_ressources: EarlyRessources
