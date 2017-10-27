# -*- coding: utf-8 -*-

USERS_MAPPING = {
    'users_get': {
        'resource': 'users/{username}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1users~1%7Busername%7D.json%2Fget'),
        'methods': ['GET'],
    },
    'users_avatar_update': {
        'resource': 'users/{username}/preferences/avatar/pick',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1users~1%7Busername%7D~1preferences~1'
                 'avatar~1pick%2Fput'),
        'methods': ['PUT'],
    },
    'users_email_update': {
        'resource': 'users/{username}/preferences/email',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1users~1%7Busername%7D~1preferences~1'
                 'email%2Fput'),
        'methods': ['PUT'],
    },
    'users_create': {
        'resource': 'users',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1users%2Fpost'),
        'methods': ['POST'],
    },
    'users_public_list': {
        'resource': 'directory_items.json?period={period}&order={order}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1directory_items.json%3Fperiod'
                 '%3D%7Bperiod%7D%26order%3D%7Border%7D%2Fget'),
        'methods': ['GET'],
    },
    'users_delete': {
        'resource': 'admin/users/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1admin~1users~1%7Bid%7D.json%2Fdelete'),
        'methods': ['DELETE'],
    },
    'users_list': {
        'resource': 'admin/users/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1admin~1users~1list~1%7B'
                 'flag%7D.json%2Fget'),
        'methods': ['GET'],
    },
    'users_list_actions': {
        'resource': 'user_actions.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1user_actions.json%2Fget'),
        'methods': ['GET'],
    },
    'users_logout': {
        'resource': 'admin/users/{id}/log_out ',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1admin~1users~1%7Bid%7D~1log_out%2Fpost'),
        'methods': ['POST'],
    },
    'users_refresh_gravatar': {
        'resource': 'user_avatar/{username}/refresh_gravatar.json ',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1user_avatar~1%7Busername%7D~1'
                 'refresh_gravatar.json%2Fpost'),
        'methods': ['POST'],
    },
}
