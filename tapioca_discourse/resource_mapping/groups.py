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
                 'Groups%2Fpaths%2F~1admin~1groups~1%7Bgroup_id'
                 '%7D.json%2Fdelete'),
        'methods': ['DELETE'],
    },
    'groups_update': {
        'resource': 'admin/groups/{group_id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1admin~1groups~1%7Bgroup_id'
                 '%7D.json%2Fput'),
        'methods': ['PUT'],
    },
    'group_members_list': {
        'resource': 'groups/{group_name}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1groups~1%7Bgroup_name'
                 '%7D~1members.json%2Fget'),
        'methods': ['GET'],
    },
    'group_members_add': {
        'resource': '/groups/{group_id}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1groups~1%7Bgroup_id'
                 '%7D~1members.json%2Fput'),
        'methods': ['PUT'],
    },
    'group_members_delete': {
        'resource': 'groups/{group_id}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Groups%2Fpaths%2F~1groups~1%7Bgroup_id%7D~1'
                 'members.json%2Fdelete'),
        'methods': ['DELETE'],
    },
}
