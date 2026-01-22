from otree.api import *
import random

doc = """
Reaction Time Task (RTI) - Five Choice Version.
Measures Reaction Time (RT) and Movement Time (MT).
User clicks and holds 'Home', waits for stimulus, releases, and clicks target.
"""


class C(BaseConstants):
    NAME_IN_URL = '_1_1_task_rti'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # --- CONFIGURATION ---
    NUM_TRIALS = 15

    # Waiting time range before stimulus appears (in milliseconds)
    # Variable intervals prevent prediction
    DELAY_MIN_MS = 600
    DELAY_MAX_MS = 1500

    # Number of possible target locations (1 = Simple RTI, 5 = Five Choice RTI)
    NUM_LOCATIONS = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Summary Statistics
    rti_mean_rt = models.FloatField(doc="Mean Reaction Time (Release) in ms")
    rti_mean_mt = models.FloatField(doc="Mean Movement Time (Click) in ms")
    rti_total_score = models.IntegerField(doc="Number of successful trials")
    rti_errors = models.IntegerField(initial=0, doc="Early releases or wrong targets")

    # Detailed Log: "Trial_TargetIndex_RT_MT_Status"
    rti_raw_data = models.LongStringField(blank=True)


# --- LOGIC ---

def get_rti_trials():
    """Generates a list of trials with random targets and delays"""
    trials = []
    for i in range(C.NUM_TRIALS):
        trials.append({
            'target_index': random.randint(1, C.NUM_LOCATIONS),  # 1 to 5
            'delay': random.randint(C.DELAY_MIN_MS, C.DELAY_MAX_MS)
        })
    return trials


# --- PAGES ---

class RTIInstruction(Page):
    pass


class RTI(Page):
    form_model = 'player'
    form_fields = ['rti_mean_rt', 'rti_mean_mt', 'rti_total_score', 'rti_errors', 'rti_raw_data']

    @staticmethod
    def js_vars(player: Player):
        return {
            'trials': get_rti_trials(),
            'num_locations': C.NUM_LOCATIONS
        }


class RTIResults(Page):
    pass


page_sequence = [RTIInstruction, RTI, RTIResults]
