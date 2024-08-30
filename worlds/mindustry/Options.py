from dataclasses import dataclass
from Options import Choice, Toggle, PerGameCommonOptions, DefaultOnToggle


class TutorialSkip(Toggle):
    """Remove the need to complete the tutorial and unlock tutorial related tech. Grant a free launch for every selected planet."""
    display_name = "Tutorial skip"

class CampaignChoice(Choice):
    """Select Serpulo, Erekir or both for the randomized campaign."""
    display_name = "Campaign choice"
    option_serpulo_only = 0
    option_erekir_only = 1
    option_all_planets = 2
    default = 0

class DisableInvasions(Toggle):
    """Disable invasions and prevent losing progress."""
    display_name = "Disable invasions"

class FasterProduction(Toggle):
    """Enable faster production and harvesting of resources."""
    display_name = "Faster production"

class DeathLink(Toggle):
    """Enable death link."""
    display_name = "Death link"

class MilitaryLevelTracking(DefaultOnToggle):
    """Ensure the player has enough military power to clear sectors. If turned off, the logic will consider that the player can clear every sector once they have the minimal requirement to land on that sector."""
    display_name = "Military level tracking"

class RandomizePlayerShots(Toggle):
    """Will randomize the player shots for every player ship they can control."""
    display_name = "Randomize player shots"

class RandomizeBlockSize(Toggle):
    """Will randomize the size of blocks. Some blocks might be excluded from randomization."""
    display_name = "Randomize block size"

@dataclass
class MindustryOptions(PerGameCommonOptions):
    """
    Options for Mindustry randomizer.
    """
    tutorial_skip: TutorialSkip
    campaign_choice: CampaignChoice
    disable_invasions: DisableInvasions
    faster_production: FasterProduction
    death_link: DeathLink
    military_level_tracking: MilitaryLevelTracking
    randomize_player_shots: RandomizePlayerShots
    randomize_block_size: RandomizeBlockSize
