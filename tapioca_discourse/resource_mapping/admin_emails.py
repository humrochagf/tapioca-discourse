# -*- coding: utf-8 -*-

ADMIN_EMAILS_MAPPING = {
    'admin_emails_settings': {
        'resource': 'admin/email.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin-Emails%2Fpaths%2F~1admin~1email.json%2Fget'),
        'methods': ['GET'],
    },
    'admin_emails_get_list_templates': {
        'resource': 'admin/customize/email_templates.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Admin-Emails%2Fpaths%2F~1admin~1customize~'
                 '1email_templates.json%2Fget'),
        'methods': ['GET'],
    },
}
