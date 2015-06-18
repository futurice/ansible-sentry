import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf')

from sentry.models import User, Team, Project, Organization, OrganizationMember

{% if sentry_admin_username %}
admin,_ = User.objects.get_or_create(username="{{sentry_admin_username}}",
    defaults={"is_superuser": True, "is_staff": True, "email": "{{sentry_admin_email}}"})
admin.set_password("{{sentry_admin_password}}")
admin.save()

{% for o in sentry_admin_orgs %}
org,_ = Organization.objects.get_or_create(name="{{o}}", defaults={"owner": admin})
om,_ = OrganizationMember.objects.get_or_create(organization=org, user=admin, type=0)
team,_ = Team.objects.get_or_create(name="Sentry", organization=org)
project,_ = Project.objects.get_or_create(name="Backend", defaults={"team": team, "organization": org, "platform": "django"})
{% endfor %}

{% endif %}
