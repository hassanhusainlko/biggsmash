from django.conf import settings
from django.db import migrations


def set_default_site(apps, schema_editor):
    """Point the sites framework at the public site so sitemap URLs are correct."""
    Site = apps.get_model("sites", "Site")
    site_id = getattr(settings, "SITE_ID", 1)
    Site.objects.update_or_create(
        pk=site_id,
        defaults={
            "domain": getattr(settings, "SITE_DOMAIN", "biggsmashoutreach.com"),
            "name": getattr(settings, "SITE_NAME", "Biggsmash Outreach"),
        },
    )


def unset_default_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.filter(pk=getattr(settings, "SITE_ID", 1)).update(
        domain="example.com",
        name="example.com",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(set_default_site, unset_default_site),
    ]
