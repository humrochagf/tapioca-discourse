# -*- coding: utf-8 -*-

USERS_MAPPING = {
    'users_list_one': {
        'resource': 'users/{username}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1users~1{username}.json%2Fget'),
        'methods': ['GET'],
    },
    'users_update_avatar': {
        'resource': 'users/{username}/preferences/avatar/pick',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1users~1{username}~1preferences~1avatar~1pick%2Fput'),
        'methods': ['PUT'],
    },
    'users_update_email': {
        'resource': 'users/{username}/preferences/email',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1users~1{username}~1preferences~1email%2Fput'),
        'methods': ['PUT'],
    },
    'users_create': {
        'resource': 'users',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1users%2Fpost'),
        'methods': ['POST'],
    },
    'users_list_public_all': {
        'resource': 'directory_items.json?period={period}&order={order}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1directory_items.json%3Fperiod%3D{period}%26order%3D{order}%2Fget'),
        'methods': ['GET'],
    },
    'users_delete': {
        'resource': 'admin/users/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1admin~1users~1{id}.json%2Fdelete'),
        'methods': ['DELETE'],
    },
    'users_list': {
        'resource': 'admin/users/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1admin~1users~1{id}.json%2Fdelete'),
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
                 'Users%2Fpaths%2F~1admin~1users~1{id}~1log_out%2Fpost'),
        'methods': ['POST'],
    },
    'users_refresh_gravatar': {
        'resource': 'user_avatar/{username}/refresh_gravatar.json ',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1user_avatar~1{username}~1refresh_gravatar.json%2Fpost'),
        'methods': ['POST'],
    },

}
