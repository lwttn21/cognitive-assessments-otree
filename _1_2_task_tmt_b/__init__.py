from otree.api import *

doc = """
Trail Making Test (TMT) - Part B.
Scientific Objective: Measures cognitive flexibility, set-shifting, and executive control.
Task: Participants connect circles in an alternating sequence of numbers and letters 
(1-A-2-B-3-C...) as fast as possible.
"""


class C(BaseConstants):
    NAME_IN_URL = 'tmt_b'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # --- CONFIGURATION ---
    # Total targets in the alternating sequence (e.g., up to the number 10 and letter J)
    NUM_CIRCLES = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # --- Performance Metrics ---
    tmt_b_errors = models.IntegerField(
        initial=0,
        doc="Count of sequence errors, specifically rule violations (e.g., 1 -> 2 instead of 1 -> A)"
    )

    tmt_b_duration = models.FloatField(
        doc="Total completion time in seconds. Reflects 'Switching' overhead compared to Part A"
    )

    tmt_b_avg_speed = models.FloatField(
        doc="Mean time per target. Usually significantly higher than TMT-A speed"
    )


# --- PAGES ---

class TMTBIntroduction(Page):
    """
    Instructions page.
    Crucial to emphasize the alternating rule (Number-Letter) to avoid initial confusion.
    """
    pass


class TMTBExercise(Page):
    """
    The interactive TMT-B task.
    The underlying JavaScript must validate the 1-A-2-B logic.
    """
    form_model = 'player'
    form_fields = ['tmt_b_errors', 'tmt_b_duration', 'tmt_b_avg_speed']


class TMTBResults(Page):
    """Display of results for Part B."""

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'duration_formatted': "{:.2f}".format(player.tmt_b_duration)
        }


page_sequence = [TMTBIntroduction, TMTBExercise, TMTBResults]