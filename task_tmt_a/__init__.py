from otree.api import *

doc = """
Trail Making Test (TMT) - Part A.
Measures visual search and motor processing speed.
"""


class C(BaseConstants):
    NAME_IN_URL = 'tmt_a'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_CIRCLES = 15        # Number of targets to be connected in the task


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Total count of sequence errors (wrong circles clicked)
    tmt_a_errors = models.IntegerField(initial=0, label="Number of errors in TMT-A")

    # Total time from start to completion in seconds
    tmt_a_duration = models.FloatField(label="Duration in seconds")

    # Calculated average time per circle found
    tmt_a_avg_speed = models.FloatField(label="Average speed per circle (sec)")


# --- PAGES ---

class TMTAIntroduction(Page):
    """Instructions page with visual examples."""
    pass


class TMTAExercise(Page):
    """The actual interactive TMT task."""
    form_model = 'player'
    form_fields = ['tmt_a_errors', 'tmt_a_duration', 'tmt_a_avg_speed']


class TMTAResults(Page):
    """Feedback page showing performance metrics."""

    def vars_for_template(player: Player):
        # Format duration to 2 decimal places for the UI
        return {
            'duration_formatted': "{:.2f}".format(player.tmt_a_duration)
        }


page_sequence = [TMTAIntroduction, TMTAExercise, TMTAResults]