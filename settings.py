from os import environ

SESSION_CONFIGS = [
    dict(
        name='Task_Go_No_Go',
        display_name="Go no Go Task",
        app_sequence=['task_go_no_go'],
        num_demo_participants=1,
    ),
    dict(
        name='n_back_test',
        display_name="N-Back Task",
        app_sequence=['task_n_back'],  # Hier muss der Ordnername stehen
        num_demo_participants=1,
    ),
    dict(
        name='stroop',
        display_name="Stroop Task",
        num_demo_participants=1,
        app_sequence=['task_stroop'],
    ),
    dict(
        name='survey_mfi',
        display_name="Mental Fatigue Inventory",
        num_demo_participants=1,
        app_sequence=['survey_mfi'],
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
