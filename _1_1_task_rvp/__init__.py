from otree.api import *
import random

doc = """
Rapid Visual Information Processing (RVP) Task.
Single Target Version: Participants look for ONE specific sequence per round.
"""


class C(BaseConstants):
    NAME_IN_URL = '_1_1_task_rvp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # --- CONFIGURATION ---
    DIGIT_SPEED_MS = 600
    NUM_DIGITS_TOTAL = 100
    NUM_TARGETS = 8

    # Available sequences
    TARGET_SEQUENCES = [
        [2, 4, 6],
        [3, 5, 7],
        [4, 6, 8]
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rvp_hits = models.IntegerField(initial=0, doc="Correctly detected sequences")
    rvp_misses = models.IntegerField(initial=0, doc="Missed sequences")
    rvp_false_alarms = models.IntegerField(initial=0, doc="Clicks without a target")
    rvp_avg_rt = models.FloatField(initial=0.0, doc="Average reaction time for hits")

    # We save which target was active for this player
    rvp_active_target = models.StringField(doc="The sequence the player had to find (e.g. '2-4-6')")
    rvp_raw_data = models.LongStringField(blank=True)


# --- LOGIC ---

def generate_rvp_stream(specific_target):
    """
    Generates a stream where ONLY 'specific_target' appears as a valid sequence.
    """
    # 1. Base stream (random 1-9)
    stream = [random.randint(1, 9) for _ in range(C.NUM_DIGITS_TOTAL)]

    possible_indices = list(range(0, C.NUM_DIGITS_TOTAL - 3))
    random.shuffle(possible_indices)

    targets_inserted = []

    count = 0
    for idx in possible_indices:
        if count >= C.NUM_TARGETS:
            break

        collision = False
        for existing_idx, _ in targets_inserted:
            if abs(existing_idx - idx) < 4:
                collision = True
                break

        if not collision:
            # Always insert the specific target selected for this round
            seq = specific_target

            stream[idx] = seq[0]
            stream[idx + 1] = seq[1]
            stream[idx + 2] = seq[2]

            targets_inserted.append((idx, seq))
            count += 1

    return stream


# --- PAGES ---

class RVPInstruction(Page):
    pass


class RVPTask(Page):
    form_model = 'player'
    form_fields = ['rvp_hits', 'rvp_misses', 'rvp_false_alarms', 'rvp_avg_rt', 'rvp_raw_data', 'rvp_active_target']

    @staticmethod
    def js_vars(player: Player):
        # 1. Pick ONE random target for this round
        target_seq = random.choice(C.TARGET_SEQUENCES)

        # 2. Generate stream only for this target
        stream = generate_rvp_stream(target_seq)

        # 3. Calculate indices
        target_indices = []
        for i in range(len(stream) - 2):
            triplet = [stream[i], stream[i + 1], stream[i + 2]]
            # Check if it matches OUR target
            if triplet == target_seq:
                target_indices.append(i + 2)

        # Create a string like "2 - 4 - 6" for the display
        target_string = f"{target_seq[0]} - {target_seq[1]} - {target_seq[2]}"

        return {
            'stream': stream,
            'target_indices': target_indices,
            'speed': C.DIGIT_SPEED_MS,
            'target_string': target_string  # Pass the label to JS
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Determine which target was used by looking at the raw data or hidden input
        # Ideally, we save it via JS, see below.
        pass


class RVPResults(Page):
    pass


page_sequence = [RVPInstruction, RVPTask, RVPResults]