from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, FAQ


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Branding', {'fields': ('site_name', 'tagline', 'logo', 'favicon')}),
        ('Contact', {'fields': ('contact_email',)}),
        ('Social Media', {'fields': ('facebook_url', 'twitter_url', 'youtube_url', 'instagram_url')}),
        ('Analytics', {'fields': ('google_analytics_id',)}),
        ('Footer', {'fields': ('footer_text', 'cookie_notice')}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('question',)
    ordering = ('order',)
