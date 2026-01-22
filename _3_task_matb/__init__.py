from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'matb_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Standard difficulty levels for the Unity application
    LEVELS = ["level1", "level2", "level3", "level4", "level5", "level6"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Data fields for the four MATB subsystems
    sysmon_score = models.IntegerField(initial=0)
    tracking_score = models.IntegerField(initial=0)
    comm_score = models.IntegerField(initial=0)
    resman_score = models.IntegerField(initial=0)

    # Calculated total performance score
    performance_score = models.FloatField()

class MatbInstructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        # Zeige die Instruktionen nur in der ersten Runde
        return player.round_number == 1

# PAGES
class MatbTask(Page):
    form_model = 'player'
    # These fields receive live data from Unity via JavaScript
    form_fields = ['sysmon_score', 'tracking_score', 'comm_score', 'resman_score']

    @staticmethod
    def vars_for_template(player: Player):
        # Selects the difficulty level based on the current round
        return dict(
            level_name=C.LEVELS[player.round_number - 1]
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Weighted calculation of total performance (Standard MATB weighting)
        # Even if the timer expires, the score is calculated based on current values
        player.performance_score = round(
            player.sysmon_score * 0.4 +
            player.tracking_score * 0.25 +
            player.comm_score * 0.2 +
            player.resman_score * 0.15, 2
        )


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            total_score=player.performance_score
        )


page_sequence = [MatbInstructions, MatbTask, Results]