from otree.api import *
import random
import time

doc = """
CANTAB-like Multitasking Test (MTT)
"""

class Constants(BaseConstants):
    name_in_url = 'mtt'
    players_per_group = None
    num_rounds = 40

    SINGLE_TASK_ROUNDS = list(range(1, 21))
    MULTI_TASK_ROUNDS = list(range(21, 41))

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    rule = models.StringField()
    arrow_side = models.StringField()
    arrow_direction = models.StringField()
    correct_response = models.StringField()
    response = models.StringField(blank=True)
    correct = models.BooleanField()
    reaction_time = models.FloatField()

# ------------------------------------------------

def creating_session(subsession):
    for player in subsession.get_players():
        if subsession.round_number in Constants.SINGLE_TASK_ROUNDS:
            player.rule = 'SIDE'
        else:
            player.rule = random.choice(['SIDE', 'DIRECTION'])

        player.arrow_side = random.choice(['LEFT', 'RIGHT'])
        player.arrow_direction = random.choice(['LEFT', 'RIGHT'])

        if player.rule == 'SIDE':
            player.correct_response = player.arrow_side
        else:
            player.correct_response = player.arrow_direction

# ------------------------------------------------

class Task(Page):
    timeout_seconds = 5

    @staticmethod
    def vars_for_template(player):
        return dict(
            rule=player.rule,
            arrow_side=player.arrow_side,
            arrow_direction=player.arrow_direction,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.response is None:
            player.correct = False
            player.reaction_time = None
        else:
            player.correct = player.response == player.correct_response

page_sequence = [Task]
