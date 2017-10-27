# -*- coding: utf-8 -*-

USER_FIELDS_MAPPING = {
    'user_fields_list': {
        'resource': 'admin/customize/user_fields.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'User-Fields'),
        'methods': ['GET'],
    },
    'user_fields_create': {
        'resource': 'admin/customize/user_fields.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'User-Fields%2Fpaths%2F~1admin~1customize~1'
                 'user_fields.json%2Fpost'),
        'methods': ['POST'],
    },
    'user_fields_delete': {
        'resource': 'admin/customize/user_fields/{id}',
        'docs': ('http://docs.discourse.org/#tag/'
                 'User-Fields%2Fpaths%2F~1admin~1customize~1'
                 'user_fields~1%7Bid%7D%2Fdelete'),
        'methods': ['DELETE'],
    },
}
