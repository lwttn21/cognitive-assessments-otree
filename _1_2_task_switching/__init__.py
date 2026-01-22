from otree.api import *
import random

doc = """
Task Switching Paradigm. 
Upper Half: LOCATION | Lower Half: DIRECTION
Controls: Arrow Keys (Left/Right)
"""


class C(BaseConstants):
    NAME_IN_URL = 'task_switching'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    STIMULUS_DURATION = None  # None = No time limit


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response = models.StringField(blank=True)

    rule = models.StringField()
    stimulus_side = models.StringField()
    stimulus_direction = models.StringField()
    is_correct = models.BooleanField()
    reaction_time = models.FloatField()


def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            for r in range(1, C.NUM_ROUNDS + 1):
                p = player.in_round(r)
                p.rule = random.choice(['LOCATION', 'DIRECTION'])
                p.stimulus_side = random.choice(['left', 'right'])
                p.stimulus_direction = random.choice(['left', 'right'])


# --- PAGES ---

class Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        # Wir berechnen die Sekunden hier, damit das Template nicht rechnen muss
        return dict(
            has_timeout=C.STIMULUS_DURATION is not None,
            duration_seconds=C.STIMULUS_DURATION / 1000 if C.STIMULUS_DURATION else 0
        )


class MyPage(Page):
    form_model = 'player'
    form_fields = ['response', 'reaction_time']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            rule=player.rule,
            stimulus_direction=player.stimulus_direction,
            stimulus_side=player.stimulus_side
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(stimulus_duration=C.STIMULUS_DURATION)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        correct_ans = player.stimulus_side if player.rule == 'LOCATION' else player.stimulus_direction
        if player.response:
            player.is_correct = (player.response == correct_ans)
        else:
            player.is_correct = False


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        all_rounds = player.in_all_rounds()
        correct_trials = [p for p in all_rounds if p.is_correct]
        error_trials = [p for p in all_rounds if not p.is_correct]

        valid_rts = [p.reaction_time for p in correct_trials if p.reaction_time is not None]
        mean_rt = round(sum(valid_rts) / len(valid_rts)) if valid_rts else 0

        return dict(
            total_correct=len(correct_trials),
            total_errors=len(error_trials),
            accuracy=round((len(correct_trials) / C.NUM_ROUNDS) * 100, 1),
            mean_rt=mean_rt,
            err_loc=len([p for p in error_trials if p.rule == 'LOCATION']),
            err_dir=len([p for p in error_trials if p.rule == 'DIRECTION'])
        )


page_sequence = [Instructions, MyPage, Results]