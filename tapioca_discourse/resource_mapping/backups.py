# -*- coding: utf-8 -*-

BACKUPS_MAPPING = {
    'backups_list': {
        'resource': 'admin/backups.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Backups%2Fpaths%2F~1admin~1backups.json%2Fget'),
        'methods': ['GET'],
    },
    'backups_create': {
        'resource': 'admin/backups.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Backups%2Fpaths%2F~1admin~1backups.json%2Fpost'),
        'methods': ['POST'],
    },
    'backups_update_readonly_mode': {
        'resource': 'admin/backups/readonly.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Backups%2Fpaths%2F~1admin~1backups~1readonly%2Fput'),
        'methods': ['PUT'],
    },
}
