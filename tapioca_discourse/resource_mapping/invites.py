# -*- coding: utf-8 -*-

INVITES_MAPPING = {
    'invite_user_to_topic': {
        'resource': 't/{id}/invite',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Invites%2Fpaths%2F~1t~1%7Bid%7D~1invite%2Fpost'),
        'methods': ['POST'],
    },
    'invite_user_by_email': {
        'resource': 'invites',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Invites%2Fpaths%2F~1invites%2Fpost'),
        'methods': ['POST'],
    },
    'invite_link_create': {
        'resource': 'invites/link',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Invites%2Fpaths%2F~1invites~1link%2Fpost'),
        'methods': ['POST'],
    },
}
