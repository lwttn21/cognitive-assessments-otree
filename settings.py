from os import environ

# =============================================================================
# COGNITIVE ASSESSMENT BATTERY - MENTAL FATIGUE STUDY
#
# Structure:
# 1.x - Objective Cognitive Tasks (Performance-based metrics)
# 2.x - Subjective Questionnaires (Self-report measures)
# =============================================================================

SESSION_CONFIGS = [
    dict(
        name='session_Go_No_Go',
        display_name="1.1 Go No Go Task",
        app_sequence=['_1_1_task_go_no_go'],
        num_demo_participants=1,
    ),
    dict(
        name="session_rti",
        display_name="1.1 Reaction Time Task",
        app_sequence=['_1_1_task_rti'],
        num_demo_participants=1,
    ),
    dict(
        name="session_rvp",
        display_name="1.1 Rapid Visual Information Processing Task",
        app_sequence=['_1_1_task_rvp'],
        num_demo_participants=1,
    ),
    dict(
        name='session_stop_signal',
        display_name="1.2 Stop Signal Task",
        app_sequence=['_1_2_task_stop_signal'],
        num_demo_participants=1,
    ),
    dict(
        name="session_stroop",
        display_name="1.2 Stroop Task",
        app_sequence=['_1_2_task_stroop'],
        num_demo_participants=1,
    ),
    dict(
        name="session_switching",
        display_name="1.2 Switching Task",
        app_sequence=['_1_2_task_switching'],
        num_demo_participants=1,
    ),
    dict(
        name="session_tmt_a",
        display_name="1.2 Trail Making Test A",
        app_sequence=['_1_2_task_tmt_a'],
        num_demo_participants=1,
    ),
    dict(
        name="session_tmt_b",
        display_name="1.2 Trail Making Test B",
        app_sequence=['_1_2_task_tmt_b'],
        num_demo_participants=1,
    ),
    dict(
        name="session_mot",
        display_name="1.3 Motor Screening Task",
        app_sequence=['_1_3_task_mot'],
        num_demo_participants=1,
    ),
    dict(
        name="session_n_back",
        display_name="1.3 N-Back Task",
        app_sequence=['_1_3_task_n_back'],
        num_demo_participants=1,
    ),
    dict(
        name="session_ssp",
        display_name="1.3 Spatial Span Task",
        app_sequence=['_1_3_task_ssp'],
        num_demo_participants=1,
    ),
    dict(
        name="session_survey_mfi",
        display_name="2. Multidimensional Fatigue Inventory Survey",
        app_sequence=['_2_survey_mfi'],
        num_demo_participants=1,
    ),
    dict(
        name="session_survey_vas",
        display_name="2. Visual Analogue Scale Survey",
        app_sequence=['_2_survey_vas'],
        num_demo_participants=1,
    ),


    dict(
        name='Task_matb',
        display_name='3. Matb Task',
        app_sequence=['_3_task_matb'],
        num_demo_participants=1,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4730736264686'

DEBUG = False