from otree.api import *

doc = """
Multidimensional Mental Fatigue Inventory (MFI) - Short Subscale.

Reference:
Smets, E. M. A., Garssen, B., Bonke, B. D., & De Haes, J. C. J. M. (1995).
The Multidimensional Fatigue Inventory (MFI) psychometric qualities of an instrument to assess fatigue.
Journal of psychosomatic research, 39(3), 315-325.

Scale: 
-3 (No, that is not true) to +3 (Yes, that is true).
"""


class C(BaseConstants):
    NAME_IN_URL = '_2_survey_mfi'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Note: If embedding this in a loop (e.g., measuring fatigue multiple times),
    # set NUM_ROUNDS to the total number of rounds in your experiment.


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # We use IntegerFields because the slider returns discrete values (-3 to 3).
    # The 'label' argument is used for documentation purposes.

    mfi_1 = models.IntegerField(
        min=-3, max=3,
        label="I feel fit"
    )
    mfi_2 = models.IntegerField(
        min=-3, max=3,
        label="I feel tired"
    )
    mfi_3 = models.IntegerField(
        min=-3, max=3,
        label="I have a lot of energy"
    )
    mfi_4 = models.IntegerField(
        min=-3, max=3,
        label="I feel exhausted"
    )


# --- PAGES ---

class MentalFatigueInventory(Page):
    form_model = 'player'
    # List of fields to be saved from the form
    form_fields = ['mfi_1', 'mfi_2', 'mfi_3', 'mfi_4']

    @staticmethod
    def is_displayed(player: Player):
        """
        Logic to determine when this survey appears.

        If used as a standalone app, simply return True.
        If used inside a multi-round loop (e.g. 108 rounds), uncomment the logic below
        to show it only on specific rounds (e.g., Baseline, Middle, End).
        """
        # Example for a multi-round experiment:
        # return player.round_number in [3, 57, 93]

        return True


page_sequence = [MentalFatigueInventory]