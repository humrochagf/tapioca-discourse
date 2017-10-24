# -*- coding: utf-8 -*-

from .admin_emails import ADMIN_EMAILS_MAPPING
from .categories import CATEGORIES_MAPPING
from .invites import INVITES_MAPPING
from .notifications import NOTIFICATIONS_MAPPING
from .posts import POSTS_MAPPING
from .private_messages import PRIVATE_MESSAGES_MAPPING
from .topics import TOPICS_MAPPING
from .tags import TAGS_MAPPING
from .search import SEARCH_MAPPING
from .upload import UPLOAD_MAPPING


RESOURCE_MAPPING = {}
RESOURCE_MAPPING.update(ADMIN_EMAILS_MAPPING)
RESOURCE_MAPPING.update(CATEGORIES_MAPPING)
RESOURCE_MAPPING.update(INVITES_MAPPING)
RESOURCE_MAPPING.update(NOTIFICATIONS_MAPPING)
RESOURCE_MAPPING.update(POSTS_MAPPING)
RESOURCE_MAPPING.update(PRIVATE_MESSAGES_MAPPING)
RESOURCE_MAPPING.update(TOPICS_MAPPING)
RESOURCE_MAPPING.update(TAGS_MAPPING)
RESOURCE_MAPPING.update(SEARCH_MAPPING)
RESOURCE_MAPPING.update(UPLOAD_MAPPING)