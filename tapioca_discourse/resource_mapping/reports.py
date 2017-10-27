# -*- coding: utf-8 -*-

REPORTS_MAPPING = {
    'reports_get': {
        'resource': 'page_view_total_reqs',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Reports%2Fpaths%2F~1page_view_total_reqs%2Fget'),
        'methods': ['GET'],
    },

    'reports_start': {
        'resource': 'export_csv/export_entity.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Reports%2Fpaths%2F~1export_csv~1export_entity.json%2Fpost'),
        'methods': ['POST'],
    },
}
