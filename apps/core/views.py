from django.shortcuts import render
from django.db.models import Q

from .models import FAQ, SiteSettings
from apps.apk.models import Platform, APKVersion
from apps.blog.models import Article


def home(request):
    android = Platform.objects.filter(platform_type='android', is_active=True).first()
    latest_version = android.get_latest_version() if android else None
    all_versions = APKVersion.objects.filter(platform=android).order_by('-release_date')[:5] if android else []
    screenshots = android.screenshots.all() if android else []
    faqs = FAQ.objects.filter(is_active=True)
    recent_posts = Article.objects.filter(is_published=True)[:3]
    platforms = Platform.objects.filter(is_active=True).exclude(platform_type='android').order_by('order')

    return render(request, 'home.html', {
        'platform': android,
        'latest_version': latest_version,
        'all_versions': all_versions,
        'screenshots': screenshots,
        'faqs': faqs,
        'recent_posts': recent_posts,
        'platforms': platforms,
        'page_title': 'Stunt Bike Extreme APK Download - Latest Version',
        'meta_description': 'Download Stunt Bike Extreme APK latest version for Android. Free motorcycle stunt racing game with stunning graphics and thrilling gameplay.',
    })


def about(request):
    return render(request, 'pages/about.html', {
        'page_title': 'About Us - Stunt Bike Extreme',
        'meta_description': 'Learn about the Stunt Bike Extreme APK website and our mission to provide safe, free APK downloads.',
    })


def privacy(request):
    return render(request, 'pages/privacy.html', {
        'page_title': 'Privacy Policy - Stunt Bike Extreme',
        'meta_description': 'Privacy policy for the Stunt Bike Extreme APK download website.',
    })


def terms(request):
    return render(request, 'pages/terms.html', {
        'page_title': 'Terms & Conditions - Stunt Bike Extreme',
        'meta_description': 'Terms and conditions for using the Stunt Bike Extreme APK website.',
    })


def disclaimer(request):
    return render(request, 'pages/disclaimer.html', {
        'page_title': 'Disclaimer - Stunt Bike Extreme',
        'meta_description': 'Disclaimer for the Stunt Bike Extreme fan guide website. Important information about our content, APK information, and user responsibilities.',
    })


def cookie_policy(request):
    return render(request, 'pages/cookie.html', {
        'page_title': 'Cookie Policy - Stunt Bike Extreme',
        'meta_description': 'Cookie policy for the Stunt Bike Extreme website. Learn how we use cookies and how to manage your preferences.',
    })


def search(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        article_results = Article.objects.filter(
            is_published=True
        ).filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(excerpt__icontains=query)
        )
        results = list(article_results)

    return render(request, 'search/results.html', {
        'query': query,
        'results': results,
        'page_title': f'Search: {query} - Stunt Bike Extreme',
    })


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
