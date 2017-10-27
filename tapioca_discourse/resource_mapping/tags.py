# -*- coding: utf-8 -*-

TAGS_MAPPING = {
    'tag_groups_list': {
        'resource': 'tag_groups.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Tags%2Fpaths%2F~1tag_groups.json%2Fget'),
        'methods': ['GET'],
    },
    'tag_groups_create': {
        'resource': 'tag_groups.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Tags%2Fpaths%2F~1tag_groups.json%2Fpost'),
        'methods': ['POST'],
    },
    'tag_groups_get': {
        'resource': 'tag_groups/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Tags%2Fpaths%2F~1tag_groups~1%7Bid%7D.json%2Fget'),
        'methods': ['GET'],
    },
    'tag_groups_update': {
        'resource': 'tag_groups/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Tags%2Fpaths%2F~1tag_groups~1%7Bid%7D.json%2Fput'),
        'methods': ['PUT'],
    },
    'tags_list': {
        'resource': 'tags',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Tags%2Fpaths%2F~1tags%2Fget'),
        'methods': ['GET'],
    },
    'tags_get': {
        'resource': 'tags/{tag}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Tags%2Fpaths%2F~1tags~1%7Btag%7D%2Fget'),
        'methods': ['GET'],
    },
}
