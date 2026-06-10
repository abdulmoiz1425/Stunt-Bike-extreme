from django.urls import path
from . import views

urlpatterns = [
    path('stunt-bike-extreme-mod-apk/', views.mod_apk, name='mod_apk'),
    path('stunt-bike-extreme-for-pc/', views.for_pc, name='for_pc'),
    path('stunt-bike-extreme-for-ios/', views.for_ios, name='for_ios'),
    path('stunt-bike-extreme-for-smart-tv/', views.for_smart_tv, name='for_smart_tv'),
    path('stunt-bike-extreme-for-tv-box/', views.for_tv_box, name='for_tv_box'),
    path('old-versions/', views.old_versions, name='old_versions'),
    path('download/<int:version_id>/', views.download_apk, name='download_apk'),
    path('download/<int:version_id>/start/', views.serve_download, name='serve_download'),
    path('download/success/', views.download_success, name='download_success'),
]
