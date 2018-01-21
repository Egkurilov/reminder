host = 'localhost'
port = 8008


class Configuration(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector:telegram:52ylRZBg4fLj' \
                              '@localhost/telegram'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


logging = {
    'version': 1,
    'formatters': {
        'f': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    'handlers': {
        'ch': {'class': 'logging.StreamHandler',
               'formatter': 'f',
               'level': 'DEBUG'},
        'fh': {'class': 'logging.FileHandler',
               'formatter': 'f',
               'filename': 'reminder.log',
               'level': 'DEBUG'}
    },
    'root': {
        'handlers': ['ch', 'fh'],
        'level': 'DEBUG',
    },
}
