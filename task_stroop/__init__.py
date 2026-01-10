from otree.api import *
import random

doc = """
Stroop Task (Color-Word Interference)
Participants must identify the ink color of the word, ignoring the word itself.
"""


class C(BaseConstants):
    NAME_IN_URL = 'task_stroop'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Configuration
    # We define pairs of (Hex Color, Name)
    COLORS = [
        ('#FF0000', 'red'),
        ('#0000FF', 'blue'),
        ('#008000', 'green'),
        ('#FFA500', 'orange')  # Changed yellow to orange for better visibility on white
    ]
    WORDS = ['RED', 'BLUE', 'GREEN', 'ORANGE']

    NUM_TRIALS = 20
    TIMEOUT_SECONDS = 30#120  # 2 minutes total limit


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Optimized field names
    stroop_score = models.IntegerField(initial=0, doc="Number of correct trials")
    stroop_errors = models.IntegerField(initial=0, doc="Number of incorrect trials")
    stroop_avg_rt = models.FloatField(initial=0.0, doc="Average reaction time in ms")

    # We save the full history for detailed analysis later
    stroop_raw_data = models.LongStringField(blank=True, doc="Log: TrialIndex_Correct_RT")


# --- FUNCTIONS ---
def get_stroop_trials():
    """Generates the sequence of trials"""
    trials = []

    for i in range(C.NUM_TRIALS):
        text_word = random.choice(C.WORDS)

        # 50% Chance für Inkongruenz
        if random.random() > 0.5:
            # Inkongruent (Schwer)
            available_colors = [c for c in C.COLORS if c[1].upper() != text_word]
            color_hex, color_name = random.choice(available_colors)
            is_congruent = False
        else:
            # Kongruent (Einfach)
            matching_color = next(c for c in C.COLORS if c[1].upper() == text_word)
            color_hex, color_name = matching_color
            is_congruent = True

        trials.append({
            'word': text_word,
            'color': color_hex,  # Hex Code für CSS
            'correct': color_name,  # Richtige Antwort als Text
            'is_congruent': is_congruent  # <--- WICHTIG FÜR EXCEL
        })

    return trials


# --- PAGES ---

class StroopInstruction(Page):
    pass


class StroopTask(Page):
    form_model = 'player'
    form_fields = ['stroop_score', 'stroop_errors', 'stroop_avg_rt', 'stroop_raw_data']
    timeout_seconds = C.TIMEOUT_SECONDS

    @staticmethod
    def js_vars(player: Player):
        # Pass the generated trials to JavaScript
        return {
            'trials': get_stroop_trials()
        }


class StroopResults(Page):
    pass


page_sequence = [StroopInstruction, StroopTask, StroopResults]