# -*- coding: utf-8 -*-

CATEGORIES_MAPPING = {
    'categories_list': {
        'resource': 'categories.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Categories%2Fpaths%2F~1categories.json%2Fget'),
        'methods': ['GET'],
    },
    'categories_create': {
        'resource': 'categories.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Categories%2Fpaths%2F~1categories.json%2Fpost'),
        'methods': ['POST'],
    },
    'categories_update': {
        'resource': 'categories/{id}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Categories%2Fpaths%2F~1categories~1%7Bid%7D%2Fput'),
        'methods': ['PUT'],
    },
}
