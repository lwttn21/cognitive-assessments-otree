from otree.api import *

doc = """
Trail Making Test (TMT) - Part B.
Measures cognitive flexibility and set-shifting abilities.
"""


class C(BaseConstants):
    NAME_IN_URL = 'tmt_b'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_CIRCLES = 20            # Number of targets (alternating numbers/letters) to be connected


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Total count of sequence errors (e.g., clicking '2' after '1' instead of 'A')
    tmt_b_errors = models.IntegerField(initial=0)

    # Total time from start to completion in seconds
    tmt_b_duration = models.FloatField()

    # Calculated average time per target (reflecting higher cognitive load)
    tmt_b_avg_speed = models.FloatField()


# --- PAGES ---

class TMTBIntroduction(Page):
    """Instructions page explaining the alternating number-letter rule."""
    pass


class TMTBExercise(Page):
    """The interactive TMT-B task with alternating sequence logic."""
    form_model = 'player'
    form_fields = ['tmt_b_errors', 'tmt_b_duration', 'tmt_b_avg_speed']


class TMTBResults(Page):
    """Feedback page showing Part B performance metrics."""

    def vars_for_template(player: Player):
        # Format duration for clean display in the results table
        return {
            'duration_formatted': "{:.2f}".format(player.tmt_b_duration)
        }


page_sequence = [TMTBIntroduction, TMTBExercise, TMTBResults]