from otree.api import *

doc = """
Trail Making Test (TMT) - Part A.
Scientific Objective: Measures visual search, scanning, and psychomotor processing speed.
Task: Participants connect numbered circles in ascending order (1-2-3-...) as fast as possible.
"""


class C(BaseConstants):
    NAME_IN_URL = 'tmt_a'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # --- CONFIGURATION ---
    # Standard TMT-A often uses 25, but 15 is common for shortened assessment batteries
    NUM_CIRCLES = 15


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # --- Performance Metrics ---
    tmt_a_errors = models.IntegerField(
        initial=0,
        label="Number of errors in TMT-A",
        doc="Total count of sequence errors (clicking the wrong number in the sequence)"
    )

    tmt_a_duration = models.FloatField(
        label="Duration in seconds",
        doc="Total time taken from the first click to the final circle in seconds"
    )

    tmt_a_avg_speed = models.FloatField(
        label="Average speed per circle (sec)",
        doc="Calculated mean time spent finding each consecutive target"
    )


# --- PAGES ---

class TMTAIntroduction(Page):
    """Introductory instructions. Essential for explaining the ascending numerical sequence."""
    pass


class TMTAExercise(Page):
    """
    Main interactive task page.
    Data is typically captured via JavaScript and submitted upon completion of the sequence.
    """
    form_model = 'player'
    form_fields = ['tmt_a_errors', 'tmt_a_duration', 'tmt_a_avg_speed']


class TMTAResults(Page):
    """Displays feedback to the participant. Useful for engagement in fatigue studies."""

    @staticmethod
    def vars_for_template(player: Player):
        # Rounding the duration for better readability in the user interface
        return {
            'duration_formatted': "{:.2f}".format(player.tmt_a_duration)
        }


page_sequence = [TMTAIntroduction, TMTAExercise, TMTAResults]