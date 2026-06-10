from .models import SiteSettings
from apps.apk.models import Platform


def site_settings(request):
    settings = SiteSettings.get_settings()
    platforms = Platform.objects.filter(is_active=True).order_by('order')
    return {
        'site_settings': settings,
        'nav_platforms': platforms,
    }
