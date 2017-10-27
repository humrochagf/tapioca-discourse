# -*- coding: utf-8 -*-

PRIVATE_MESSAGES_MAPPING = {
    'private_messages_get_list_received': {
        'resource': 'topics/private-messages/{username}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Private-Messages%2Fpaths%2F~1topics~1private-messages~1'
                 '%7Busername%7D.json%2Fget'),
        'methods': ['GET'],
    },
    'private_messages_get_list_sent': {
        'resource': 'topics/private-messages-sent/{username}.json',
        'docs': ('http://docs.discourse.org/#tag/'
                 'Private-Messages%2Fpaths%2F~1topics~1'
                 'private-messages-sent~1%7Busername%7D.json%2Fget'),
        'methods': ['GET'],
    },
}
