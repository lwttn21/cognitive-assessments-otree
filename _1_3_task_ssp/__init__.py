from otree.api import *
import random

doc = """
Spatial Span (SSP) / Corsi Block Tapping Task.

Measures visuospatial working memory capacity.
Participants must reproduce a sequence of lighting-up boxes in the correct order.

Mechanism:
- Starts with a sequence length of 2.
- Adaptive Logic:
  - Success -> Sequence length increases by 1 (Level Up).
  - Failure -> Error counter increases.
  - Stop Rule -> Two consecutive errors at the same length terminate the task.
"""


class C(BaseConstants):
    NAME_IN_URL = '_1_3_task_ssp'
    PLAYERS_PER_GROUP = None

    # We set a high number of rounds as a buffer.
    # The task usually terminates earlier via the stop rule.
    NUM_ROUNDS = 20

    # 9 Box Layout (Top %, Left %) relative to the container
    BOX_POSITIONS = [
        (10, 40), (25, 20), (25, 70),
        (50, 10), (50, 50), (50, 90),
        (75, 30), (75, 70), (90, 50)
    ]

    START_SPAN = 2
    BOX_FLASH_DURATION_MS = 500
    BOX_PAUSE_DURATION_MS = 250


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 'blank=True' is crucial here to prevent oTree validation errors
    # when data is submitted via hidden inputs.

    ssp_current_span_length = models.IntegerField(blank=True, doc="Length of sequence in this round")

    # Using IntegerField (1=True, 0=False) is more robust for hidden inputs than BooleanField
    ssp_is_correct = models.IntegerField(blank=True, initial=0, doc="1 if correct, 0 if incorrect")

    ssp_max_span = models.IntegerField(blank=True, initial=0, doc="Highest span length successfully completed")

    # Detailed logging for analysis
    ssp_sequence = models.StringField(blank=True, doc="The target sequence (e.g. '0-4-2')")
    ssp_response = models.StringField(blank=True, doc="The user response (e.g. '0-4-5')")
    ssp_rt_seq = models.LongStringField(blank=True, doc="Reaction timestamps for each click")


# --- FUNCTIONS ---

def creating_session(subsession: Subsession):
    """Initialize participant variables only in the first round."""
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.vars['ssp_active'] = True  # Is the game still running?
            p.participant.vars['ssp_span'] = C.START_SPAN  # Current difficulty level
            p.participant.vars['ssp_errors_at_span'] = 0  # Error counter for current level
            p.participant.vars['ssp_best_score'] = 0  # Highscore tracking


def generate_sequence(length):
    """Generates a random sequence of box indices (0-8) without immediate repeats."""
    seq = []
    last = -1
    for _ in range(length):
        # Filter available boxes to exclude the one just clicked
        choices = [i for i in range(len(C.BOX_POSITIONS)) if i != last]
        choice = random.choice(choices)
        seq.append(choice)
        last = choice
    return seq


# --- PAGES ---

class SSPInstruction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class SSP(Page):
    form_model = 'player'
    form_fields = ['ssp_is_correct', 'ssp_sequence', 'ssp_response', 'ssp_current_span_length', 'ssp_rt_seq']

    @staticmethod
    def is_displayed(player: Player):
        # Only display this page if the task is still active
        return player.participant.vars.get('ssp_active', False)

    @staticmethod
    def js_vars(player: Player):
        # Retrieve the current difficulty level from participant vars
        current_span = player.participant.vars['ssp_span']

        # Generate a new random sequence for this round
        sequence = generate_sequence(current_span)

        return {
            'box_positions': C.BOX_POSITIONS,
            'sequence': sequence,
            'flash_duration': C.BOX_FLASH_DURATION_MS,
            'pause_duration': C.BOX_PAUSE_DURATION_MS
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        # Log the difficulty of the current round
        player.ssp_current_span_length = participant.vars['ssp_span']

        # Logic: Did the player answer correctly? (1 = Yes)
        if player.ssp_is_correct == 1:
            # Correct Answer

            # 1. Update Highscore
            if player.ssp_current_span_length > participant.vars['ssp_best_score']:
                participant.vars['ssp_best_score'] = player.ssp_current_span_length

            # 2. Increase Difficulty (Level Up)
            participant.vars['ssp_span'] += 1
            participant.vars['ssp_errors_at_span'] = 0  # Reset errors for new level

        else:
            # Incorrect Answer
            participant.vars['ssp_errors_at_span'] += 1

            # Stop Rule: If 2 errors occur at the same span length -> Terminate
            if participant.vars['ssp_errors_at_span'] >= 2:
                participant.vars['ssp_active'] = False

            # If only 1 error, the loop continues with the SAME span length (Second Chance)

        # Save the current highscore to the player model for easy data export
        player.ssp_max_span = participant.vars['ssp_best_score']


class SSPResults(Page):
    @staticmethod
    def is_displayed(player: Player):
        # Show results only when the game is inactive OR it's the final round
        return (not player.participant.vars.get('ssp_active', False)) or (player.round_number == C.NUM_ROUNDS)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'final_score': player.participant.vars.get('ssp_best_score', 0)
        }


page_sequence = [SSPInstruction, SSP, SSPResults]