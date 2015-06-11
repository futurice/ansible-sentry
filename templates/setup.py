import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf')
from sentry.models import User

{% if sentry_admin_username %}
admin,_ = User.objects.get_or_create(username="{{sentry_admin_username}}",
    defaults={"is_superuser": True, "is_staff": True, "email": "{{sentry_admin_email}}"})
if _:
    admin.set_password("{{sentry_admin_password}}")
    admin.save()
{% endif %}
