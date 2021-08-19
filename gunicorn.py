import logging
import sys
import helpers


bind = "127.0.0.1:9000"
logconfig_dict = {
    'formatters': {
        'simple': {
            'format': '%(name)s %(levelname)s %(asctime)s: %(message)s'
        },
    },
    'filters': {
        'require_message_is_normal': {
            '()': 'helpers.MessageIsNormal',
        },
        'require_message_is_error': {
            '()': 'helpers.MessageIsError',
        },
    },
    'handlers': {
        'console_stdout': {
            'level': 'DEBUG',
            'filters': ['require_message_is_normal'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
        'console_stderr': {
            'level': 'DEBUG',
            'filters': ['require_message_is_error'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stderr,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console_stdout', 'console_stderr'],
            'level': 'INFO',
        },
        'gunicorn': {
            'handlers': ['console_stdout'],
            'level': 'INFO',
        },
        'gunicorn.access': {
            'handlers': ['console_stdout'],
            'level': 'INFO',
        },
        'gunicorn.error': {
            'handlers': ['console_stdout', 'console_stderr'],
            'level': 'INFO',
        },
    },
    'root': {
        "level": "INFO",
        "handlers": ['console_stdout', 'console_stderr'],
    },
}
