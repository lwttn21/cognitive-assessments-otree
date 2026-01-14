from otree.api import *
import json, random, time


class C(BaseConstants):
    NAME_IN_URL = 'TestDustinTP'
    PLAYERS_PER_GROUP = None

    # ---- DESIGNPARAMETER ----
    N_BLOCKS = 2
    N_STIM = 8                      # pro Block
    PATTERNS_PER_ROUND = 4          # <-- du willst 4 Muster pro Runde

    NUM_ROUNDS = (N_BLOCKS * N_STIM) // PATTERNS_PER_ROUND  # 16/4 = 4 Runden

    STIM_MS = 5000                  # <-- 5 Sekunden Anzeige pro Muster
    ISI_MIN_MS = 400
    ISI_MAX_MS = 1200

    @staticmethod
    def file_list(prefix, n):
        return [f"global/patterns/{prefix}_{i:02d}.png" for i in range(1, n + 1)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # pro Runde (oTree speichert Player pro round_number)
    study_json = models.LongStringField(blank=True)
    immrec_json = models.LongStringField(blank=True)

    imm_score = models.IntegerField(initial=0)
    imm_mean_rt_ms = models.FloatField(blank=True)


# --------- Helper: stimuli in participant.vars bauen ----------
def ensure_stimuli(participant):
    if participant.vars.get('tp_stimuli_built'):
        return

    blocks = []
    for b in range(1, C.N_BLOCKS + 1):
        targets = C.file_list(f"block{b}_targets", C.N_STIM)
        foil1 = C.file_list(f"block{b}_foil1", C.N_STIM)   # Foils für Immediate Recognition

        order = list(range(C.N_STIM))
        random.shuffle(order)

        blocks.append(dict(
            block=b,
            targets=[targets[i] for i in order],
            foil1=[foil1[i] for i in order],
        ))

    participant.vars['tp_blocks'] = blocks
    participant.vars['tp_stimuli_built'] = True


def flat_targets(participant):
    ensure_stimuli(participant)
    out = []
    for blk in participant.vars['tp_blocks']:
        out += blk['targets']
    return out


def flat_foils1(participant):
    ensure_stimuli(participant)
    out = []
    for blk in participant.vars['tp_blocks']:
        out += blk['foil1']
    return out


def targets_for_round(player: Player):
    all_t = flat_targets(player.participant)
    start = (player.round_number - 1) * C.PATTERNS_PER_ROUND
    end = start + C.PATTERNS_PER_ROUND
    return all_t[start:end]


def foils_for_round(player: Player):
    all_f = flat_foils1(player.participant)
    start = (player.round_number - 1) * C.PATTERNS_PER_ROUND
    end = start + C.PATTERNS_PER_ROUND
    return all_f[start:end]


# ---------------- Pages ----------------
class Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        ensure_stimuli(player.participant)


class Study(Page):
    form_model = 'player'
    form_fields = ['study_json']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            targets=json.dumps(targets_for_round(player)),
            stim_ms=C.STIM_MS,
            isi_min_ms=C.ISI_MIN_MS,
            isi_max_ms=C.ISI_MAX_MS,
        )


class ImmediateRecognition(Page):
    form_model = 'player'
    form_fields = ['immrec_json', 'imm_score', 'imm_mean_rt_ms']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            targets=json.dumps(targets_for_round(player)),
            foils=json.dumps(foils_for_round(player)),
        )


class MyPage(Page):
    """Diese Seite ist die 'Bist du bereit für die nächste Runde?'-Seite."""
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number < C.NUM_ROUNDS


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


# Delay/DelayedRecognition existieren bei dir im Ordner, werden aber NICHT benutzt.
class Delay(Page):
    @staticmethod
    def is_displayed(player: Player):
        return False


class DelayedRecognition(Page):
    @staticmethod
    def is_displayed(player: Player):
        return False


page_sequence = [
    Instructions,
    Study,
    ImmediateRecognition,
    MyPage,     # <-- "Weiter?" zwischen den Runden
    Results,
]