from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
    path('search/', views.search, name='search'),
]
