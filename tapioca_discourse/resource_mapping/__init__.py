# -*- coding: utf-8 -*-

from .admin import ADMIN_MAPPING
from .admin_emails import ADMIN_EMAILS_MAPPING
from .backups import BACKUPS_MAPPING
from .badges import BADGES_MAPPING
from .categories import CATEGORIES_MAPPING
from .groups import GROUPS_MAPPING
from .invites import INVITES_MAPPING
from .notifications import NOTIFICATIONS_MAPPING
from .password_reset import PASSWORD_RESET_MAPPING
from .plugins import PLUGINS_MAPPING
from .posts import POSTS_MAPPING
from .private_messages import PRIVATE_MESSAGES_MAPPING
from .topics import TOPICS_MAPPING
from .tags import TAGS_MAPPING
from .search import SEARCH_MAPPING
from .upload import UPLOAD_MAPPING
from .users import USERS_MAPPING
from .user_fields import USER_FIELDS_MAPPING


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
RESOURCE_MAPPING.update(ADMIN_MAPPING)
RESOURCE_MAPPING.update(USERS_MAPPING)
RESOURCE_MAPPING.update(BACKUPS_MAPPING)
RESOURCE_MAPPING.update(GROUPS_MAPPING)
RESOURCE_MAPPING.update(BADGES_MAPPING)
RESOURCE_MAPPING.update(PASSWORD_RESET_MAPPING)
RESOURCE_MAPPING.update(USER_FIELDS_MAPPING)
RESOURCE_MAPPING.update(PASSWORD_RESET_MAPPING)
RESOURCE_MAPPING.update(PLUGINS_MAPPING)