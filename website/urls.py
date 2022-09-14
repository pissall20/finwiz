from django.urls import path
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticSitemap

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact_us'),
    path('inner-page/', views.inner_page, name='inner_page'),
    path('about-us/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('sitemap.xml', sitemap, {'sitemaps': {"static": StaticSitemap}},
         name='django.contrib.sitemaps.views.sitemap')
]
