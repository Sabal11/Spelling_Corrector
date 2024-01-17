"""
URL configuration for source project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# source/urls.py

from django.contrib import admin
from django.urls import path, include
from source import views
from spelling_corrector.views import check_spelling  # Correct the import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('aboutus', views.about),
    path('contactus', views.contact),
    path('contactus', views.click),
    path('check_spelling/', check_spelling, name='check_spelling'),
    path('spelling_corrector/', include('spelling_corrector.urls')),
]

