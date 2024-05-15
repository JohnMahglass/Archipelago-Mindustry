import json
from dataclasses import dataclass
from Options import DefaultOnToggle, Choice, Toggle, PerGameCommonOptions


class TutorialSkip(DefaultOnToggle):
    """Remove the need to complete the tutorial and unlock tutorial related tech."""
    display_name = "Tutorial Skip"

class CampaignChoice(Choice):
    """Select Serpulo, Erekir or both for the randomized campaign."""
    display_name = "Campaign choice"
    serpulo_only = 0
    erekir_only = 1
    all_planets = 2

class NumberedSectorAreLocation(Toggle):
    """Add numbered sector to Mindustry locations"""
    display_name = "Numbered sector location"

class AllowPause(DefaultOnToggle):
    """Allow pause (space bar not ESC pause)."""
    display_name = "Allow Pause"


@dataclass
class MindustryOptions(PerGameCommonOptions):
    """
    Options for Mindustry randomizer.
    """
    tutorial_skip: TutorialSkip
    campaign_choice: CampaignChoice
    numbered_sector: NumberedSectorAreLocation
    allow_pause: AllowPause

    def __load_options_JSON(self):
        file = open("DefaultSettings.json", "r")
        data = json.load(file)
        self.tutorial_skip: bool = data["tutorialSkip"]
        self.campaign_choice: int = data["campainChoice"]
        self.numbered_sector: bool = data["numberedSectorAreLocation"]
        self.allow_pause: bool = data["allowPause"]
        file.close()

    def __init__(self):
        self.__load_options_JSON()

