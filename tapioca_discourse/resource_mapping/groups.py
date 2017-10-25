# -*- coding: utf-8 -*-

GROUPS_MAPPING = {
    'groups_list': {
        'resource': 'groups/search.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1groups~1search.json%2Fget'),
        'methods': ['GET'],
    },
    'groups_create': {
        'resource': 'admin/groups',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1admin~1groups%2Fpost'),
        'methods': ['POST'],
    },
    'groups_delete': {
        'resource': 'admin/groups/{group_id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1admin~1groups~1{group_id}.json%2Fdelete'),
        'methods': ['DELETE'],
    },
    'groups_update': {
        'resource': 'admin/groups/{group_id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1admin~1groups~1{group_id}.json%2Fput'),
        'methods': ['PUT'],
    },
    'groups_list_members': {
        'resource': 'groups/{group_name}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1groups~1{group_name}~1members.json%2Fget'),
        'methods': ['GET'],
    },
    'groups_add_users': {
        'resource': '/groups/{group_id}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1groups~1{group_id}~1members.json%2Fput'),
        'methods': ['PUT'],
    },
    'groups_delete_users': {
        'resource': 'groups/{group_id}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Users%2Fpaths%2F~1admin~1users~1{id}.json%2Fdelete'),
        'methods': ['DELETE'],
    },
}
