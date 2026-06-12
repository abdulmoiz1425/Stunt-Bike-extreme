from django.conf import settings as django_settings

from .models import SiteSettings
from apps.apk.models import Platform


def site_settings(request):
    settings = SiteSettings.get_settings()
    platforms = Platform.objects.filter(is_active=True).order_by('order')
    return {
        'site_settings': settings,
        'nav_platforms': platforms,
        'canonical_url': django_settings.SITE_DOMAIN + request.path,
        'site_domain': django_settings.SITE_DOMAIN,
    }
