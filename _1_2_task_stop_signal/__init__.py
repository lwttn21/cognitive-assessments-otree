from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '_1_2_task_stop_signal'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 32


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    arrow_direction = models.StringField()
    stop_signal = models.BooleanField()
    response = models.StringField(blank=True)
    reaction_time = models.FloatField(blank=True)
    correct = models.BooleanField(null=True)
    phase = models.IntegerField()

def creating_session(subsession):
    for player in subsession.get_players():
        if player.round_number <= 16:
            player.phase = 1
            player.stop_signal = False
        else:
            player.phase = 2
            player.stop_signal = random.choice([True, False])

        player.arrow_direction = random.choice(['left', 'right'])

class Instructions(Page):
    def is_displayed(player):
        return player.round_number == 1

class Phase2Instructions(Page):
    def is_displayed(player):
        return player.round_number == 17  #phase 2 instructions get displayed directly after phase 1

    def vars_for_template(player):
        return {
            'message': "Ab jetzt können die Beeps erscheinen. Reagiere wie bisher."
        }

class MyPage(Page):
    timeout_seconds = 1.5

    def vars_for_template(player):
        return {
            'arrow': player.arrow_direction,
            'stop_signal': player.stop_signal
        }

    def live_method(player, data):

        if 'timeout' in data:
            return

        # Reactions:
        player.response = data['key']
        player.reaction_time = data['rt']

        if player.stop_signal:
            # Stop-trial + reaction = False
            player.correct = False
            return

        # Go-Trial
        if player.arrow_direction == 'left' and data['key'] == 'f':
            player.correct = True
        elif player.arrow_direction == 'right' and data['key'] == 'j':
            player.correct = True
        else:
            player.correct = False

    def before_next_page(player, timeout_happened):
        if player.field_maybe_none('response') is not None:
            return

        if player.stop_signal:
            player.correct = True
        else:
            player.correct = False

class BlankPage(Page):
    timeout_seconds = 1.0  #length of showing the empty screen in between

class Results(Page):
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS

    def vars_for_template(player):
        trials = player.in_all_rounds()
        return {
            'n_trials': len(trials),
            'n_correct': sum(p.correct for p in trials)
        }

page_sequence = [Instructions, Phase2Instructions, MyPage, BlankPage, Results]