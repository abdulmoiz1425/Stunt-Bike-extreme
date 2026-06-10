from django.contrib import admin
from django.utils.html import format_html
from .models import Platform, APKVersion, Screenshot


class APKVersionInline(admin.TabularInline):
    model = APKVersion
    extra = 1
    fields = ('version', 'apk_file', 'external_url', 'file_size', 'android_requirement',
              'release_date', 'is_latest', 'rating', 'download_count')
    readonly_fields = ('download_count',)


class ScreenshotInline(admin.TabularInline):
    model = Screenshot
    extra = 2
    fields = ('image', 'caption', 'order')


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform_type', 'order', 'is_active', 'latest_version_display', 'total_downloads')
    list_editable = ('order', 'is_active')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [APKVersionInline, ScreenshotInline]
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'slug', 'platform_type', 'tagline', 'description', 'order', 'is_active')}),
        ('Content', {'fields': ('features', 'installation_guide')}),
        ('SEO', {'fields': ('meta_title', 'meta_description')}),
    )

    def latest_version_display(self, obj):
        v = obj.get_latest_version()
        return v.version if v else '—'
    latest_version_display.short_description = 'Latest Version'

    def total_downloads(self, obj):
        total = sum(v.download_count for v in obj.apkversion_set.all())
        return format_html('<strong>{:,}</strong>', total)
    total_downloads.short_description = 'Total Downloads'


@admin.register(APKVersion)
class APKVersionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'platform', 'version', 'file_size', 'release_date',
                    'is_latest', 'download_count', 'rating')
    list_filter = ('platform', 'is_latest')
    list_editable = ('is_latest',)
    readonly_fields = ('download_count',)
    ordering = ('-release_date',)


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'platform', 'order', 'preview')
    list_filter = ('platform',)
    list_editable = ('order',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return '—'
    preview.short_description = 'Preview'
