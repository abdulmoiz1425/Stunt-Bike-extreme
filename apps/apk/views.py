import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404
from django.db.models import F

from .models import Platform, APKVersion
from apps.core.models import FAQ


def _platform_context(platform_type):
    platform = get_object_or_404(Platform, platform_type=platform_type, is_active=True)
    latest_version = platform.get_latest_version()
    all_versions = APKVersion.objects.filter(platform=platform).order_by('-release_date')
    screenshots = platform.screenshots.all()
    faqs = FAQ.objects.filter(is_active=True)
    return {
        'platform': platform,
        'latest_version': latest_version,
        'all_versions': all_versions,
        'screenshots': screenshots,
        'faqs': faqs,
        'page_title': platform.meta_title,
        'meta_description': platform.meta_description,
    }


def mod_apk(request):
    return render(request, 'apk/platform.html', _platform_context('mod'))


def for_pc(request):
    return render(request, 'apk/platform.html', _platform_context('pc'))


def for_ios(request):
    return render(request, 'apk/platform.html', _platform_context('ios'))


def for_smart_tv(request):
    return render(request, 'apk/platform.html', _platform_context('smart_tv'))


def for_tv_box(request):
    return render(request, 'apk/platform.html', _platform_context('tv_box'))


def old_versions(request):
    android = Platform.objects.filter(platform_type='android', is_active=True).first()
    versions = APKVersion.objects.filter(platform=android).order_by('-release_date') if android else []
    all_platforms = Platform.objects.filter(is_active=True)
    selected_platform_type = request.GET.get('platform', 'android')
    selected_platform = Platform.objects.filter(
        platform_type=selected_platform_type, is_active=True
    ).first() or android
    if selected_platform:
        versions = APKVersion.objects.filter(platform=selected_platform).order_by('-release_date')

    return render(request, 'apk/old_versions.html', {
        'versions': versions,
        'all_platforms': all_platforms,
        'selected_platform': selected_platform,
        'page_title': 'Stunt Bike Extreme Old Versions — APK Version History',
        'meta_description': 'Download older versions of Stunt Bike Extreme APK. Full version history archive.',
    })


def download_apk(request, version_id):
    """Step 1 — show the intermediate confirmation/instruction page."""
    version = get_object_or_404(APKVersion, pk=version_id)
    has_file = bool(version.apk_file) or (version.external_url and version.external_url != '#')
    return render(request, 'apk/download_intermediate.html', {
        'version': version,
        'platform': version.platform,
        'no_file': not has_file,
        'page_title': f'Download {version.platform.name} v{version.version} — Stunt Bike Extreme',
        'meta_description': f'Download {version.platform.name} version {version.version} free for Android.',
    })


def serve_download(request, version_id):
    """Step 2 — increment counter and deliver the actual file."""
    version = get_object_or_404(APKVersion, pk=version_id)
    APKVersion.objects.filter(pk=version_id).update(download_count=F('download_count') + 1)

    if version.apk_file:
        file_path = version.apk_file.path
        if not os.path.exists(file_path):
            raise Http404('APK file not found on server.')
        filename = os.path.basename(file_path)
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        return response

    if version.external_url and version.external_url != '#':
        return redirect(version.external_url)

    # No file configured — go back to intermediate page with an error flag
    return render(request, 'apk/download_intermediate.html', {
        'version': version,
        'platform': version.platform,
        'no_file': True,
        'page_title': f'Download {version.platform.name} — Stunt Bike Extreme',
    })


def download_success(request):
    last_version = request.session.get('last_downloaded_version', 'Stunt Bike Extreme APK')
    return render(request, 'apk/download_success.html', {
        'version_name': last_version,
        'page_title': 'Download Started — Stunt Bike Extreme',
    })
