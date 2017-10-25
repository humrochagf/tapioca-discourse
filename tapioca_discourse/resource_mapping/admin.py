# -*- coding: utf-8 -*-

ADMIN_MAPPING = {
    'admin_user_suspend': {
        'resource': 'admin/users/{id}/suspend',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1suspend%2Fput'),
        'methods': ['PUT'],
    },
    'admin_user_unsuspend': {
        'resource': 'admin/users/{id}/unsuspend',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1unsuspend%2Fput'),
        'methods': ['PUT'],
    },
    'admin_user_block': {
        'resource': 'admin/users/{id}/block',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1block%2Fput'),
        'methods': ['PUT'],
    },
    'admin_user_unblock': {
        'resource': 'admin/users/{id}/unblock',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1unblock%2Fput'),
        'methods': ['PUT'],
    },
    'admin_user_activate': {
        'resource': 'admin/users/{id}/activate',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1activate%2Fput'),
        'methods': ['PUT'],
    },
    'admin_user_anonymize': {
        'resource': 'admin/users/{id}/anonymize',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1anonymize%2Fput'),
        'methods': ['PUT'],
    },
    'admin_api_key_generate': {
        'resource': 'admin/users/{id}/generate_api_key',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1generate_api_key%2Fpost'),
        'methods': ['POST'],
    },
    'admin_group_assign': {
        'resource': 'admin/users/{id}/groups',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1groups%2Fpost'),
        'methods': ['POST'],
    },
    'admin_group_remove': {
        'resource': 'admin/users/{id}/groups/{group_id}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1users~1%7Bid%7D~1groups~1%7Bgroup_id%7D%2Fdelete'),
        'methods': ['DELETE'],
    },
    'admin_group_create': {
        'resource': 'admin/groups',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1groups%2Fpost'),
        'methods': ['POST'],
    },
    'admin_group_delete': {
        'resource': 'admin/groups/{group_id}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1groups~1%7Bgroup_id%7D.json%2Fdelete'),
        'methods': ['DELETE'],
    },
    'admin_group_members_list': {
        'resource': 'groups/{group_name}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1groups~1%7Bgroup_name%7D~1members.json%2Fget'),
        'methods': ['GET'],
    },
    'admin_group_members_add': {
        'resource': 'groups/{group_id}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1groups~1%7Bgroup_id%7D~1members.json%2Fput'),
        'methods': ['PUT'],
    },
    'admin_group_members_delete': {
        'resource': 'groups/{group_id}/members.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1groups~1%7Bgroup_id%7D~1members.json%2Fdelete'),
        'methods': ['DELETE'],
    },
    'admin_site_settings_show': {
        'resource': 'admin/site_settings.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin%2Fpaths%2F~1admin~1site_settings.json%2Fget'),
        'methods': ['GET'],
    },
}
