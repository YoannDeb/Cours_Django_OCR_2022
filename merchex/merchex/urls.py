"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>', views.band_detail, name='band-detail'),
    path('bands/listings/<int:band_id>', views.band_listing_list, name='band-listing-list'),
    path('listings/', views.listing_list, name='listing-list'),
    path('listings/<int:listing_id>', views.listing_detail, name='listing-detail'),
    path('about/', views.about),
    path('contact/', views.contact, name='contact'),
    path('email_sent/', views.email_sent, name='email-sent')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
