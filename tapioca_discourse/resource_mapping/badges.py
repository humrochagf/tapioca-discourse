# -*- coding: utf-8 -*-

BADGES_MAPPING = {
    'badges_user_list': {
        'resource': 'user_badges/{username}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Badges%2Fpaths%2F~1user_badges~1%7Busername%7D.json%2Fget'),
        'methods': ['GET'],
    },
    'badges_assign': {
        'resource': 'user_badges.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Badges%2Fpaths%2F~1user_badges.json%2Fpost'),
        'methods': ['POST'],
    },
    'badges_list': {
        'resource': 'admin/badges.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Badges%2Fpaths%2F~1admin~1badges.json%2Fget'),
        'methods': ['GET'],
    },
    'badges_create': {
        'resource': 'admin/badges.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Badges%2Fpaths%2F~1admin~1badges.json%2Fpost'),
        'methods': ['POST'],
    },
    'badges_revoke': {
        'resource': 'user_badges/{id}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Badges%2Fpaths%2F~1user_badges~1%7Bid%7D%2Fdelete'),
        'methods': ['DELETE'],
    },
}
