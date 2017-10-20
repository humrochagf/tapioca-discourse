# coding: utf-8

RESOURCE_MAPPING = {
    # categories
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

    # invites
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

    # topics
    'topics_create': {
        'resource': 'posts',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1posts%2Fpost'),
        'methods': ['POST'],
    },
    'topics_retrieve': {
        'resource': 't/{id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Topics%2Fpaths%2F~1t~1%7Bid%7D.json%2Fget'),
        'methods': ['GET'],
    },
}
