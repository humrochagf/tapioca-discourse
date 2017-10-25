# -*- coding: utf-8 -*-

PASSWORD_RESET_MAPPING = {
    'password_reset_send': {
        'resource': 'session/forgot_password',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Password-Reset%2Fpaths%2F~1session~1forgot_password%2Fpost'),
        'methods': ['POST'],
    },
    'password_reset_create': {
        'resource': 'users/password-reset/{token}',
        'docs': ('http://docs.discourse.org/#tag/'
                'Password-Reset%2Fpaths%2F~1users~1password-reset~1{token}%2Fput'),
        'methods': ['PUT'],
    },
}
