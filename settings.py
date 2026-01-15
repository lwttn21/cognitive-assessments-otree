from os import environ

SESSION_CONFIGS = [
    dict(
        name="multitaskingtest",
        display_name="Multitasking Test",
        app_sequence=['multitaskingtest'],
        num_demo_participants=1,
    ),
    dict(
        name="survey_mfi",
        display_name="Survey MFI",
        app_sequence=['survey_mfi'],
        num_demo_participants=1,
    ),
    dict(
        name="survey_vas",
        display_name="Survey VAS",
        app_sequence=['survey_vas'],
        num_demo_participants=1,
    ),
    dict(
        name="task_go_no_go",
        display_name="Task Go/No Go",
        app_sequence=['task_go_no_go'],
        num_demo_participants=1,
    ),
    dict(
        name="task_mot",
        display_name="Task Motor Screening",
        app_sequence=['task_mot'],
        num_demo_participants=1,
    ),
    dict(
        name="task_n_back",
        display_name="Task N-Back",
        app_sequence=['task_n_back'],
        num_demo_participants=1,
    ),
    dict(
        name="task_rti",
        display_name="Task Reaction Time",
        app_sequence=['task_rti'],
        num_demo_participants=1,
    ),
    dict(
        name="task_ssp",
        display_name="Task Spatial Span",
        app_sequence=['task_ssp'],
        num_demo_participants=1,
    ),
    dict(
        name="task_stroop",
        display_name="Task Stroop",
        app_sequence=['task_stroop'],
        num_demo_participants=1,
    ),
    dict(
        name="task_tmt_a",
        display_name="Task TMT A",
        app_sequence=['task_tmt_a'],
        num_demo_participants=1,
    ),
    dict(
        name="task_tmt_b",
        display_name="Task TMT B",
        app_sequence=['task_tmt_b'],
        num_demo_participants=1,
    ),
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