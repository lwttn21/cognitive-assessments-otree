from otree.api import *

doc = """
Visual Analog Scales (VAS).
Measures subjective states (Fatigue, Motivation, Workload, Frustration) 
on a continuous scale from 0 (Not at all) to 100 (Very much).
"""


class C(BaseConstants):
    NAME_IN_URL = '_2_survey_vas'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # If integrated into the main loop, set NUM_ROUNDS to the total (e.g., 108)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # We use 0-100 integers to represent the slider position.
    # 0 = "Not at all", 100 = "Very much"

    mental_fatigue = models.IntegerField(
        min=0, max=100,
        label="How mentally fatigued do you feel right now?"
    )

    motivation = models.IntegerField(
        min=0, max=100,
        label="How motivated do you feel right now?"
    )

    mental_workload = models.IntegerField(
        min=0, max=100,
        label="How mentally demanded do you feel right now?"
    )

    frustration = models.IntegerField(
        min=0, max=100,
        label="How frustrated do you feel right now?"
    )


# --- PAGES ---

class VASPage(Page):
    form_model = 'player'
    form_fields = ['mental_fatigue', 'motivation', 'mental_workload', 'frustration']

    @staticmethod
    def is_displayed(player: Player):
        # Logic for displaying this page in specific rounds only.
        # Uncomment and adjust the list below for your full experiment.

        # return player.round_number in [3, 21, 39, 57, 75, 93]

        return True


page_sequence = [VASPage]