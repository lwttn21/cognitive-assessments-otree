from otree.api import *
import random

doc = """
Motor Screening Task (MOT.html).
Participants must click on flashing crosses appearing at random locations.
Measures: 
1. Reaction Time (Speed)
2. Spatial Accuracy (Distance from center of cross in pixels)
"""


class C(BaseConstants):
    NAME_IN_URL = 'task_mot'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Configuration
    NUM_TRIALS = 10  # Standard is often 10-15 trials
    CROSS_SIZE_PX = 40  # Size of the clickable cross
    CONTAINER_WIDTH = 800  # Width of the active area
    CONTAINER_HEIGHT = 600  # Height of the active area


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Summary Metrics
    mot_mean_rt = models.FloatField(doc="Average Reaction Time in ms")
    mot_mean_error = models.FloatField(doc="Average pixel distance from center")

    # Detailed Log: "Trial_X_Y_ClickX_ClickY_Error_RT"
    mot_raw_data = models.LongStringField(blank=True)


# --- PAGES ---

class MOTInstruction(Page):
    pass


class MOT(Page):
    form_model = 'player'
    form_fields = ['mot_mean_rt', 'mot_mean_error', 'mot_raw_data']

    @staticmethod
    def js_vars(player: Player):
        return {
            'num_trials': C.NUM_TRIALS,
            'cross_size': C.CROSS_SIZE_PX,
            'container_w': C.CONTAINER_WIDTH,
            'container_h': C.CONTAINER_HEIGHT
        }


class MOTResults(Page):
    pass


page_sequence = [MOTInstruction, MOT, MOTResults]