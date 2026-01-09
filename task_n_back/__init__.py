from otree.api import *
import random
import json


class C(BaseConstants):
    NAME_IN_URL = 'n_back'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # --- ADJUSTABLE PARAMETERS ---
    N_LEVEL = 2  # The 'n' in N-Back (1, 2, or 3)
    NUM_TRIALS = 30  # Total number of stimuli in the main task
    MATCH_PROPORTION = 0.25  # 25% of trials will be matches (targets)
    STIMULUS_DURATION = 600  # Display time in milliseconds
    ISI_FIXED = 2000  # Inter-Stimulus Interval (break) in milliseconds
    LETTERS = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M']  # Pool of letters

    # --- PRACTICE ROUND PARAMETERS ---
    PRACTICE_TRIALS = 15  # Number of trials in the practice session
    PRACTICE_MATCH_PROPORTION = 0.33  # 33% of trials will be matches (targets)


class Player(BasePlayer):
    n_back_level = models.IntegerField()
    task_data_json = models.LongStringField()

    # Aggregated data
    total_hits = models.IntegerField(initial=0)
    total_false_alarms = models.IntegerField(initial=0)
    avg_rt_ms = models.FloatField()


def creating_session(subsession):
    """Initial session setup (currently no global logic needed)."""
    pass


def make_nback_sequence(num_trials, n_level, match_proportion):
    """
    Generates a controlled N-Back sequence with a specific match rate.

    Args:
        num_trials: Total length of the sequence
        n_level: The N-Back difficulty (e.g., 2)
        match_proportion: Desired ratio of target trials
    """
    n = n_level
    trials = []

    # Start with n random letters to build the initial memory buffer
    stimuli = [random.choice(C.LETTERS) for _ in range(n)]

    # Determine which indices will be matches (starting from index n)
    num_matches = int(num_trials * match_proportion)
    match_indices = random.sample(range(n, num_trials), num_matches)

    # Build the rest of the sequence
    for i in range(n, num_trials):
        if i in match_indices:
            # Create a match: Use the letter from n positions back
            stimuli.append(stimuli[i - n])
        else:
            # Create a non-match: Choose a random letter that is NOT the match letter
            remaining = [l for l in C.LETTERS if l != stimuli[i - n]]
            stimuli.append(random.choice(remaining))

    # Convert the raw stimuli into trial dictionaries for the frontend
    for i, char in enumerate(stimuli):
        is_match = False
        if i >= n:
            is_match = (stimuli[i] == stimuli[i - n])

        trials.append({
            'trial_id': i + 1,
            'letter': char,
            'is_match': is_match
        })
    return trials


# PAGES
class Instructions(Page):
    """Introduction page explaining the rules of the N-Back task."""

    @staticmethod
    def vars_for_template(player):
        return dict(n=C.N_LEVEL)


class PracticePage(Page):
    """Practice round with visual aids and immediate feedback."""

    @staticmethod
    def vars_for_template(player):
        practice_trials = make_nback_sequence(
            C.PRACTICE_TRIALS,
            C.N_LEVEL,
            C.PRACTICE_MATCH_PROPORTION
        )
        return dict(
            trials=practice_trials,
            n=C.N_LEVEL,
            stim_ms=C.STIMULUS_DURATION,
            isi_ms=C.ISI_FIXED
        )


class StartMainTask(Page):
    """Transition page to warn the player that the real task is about to start."""
    pass


class TaskPage(Page):
    """The actual N-Back task where reaction times and accuracy are recorded."""
    form_model = 'player'
    form_fields = ['task_data_json']

    @staticmethod
    def vars_for_template(player):
        player.n_back_level = C.N_LEVEL
        return dict(
            trials=make_nback_sequence(C.NUM_TRIALS, C.N_LEVEL, C.MATCH_PROPORTION),
            n=C.N_LEVEL,
            stim_ms=C.STIMULUS_DURATION,
            isi_ms=C.ISI_FIXED
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        """Processes the JSON data from the frontend and calculates summary statistics."""
        data = json.loads(player.task_data_json)

        # Calculate performance metrics
        rts = [t['rt'] for t in data if t['rt'] is not None]
        hits = sum(1 for t in data if t['is_match'] and t['responded'])
        false_alarms = sum(1 for t in data if not t['is_match'] and t['responded'])

        # Store results in the database
        player.total_hits = hits
        player.total_false_alarms = false_alarms
        if rts:
            player.avg_rt_ms = sum(rts) / len(rts)


# Define the sequence of pages
page_sequence = [Instructions, PracticePage, StartMainTask, TaskPage]

# Required oTree infrastructure classes (not used for this single-player task)
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass