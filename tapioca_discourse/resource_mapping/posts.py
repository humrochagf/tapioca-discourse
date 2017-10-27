# -*- coding: utf-8 -*-

POSTS_MAPPING = {
    'posts_create': {
        'resource': 'posts',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Posts%2Fpaths%2F~1posts%2Fpost'),
        'methods': ['POST'],
    },
    'posts_get': {
        'resource': 'posts/{id}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Posts%2Fpaths%2F~1posts~1%7Bid%7D%2Fget'),
        'methods': ['GET'],
    },
    'posts_update': {
        'resource': 'posts/{id}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Posts%2Fpaths%2F~1posts~1%7Bid%7D%2Fput'),
        'methods': ['PUT'],
    },
    'posts_like': {
        'resource': 'post_actions',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Posts%2Fpaths%2F~1post_actions%2Fpost'),
        'methods': ['POST'],
    },
    'posts_unlike': {
        'resource': 'post_actions/{id}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Posts%2Fpaths%2F~1post_actions~1%7Bid%7D%2Fdelete'),
        'methods': ['DELETE'],
    },
}
