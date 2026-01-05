from otree.api import *
import random
import json

doc = """
    Go/No-Go Task (SART Paradigm).
    Participants must press SPACE for every letter appearing, 
    but inhibit the response for the letter 'X'.
"""


class C(BaseConstants):
    NAME_IN_URL = 'go_no_go'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # --- Parameters ---
    NUM_TRIALS = 45
    NO_GO_LETTER = 'X'
    NO_GO_PROPORTION = 0.10

    LETTERS = [chr(i) for i in range(65, 91)]  # Generates A-Z
    STIM_DURATION_MS = 250
    ISI_VALUES_MS = [1000, 2000, 4000]  # Inter-stimulus intervals
    RESPONSE_KEY = ' '


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Raw data storage (JSON string)
    task_data_json = models.LongStringField()

    # Timestamps
    time_started_iso = models.StringField()
    time_finished_iso = models.StringField()

    # Aggregated results (for Excel export)
    total_trials = models.IntegerField(initial=0)
    total_hits = models.IntegerField(initial=0, label="Correct clicks on Go")
    total_misses = models.IntegerField(initial=0, label="Missed clicks on Go")
    total_correct_rejections = models.IntegerField(initial=0, label="Correctly withheld on No-Go")
    total_false_alarms = models.IntegerField(initial=0, label="Clicked on No-Go")
    avg_rt_ms = models.FloatField(label="Average Reaction Time (ms)")


# --- FUNCTIONS ---

def creating_session(subsession: Subsession):
    pass


def make_trial_sequence(seed):
    """
    Generates a randomized sequence of trials.
    Uses a seed for reproducibility across page reloads.
    """
    rng = random.Random(seed)

    trials = []
    letters_without_no_go = [l for l in C.LETTERS if l != C.NO_GO_LETTER]

    for i in range(C.NUM_TRIALS):
        is_no_go = rng.random() < C.NO_GO_PROPORTION

        if is_no_go:
            letter = C.NO_GO_LETTER
        else:
            letter = rng.choice(letters_without_no_go)

        isi = rng.choice(C.ISI_VALUES_MS)

        trials.append({
            'trial_id': i + 1,
            'letter': letter,
            'is_no_go': is_no_go,
            'isi_ms': isi
        })

    return trials


def compute_summary_stats(player: Player):
    """
    Parses the JSON data and calculates summary statistics for data export.
    """
    if not player.task_data_json:
        return

    data = json.loads(player.task_data_json)

    hits = 0
    misses = 0
    correct_rejections = 0
    false_alarms = 0
    rts = []

    for row in data:
        is_no_go = row['is_no_go']
        responded = row['responded']

        if not is_no_go:  # Go Trial
            if responded:
                hits += 1
                if row['rt_ms']:
                    rts.append(row['rt_ms'])
            else:
                misses += 1
        else:  # No-Go Trial
            if responded:
                false_alarms += 1
            else:
                correct_rejections += 1

    player.total_trials = len(data)
    player.total_hits = hits
    player.total_misses = misses
    player.total_correct_rejections = correct_rejections
    player.total_false_alarms = false_alarms

    if len(rts) > 0:
        player.avg_rt_ms = sum(rts) / len(rts)


# --- PAGES ---

class Introduction(Page):
    pass


class AssessmentPhaseTask(Page):
    form_model = 'player'
    form_fields = ['task_data_json', 'time_started_iso', 'time_finished_iso']

    @staticmethod
    def vars_for_template(player: Player):
        # Use participant code as seed so the sequence remains consistent on refresh
        trials = make_trial_sequence(seed=player.participant.code)

        return dict(
            RESPONSE_KEY=C.RESPONSE_KEY,
            STIM_DURATION_MS=C.STIM_DURATION_MS,
            TRIALS=trials,
            NO_GO_LETTER=C.NO_GO_LETTER
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.task_data_json:
            compute_summary_stats(player)


page_sequence = [Introduction, AssessmentPhaseTask]