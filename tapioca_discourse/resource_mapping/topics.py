# -*- coding: utf-8 -*-

TOPICS_MAPPING = {
    'topics_get': {
        'resource': 't/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1%7Bid%7D.json%2Fget'),
        'methods': ['GET'],
    },
    'topics_get_latest': {
        'resource': 'latest.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1latest.json%2Fget'),
        'methods': ['GET'],
    },
    'topics_get_top': {
        'resource': 'top.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1top.json%2Fget'),
        'methods': ['GET'],
    },
    'topics_get_top_filtered': {
        'resource': 'top/{flag}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1top~1%7Bflag%7D.json%2Fget'),
        'methods': ['GET'],
    },
    'topics_create': {
        'resource': 'posts',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1posts%2Fpost'),
        'methods': ['POST'],
    },
    'topics_create_timed': {
        'resource': 't/{id}/status_update',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1%7Bid%7D~1status_update%2Fpost'),
        'methods': ['POST'],
    },
    'topics_update': {
        'resource': 't/-/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1-~1%7Bid%7D.json%2Fput'),
        'methods': ['PUT'],
    },
    'topics_update_timestamp': {
        'resource': 't/{id}/change-timestamp',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1%7Bid%7D~1change-timestamp%2Fput'),
        'methods': ['PUT'],
    },
    'topics_delete': {
        'resource': 't/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1%7Bid%7D.json%2Fdelete'),
        'methods': ['DELETE'],
    },
    'topics_bookmark': {
        'resource': '/t/{id}/bookmark',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1%7Bid%7D~1bookmark%2Fput'),
        'methods': ['PUT'],
    },
    'topics_close': {
        'resource': 't/{id}/status',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1%7Bid%7D~1status%2Fput'),
        'methods': ['PUT'],
    },
    'topics_set_notification_level': {
        'resource': 't/{id}/notifications',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1%7Bid%7D~1notifications%2Fpost'),
        'methods': ['POST'],
    },
}
